import { MockHomeAssistant } from "../../../src/fake_data/provide_hass";

const IOTERA_HOST = "localhost";
const IOTERA_PORT = "8321";
const IOTERA_PROTOCOL = "ws://";
const IOTERA_SERVER = IOTERA_PROTOCOL + IOTERA_HOST + ":" + IOTERA_PORT;
const IOTERA_LOG = "Iotera";

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
      console.log(IOTERA_LOG, "INCOMING", event);

      // what to do when receiving messages.
      const messageGroup = JSON.parse(event.data);
      messageGroup.forEach((msg) => {
        console.log(msg);
        let msgInfo;
        switch (msg.type) {
          case "event":
            msgInfo = this._wsCommands.get(msg.id);
            console.log("result => event callback to something " + msgInfo);
            // msgInfo.callback(msg.event);
            break;
          case "result":
            msgInfo = this._wsCommands.get(msg.id);
            console.log("result => result callback to something " + msgInfo);
            if (msgInfo !== undefined) {
              msgInfo.resolve(msg.message);
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

  sendMessage(message: IoteraMessage) {
    setTimeout(() => {
      console.log(IOTERA_LOG, "SOCKET STATE", this.socket.readyState);
      if (this.socket.readyState === WebSocket.OPEN) {
        if (!message.id) {
          const messageId = this._genCommandId();
          message.id = messageId;
        }
        console.log(IOTERA_LOG, "SENDING", message);
        this.socket.send(JSON.stringify(message));
      }
    }, 5);
  }

  sendMessagePromise(
    message: IoteraMessage,
    hass: MockHomeAssistant
  ): Promise<any> {
    return new Promise((resolve, reject) => {
      /**
       * hass implementation contains message queueing here. not sure how that works.
       * just return promise for use later.
       */
      const commandId = this._genCommandId();
      message.id = commandId;
      console.log("start promise " + JSON.stringify(message));
      this._wsCommands.set(commandId, { resolve, reject });
      this.sendMessage(message);
    });
  }

  _genCommandId = () => ++this._cmdId;
}
