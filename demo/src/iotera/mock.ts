import {
  IOTERA_ERR_NOT_IMPLEMENTED,
  IoteraConnection,
  IoteraMessage,
} from "./iotera";
import { MockHomeAssistant } from "../../../src/fake_data/provide_hass";

const mockRequest = (message: IoteraMessage, iotera_conn: IoteraConnection) => {
  setTimeout(() => {
    iotera_conn.sendMessage(message);
  }, 2000); // send after 2 seconds.
};

const mockRequestPromise = (
  message: IoteraMessage,
  iotera_conn: IoteraConnection
) => {};

export const iotera_mockPing = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "ping", message: "ping message" }, iotera_connection);
};

export const iotera_mockLovelace = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "lovelace", message: "" }, iotera_connection);
};

export const iotera_mockAuth = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "auth", message: "" }, iotera_connection);
};

export const iotera_mockTranslations = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "translation", message: "" }, iotera_connection);
};

export const iotera_mockHistory = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "history", message: "" }, iotera_connection);
};

export const iotera_mockRecorder = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "recorder", message: "" }, iotera_connection);
};

export const iotera_mockTodo = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "todo", message: "" }, iotera_connection);
};

export const iotera_mockSensor = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "sensor", message: "" }, iotera_connection);
};

export const iotera_mockSystemLog = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "system_log", message: "" }, iotera_connection);
};

export const iotera_mockTemplate = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "template", message: "" }, iotera_connection);
};

export const iotera_mockEvents = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "event", message: "" }, iotera_connection);
};

export const iotera_mockMediaPlayer = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "mediaplayer", message: "" }, iotera_connection);
};

export const iotera_mockFrontend = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "frontend", message: "" }, iotera_connection);
};

export const iotera_mockIcons = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "icon", message: "" }, iotera_connection);
};

export const iotera_mockEnergy = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "energy/get_prefs", message: "" }, iotera_connection);
  mockRequest({ type: "energy/info", message: "" }, iotera_connection);
  mockRequest(
    { type: "energy/fossil_energy_consumption", message: "" },
    iotera_connection
  );
  mockRequest(
    { type: "energy/solar_forecast", message: "" },
    iotera_connection
  );
};

export const iotera_mockPersistentNotification = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest(
    { type: "persistent_notification", message: "" },
    iotera_connection
  );
};

export const iotera_mockConfigEntries = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "config_entry", message: "" }, iotera_connection);
};

export const iotera_mockAreaRegistry = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  mockRequest({ type: "area/registry", message: "" }, iotera_connection);
};

export const iotera_mockEntityRegistry = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant,
  data: any
) => {
  mockRequest({ type: "entity/registry", message: "" }, iotera_connection);
};

export const iotera_mockEnergyEntities = (
  iotera_connection: IoteraConnection,
  mockHass: MockHomeAssistant
) => {
  mockRequest({ type: "energy/entity", message: "" }, iotera_connection);
};

export const iotera_mockEnergyEntities_w_Promise = (
  iotera_connection: IoteraConnection,
  mockHass: MockHomeAssistant
): Promise<any> =>
  iotera_connection.sendMessagePromise(
    { type: "energy/entity", message: "" },
    mockHass
  );
