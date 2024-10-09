// Compat needs to be first import
import "../../src/resources/compatibility";
import { customElement } from "lit/decorators";
import { isNavigationClick } from "../../src/common/dom/is-navigation-click";
import { navigate } from "../../src/common/navigate";
import {
  MockHomeAssistant,
  provideHass,
} from "../../src/fake_data/provide_hass";
import { HomeAssistantAppEl } from "../../src/layouts/home-assistant";
import { HomeAssistant } from "../../src/types";
import { selectedDemoConfig } from "./configs/demo-configs";
import { mockAreaRegistry } from "./stubs/area_registry";
import { mockAuth } from "./stubs/auth";
import { mockConfigEntries } from "./stubs/config_entries";
import { mockEnergy } from "./stubs/energy";
import { energyEntities } from "./stubs/entities";
import { mockEntityRegistry } from "./stubs/entity_registry";
import { mockEvents } from "./stubs/events";
import { mockFrontend } from "./stubs/frontend";
import { mockIcons } from "./stubs/icons";
import { mockHistory } from "./stubs/history";
import { mockLovelace } from "./stubs/lovelace";
import { mockMediaPlayer } from "./stubs/media_player";
import { mockPersistentNotification } from "./stubs/persistent_notification";
import { mockRecorder } from "./stubs/recorder";
import { mockSensor } from "./stubs/sensor";
import { mockSystemLog } from "./stubs/system_log";
import { mockTemplate } from "./stubs/template";
import { mockTodo } from "./stubs/todo";
import { mockTranslations } from "./stubs/translations";
import {
  iotera_mockAreaRegistry,
  iotera_mockAuth,
  iotera_mockConfigEntries,
  iotera_mockEnergy,
  iotera_mockEntityRegistry,
  iotera_mockEvents,
  iotera_mockFrontend,
  iotera_mockHistory,
  iotera_mockIcons,
  iotera_mockLovelace,
  iotera_mockMediaPlayer,
  iotera_mockPersistentNotification,
  iotera_mockRecorder,
  iotera_mockSensor,
  iotera_mockSystemLog,
  iotera_mockTemplate,
  iotera_mockTodo,
  iotera_mockTranslations,
} from "./iotera/mock";

import { IoteraConnection } from "./iotera/iotera";

@customElement("ha-demo")
export class HaDemo extends HomeAssistantAppEl {
  protected async _initializeHass() {
    const initial: Partial<MockHomeAssistant> = {
      panelUrl: (this as any)._panelUrl,
      // Override updateHass so that the correct hass lifecycle methods are called
      updateHass: (hassUpdate: Partial<HomeAssistant>) =>
        this._updateHass(hassUpdate),
    };

    const hass = (this.hass = provideHass(this, initial));
    const localizePromise =
      // @ts-ignore
      this._loadFragmentTranslations(hass.language, "page-demo").then(
        () => this.hass!.localize
      );

    mockLovelace(hass, localizePromise);
    mockAuth(hass);
    mockTranslations(hass);
    mockHistory(hass);
    mockRecorder(hass);
    mockTodo(hass);
    mockSensor(hass);
    mockSystemLog(hass);
    mockTemplate(hass);
    mockEvents(hass);
    mockMediaPlayer(hass);
    mockFrontend(hass);
    mockIcons(hass);
    mockEnergy(hass);
    mockPersistentNotification(hass);
    mockConfigEntries(hass);
    mockAreaRegistry(hass);
    mockEntityRegistry(hass, [
      {
        config_entry_id: "co2signal",
        device_id: "co2signal",
        area_id: null,
        disabled_by: null,
        entity_id: "sensor.co2_intensity",
        id: "sensor.co2_intensity",
        name: null,
        icon: null,
        labels: [],
        categories: {},
        platform: "co2signal",
        hidden_by: null,
        entity_category: null,
        has_entity_name: false,
        unique_id: "co2_intensity",
        options: null,
        created_at: 0,
        modified_at: 0,
      },
      {
        config_entry_id: "co2signal",
        device_id: "co2signal",
        area_id: null,
        disabled_by: null,
        entity_id: "sensor.grid_fossil_fuel_percentage",
        id: "sensor.co2_intensity",
        name: null,
        icon: null,
        labels: [],
        categories: {},
        platform: "co2signal",
        hidden_by: null,
        entity_category: null,
        has_entity_name: false,
        unique_id: "grid_fossil_fuel_percentage",
        options: null,
        created_at: 0,
        modified_at: 0,
      },
    ]);

    // iotera mock API
    const iotera_connection = IoteraConnection.get_instance();
    iotera_mockLovelace(iotera_connection, hass);
    iotera_mockAuth(iotera_connection, hass);
    iotera_mockTranslations(iotera_connection, hass);
    iotera_mockHistory(iotera_connection, hass);
    iotera_mockRecorder(iotera_connection, hass);
    iotera_mockTodo(iotera_connection, hass);
    iotera_mockSensor(iotera_connection, hass);
    iotera_mockSystemLog(iotera_connection, hass);
    iotera_mockTemplate(iotera_connection, hass);
    iotera_mockEvents(iotera_connection, hass);
    iotera_mockMediaPlayer(iotera_connection, hass);
    iotera_mockFrontend(iotera_connection, hass);
    iotera_mockIcons(iotera_connection, hass);
    iotera_mockEnergy(iotera_connection, hass);
    iotera_mockPersistentNotification(iotera_connection, hass);
    iotera_mockConfigEntries(iotera_connection, hass);
    iotera_mockAreaRegistry(iotera_connection, hass);
    iotera_mockEntityRegistry(iotera_connection, hass, [
      {
        config_entry_id: "co2signal",
        device_id: "co2signal",
        area_id: null,
        disabled_by: null,
        entity_id: "sensor.co2_intensity",
        id: "sensor.co2_intensity",
        name: null,
        icon: null,
        labels: [],
        categories: {},
        platform: "co2signal",
        hidden_by: null,
        entity_category: null,
        has_entity_name: false,
        unique_id: "co2_intensity",
        options: null,
        created_at: 0,
        modified_at: 0,
      },
      {
        config_entry_id: "co2signal",
        device_id: "co2signal",
        area_id: null,
        disabled_by: null,
        entity_id: "sensor.grid_fossil_fuel_percentage",
        id: "sensor.co2_intensity",
        name: null,
        icon: null,
        labels: [],
        categories: {},
        platform: "co2signal",
        hidden_by: null,
        entity_category: null,
        has_entity_name: false,
        unique_id: "grid_fossil_fuel_percentage",
        options: null,
        created_at: 0,
        modified_at: 0,
      },
    ]);

    const _energyEntities = energyEntities();
    console.log("_initializeHass : " + JSON.stringify(_energyEntities));

    hass.addEntities(_energyEntities);

    // Once config is loaded AND localize, set entities and apply theme.
    Promise.all([selectedDemoConfig, localizePromise]).then(
      ([conf, localize]) => {
        hass.addEntities(conf.entities(localize));
        if (conf.theme) {
          hass.mockTheme(conf.theme());
        }
      }
    );

    // Taken from polymer/pwa-helpers. BSD-3 licensed
    document.body.addEventListener(
      "click",
      (e) => {
        const href = isNavigationClick(e);

        if (!href) {
          return;
        }

        e.preventDefault();
        navigate(href);
      },
      { capture: true }
    );

    (this as any).hassConnected();
  }
}

declare global {
  interface HTMLElementTagNameMap {
    "ha-demo": HaDemo;
  }
}
