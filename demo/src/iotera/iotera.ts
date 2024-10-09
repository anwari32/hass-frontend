const IOTERA_HOST = "localhost";
const IOTERA_PORT = "8321";
const IOTERA_PROTOCOL = "ws://";
const IOTERA_SERVER = IOTERA_PROTOCOL + IOTERA_HOST + ":" + IOTERA_PORT;
const IOTERA_LOG = "Iotera";

export class IoteraConnection {
  socket: WebSocket;

  _handleMessages: any;

  _handleClose: any;

  static instance: IoteraConnection;

  constructor(socket: WebSocket) {
    this._handleMessages = (event) => {
      console.log(IOTERA_LOG, event);

      // what to do when receiving messages.
    };
    this._handleClose = (event) => {
      console.log(IOTERA_LOG, event);

      // what to do when closing.
    };
    this.socket = socket;
    this.socket.onmessage = this._onmessage;
    this.socket.onopen = this._onopen;
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

  sendMessage(message: string) {
    setTimeout(() => {
      if (this.socket.readyState === WebSocket.OPEN) {
        this.socket.send(message);
      }
    }, 5);
  }

  _onmessage = (event) => {
    console.log(IOTERA_LOG, "socket onmessage", event);

    // callback when socket receiving message.
  };

  _onopen = (event) => {
    console.log(IOTERA_LOG, "socket onopen", event);
  };
}
