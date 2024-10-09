import { IoteraConnection } from "./iotera";
import { MockHomeAssistant } from "../../../src/fake_data/provide_hass";

export const iotera_mockLovelace = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("lovelace");
};
export const iotera_mockAuth = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("auth");
};
export const iotera_mockTranslations = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("translation");
};
export const iotera_mockHistory = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("history");
};
export const iotera_mockRecorder = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("recorder");
};
export const iotera_mockTodo = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("todo");
};
export const iotera_mockSensor = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("sensor");
};
export const iotera_mockSystemLog = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("system_log");
};
export const iotera_mockTemplate = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("template");
};
export const iotera_mockEvents = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("event");
};
export const iotera_mockMediaPlayer = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("mediaplayer");
};
export const iotera_mockFrontend = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("frontend");
};
export const iotera_mockIcons = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("icon");
};
export const iotera_mockEnergy = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("energy/get_prefs");
  iotera_connection.sendMessage("energy/info");
  iotera_connection.sendMessage("energy/fossil_energy_consumption");
  iotera_connection.sendMessage("energy/solar_forecast");
};
export const iotera_mockPersistentNotification = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("persistent_notification");
};
export const iotera_mockConfigEntries = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("config_entry");
};
export const iotera_mockAreaRegistry = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant
) => {
  iotera_connection.sendMessage("area_registry");
};
export const iotera_mockEntityRegistry = (
  iotera_connection: IoteraConnection,
  hass: MockHomeAssistant,
  anything: any
) => {
  iotera_connection.sendMessage("entity_registry");
};
