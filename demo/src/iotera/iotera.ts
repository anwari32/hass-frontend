import { MockHomeAssistant } from "../../../src/fake_data/provide_hass";

const IOTERA_HOST = "localhost";
const IOTERA_PORT = "8321";
const IOTERA_PROTOCOL = "ws://";
const IOTERA_SERVER = IOTERA_PROTOCOL + IOTERA_HOST + ":" + IOTERA_PORT;
const IOTERA_LOG = "Iotera";
const MAX_RETRY = 5;
const MAX_TIMEDELTA = 1000; // 1 seconds.
const MAX_ATTEMPT = 10;
const INTERVAL_TIME = 100; // 100 ms.

export interface IoteraMessage {
  id?: number;
  type: string;
  message: string;
}

export const IOTERA_ERR_CONNECTION_LOST = 3;
export const IOTERA_ERR_NOT_IMPLEMENTED = 100;

export class IoteraConnection {
  socket: WebSocket;

  _handleMessages: any;

  _handleClose: any;

  _handleOpen: any;

  private _wsCommands: Map<any, any>;

  private _cmdId: number;

  private _access_token: string;

  static instance: IoteraConnection;

  constructor(socket: WebSocket) {
    this._handleMessages = (event) => {
      // what to do when receiving messages.
      const messageGroup = JSON.parse(event.data);
      console.log(IOTERA_LOG, "INCOMING", messageGroup);
      messageGroup.forEach((msg) => {
        let msgInfo;
        switch (msg.type) {
          case "event":
            msgInfo = this._wsCommands.get(msg.id);
            msgInfo.resolve(msg.event);
            break;
          case "result":
            msgInfo = this._wsCommands.get(msg.id);
            if (msgInfo !== undefined) {
              msgInfo.resolve(msg.result);
            }
            break;
          default:
            console.log("Unhandled message " + JSON.stringify(msg));
            break;
        }
      });
    };

    this._handleOpen = (event) => {
      console.log(IOTERA_LOG, "SOCKET OPEN", event);
    };

    this._handleClose = (event) => {
      console.log(IOTERA_LOG, "SOCKET CLOSE", event);

      // what to do when closing.
    };

    this.socket = socket;
    this.socket.onmessage = this._handleMessages;
    this.socket.onopen = this._handleOpen;
    this._wsCommands = new Map<any, any>();
    this._cmdId = 0;
    this._access_token =
      "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIzNDk3NTY5OGQwMDM0NDUwODkzNmEwNzc5MDY2NjE5NyIsImlhdCI6MTcyODg5MTY3MCwiZXhwIjoxNzI4ODkzNDcwfQ.j9y_BGx_yVpCAvoEIWgVyIG3yW68qLSr-Tz9_I9OhMM";
    IoteraConnection.instance = this;
  }

  static get_instance(): IoteraConnection {
    if (this.instance == null) {
      return new IoteraConnection(new WebSocket(IOTERA_SERVER));
    }
    return this.instance;
  }

  connected(): boolean {
    return this.socket.readyState === WebSocket.OPEN;
  }

  _waitForOpenConnection(socket: WebSocket): Promise<any> {
    return new Promise((resolve, reject) => {
      let attemptCount = 0;
      const checkInterval = setInterval(() => {
        if (socket.readyState === WebSocket.OPEN) {
          clearInterval(checkInterval);
          resolve("websocket connection open.");
        }
        attemptCount += 1;
        if (attemptCount > MAX_ATTEMPT) {
          clearInterval(checkInterval);
          reject(
            "websocket connection failed. max attempt reached " + MAX_ATTEMPT
          );
        }
      }, INTERVAL_TIME);
    });
  }

  async sendMessage(message: IoteraMessage) {
    if (!message.id) {
      message.id = this._genCommandId();
    }
    if (!this.connected()) {
      // wait until connection is open.
      console.log(
        IOTERA_LOG,
        "WAITING WEBSOCKET TO OPEN",
        this.socket.readyState
      );
      await this._waitForOpenConnection(this.socket);
    }
    this.socket.send(JSON.stringify(message));
    console.log(
      IOTERA_LOG,
      "WEBSOCKET STATUS",
      this.socket.readyState,
      "SENDING MESSAGE",
      message
    );
  }

  sendMessagePromise(
    message: IoteraMessage,
    hass: MockHomeAssistant
  ): Promise<any> {
    return new Promise((resolve, reject) => {
      const commandId = this._genCommandId();
      message.id = commandId;
      this._wsCommands.set(commandId, { resolve, reject });
      console.log(IOTERA_LOG, "SENDING PROMISE", message);
      this.sendMessage(message);
    });
  }

  _genCommandId = () => ++this._cmdId;
}
