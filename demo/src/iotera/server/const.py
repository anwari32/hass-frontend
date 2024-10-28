import datetime

""" some constants """
null = None

""" some function """
def localize(someinput):
    """ function from frontend implementation. TODO: figure this one out later. """

    return someinput

lovelace = ""
auth = ""
translation = ""
history = ""
recorder = ""
todo = ""
sensor = ""
system_log = ""
template = ""
event = ""
mediaplayer = ""
frontend = ""
icon = ""
energy = ""
persistent_notification = ""
config_entry = ""
area_registry = ""
entity_registry = ""


numeric_device_classes = [
    {
      "numeric_device_classes": [
        # "volume_storage",
        # "gas",
        # "data_size",
        # "irradiance",
        # "wind_speed",
        # "volatile_organic_compounds",
        # "volatile_organic_compounds_parts",
        # "voltage",
        # "frequency",
        # "precipitation_intensity",
        # "volume",
        # "precipitation",
        # "battery",
        # "nitrogen_dioxide",
        # "speed",
        # "signal_strength",
        # "pm1",
        # "nitrous_oxide",
        # "atmospheric_pressure",
        # "data_rate",
        # "temperature",
        # "power_factor",
        # "aqi",
        # "current",
        # "volume_flow_rate",
        # "humidity",
        # "duration",
        # "ozone",
        # "distance",
        # "pressure",
        # "pm25",
        # "weight",
        # "energy",
        # "carbon_monoxide",
        # "apparent_power",
        # "illuminance",
        # "energy_storage",
        # "moisture",
        # "power",
        # "water",
        # "carbon_dioxide",
        # "ph",
        # "reactive_power",
        # "monetary",
        # "nitrogen_monoxide",
        # "pm10",
        # "sound_pressure",
        # "sulphur_dioxide",
        "x_uranium_radiation",
        "x_plutonium_radiation"
      ],
  }
]

map_entities = {
    "zone.home": {
      "entity_id": "zone.home",
      "state": "zoning",
      "attributes": {
        "hidden": True,
        "latitude": -6.1944,
        "longitude": 106.8229,
        "radius": 200,
        "friendly_name": "Home",
        "icon": "hademo:home",
      },
    },
    "zone.workplace": {
      "entity_id": "zone.buckhead",
      "state": "zoning",
      "attributes": {
        "hidden": True,
        "radius": 400,
        "friendly_name": "Basecamp IOTERA",
        "icon": "hademo:school",
        "latitude": -6.8995,
        "longitude": 107.6158,
      },
    },
    "person.arsaboo": {
      "entity_id": "person.arsaboo",
      "state": "not_home",
      "attributes": {
        "radius": 50,
        "friendly_name": "Arsaboo",
        "latitude": 52.3579946,
        "longitude": 4.8664597,
        "entity_picture": "/assets/arsaboo/images/arsaboo.jpg",
      },
    },
    "person.melody": {
      "entity_id": "person.melody",
      "state": "not_home",
      "attributes": {
        "radius": 50,
        "friendly_name": "Melody",
        "latitude": 52.3408927,
        "longitude": 4.8711073,
        "entity_picture": "/assets/arsaboo/images/melody.jpg",
      },
    },
  }

energy_entities = {
    "sensor.solar_production": {
      "entity_id": "sensor.solar_production",
      "state": "88.6",
      "attributes": {
        "last_reset": "2024-02-03T00:00:00:00+00",
        "friendly_name": "Sel Surya Rumahan",
        "unit_of_measurement": "kWh",
      },
    },
    "sensor.battery_input": {
      "entity_id": "sensor.battery_input",
      "state": "4",
      "attributes": {
        "last_reset": "2024-02-03T00:00:00:00+00",
        "friendly_name": "Masukan Data Baterai",
        "unit_of_measurement": "kWh ^_^",
      },
    },
    "sensor.battery_output": {
      "entity_id": "sensor.battery_output",
      "state": "3",
      "attributes": {
        "last_reset": "2024-02-03T00:00:00:00+00",
        "friendly_name": "Daya Keluaran Baterai",
        "unit_of_measurement": "kWh",
      },
    },

    "sensor.energy_consumption_tarif_1_cost": {
      "entity_id": "sensor.energy_consumption_tarif_1_cost",
      "state": "2",
      "attributes": {
        "last_reset": "2024-02-03T00:00:00:00+00",
        "unit_of_measurement": "IDR",
      },
    },
    "sensor.energy_consumption_tarif_2_cost": {
      "entity_id": "sensor.energy_consumption_tarif_2_cost",
      "state": "2",
      "attributes": {
        "last_reset": "2024-02-03T00:00:00:00+00",
        "unit_of_measurement": "IDR",
      },
    },
    "sensor.energy_production_tarif_1_compensation": {
      "entity_id": "sensor.energy_production_tarif_1_compensation",
      "state": "2",
      "attributes": {
        "last_reset": "2024-02-03T00:00:00:00+00",
        "unit_of_measurement": "IDR",
      },
    },
    "sensor.energy_production_tarif_2_compensation": {
      "entity_id": "sensor.energy_production_tarif_2_compensation",
      "state": "2",
      "attributes": {
        "last_reset": "2024-02-03T00:00:00:00+00",
        "unit_of_measurement": "IDR",
      },
    },
    "sensor.energy_gas_cost": {
      "entity_id": "sensor.energy_gas_cost",
      "state": "2",
      "attributes": {
        "last_reset": "2024-02-03T00:00:00:00+00",
        "unit_of_measurement": "IDR",
      },
    },
    "sensor.energy_gas": {
      "entity_id": "sensor.energy_gas",
      "state": "4",
      "attributes": {
        "last_reset": "2024-02-03T00:00:00:00+00",
        "friendly_name": "Gas LNG",
        "unit_of_measurement": "m cubic",
      },
    },
    "sensor.energy_car": {
      "entity_id": "sensor.energy_car",
      "state": "4",
      "attributes": {
        "last_reset": "2024-02-03T00:00:00:00+00",
        "friendly_name": "Mobil Listrik Esemka",
        "unit_of_measurement": "kWh",
      },
    },
    "sensor.energy_ac": {
      "entity_id": "sensor.energy_ac",
      "state": "3",
      "attributes": {
        "last_reset": "2024-02-03T00:00:00:00+00",
        "friendly_name": "AC Sharp",
        "unit_of_measurement": "kWh",
      },
    },
    "sensor.energy_washing_machine": {
      "entity_id": "sensor.energy_washing_machine",
      "state": "6",
      "attributes": {
        "last_reset": "2024-02-03T00:00:00:00+00",
        "friendly_name": "Mesin Cuci Samsung",
        "unit_of_measurement": "kWh",
      },
    },
    "sensor.energy_dryer": {
      "entity_id": "sensor.energy_dryer",
      "state": "5.5",
      "attributes": {
        "last_reset": "2024-02-03T00:00:00:00+00",
        "friendly_name": "Hair Dryer Philips",
        "unit_of_measurement": "kWh",
      },
    },
    "sensor.energy_heat_pump": {
      "entity_id": "sensor.energy_heat_pump",
      "state": "6",
      "attributes": {
        "last_reset": "2024-02-03T00:00:00:00+00",
        "friendly_name": "Penghangat Ruangan Xiaomi",
        "unit_of_measurement": "kWh",
      },
    },
    "sensor.energy_boiler": {
      "entity_id": "sensor.energy_boiler",
      "state": "7",
      "attributes": {
        "last_reset": "2024-02-03T00:00:00:00+00",
        "friendly_name": "Pemanas Air (Water Boiler)",
        "unit_of_measurement": "kWh",
      },
    },
  }

energy_prefs = {
    "energy_sources": [
        {
          "type": "grid",
          "flow_from": [
            {
              "stat_energy_from": "sensor.energy_consumption_tarif_1",
              "stat_cost": "sensor.energy_consumption_tarif_1_cost",
              "entity_energy_price": None,
              "number_energy_price": None,
            },
            {
              "stat_energy_from": "sensor.energy_consumption_tarif_2",
              "stat_cost": "sensor.energy_consumption_tarif_2_cost",
              "entity_energy_price": None,
              "number_energy_price": None,
            },
          ],
          "flow_to": [
            {
              "stat_energy_to": "sensor.energy_production_tarif_1",
              "stat_compensation": "sensor.energy_production_tarif_1_compensation",
              "entity_energy_price": None,
              "number_energy_price": None,
            },
            {
              "stat_energy_to": "sensor.energy_production_tarif_2",
              "stat_compensation": "sensor.energy_production_tarif_2_compensation",
              "entity_energy_price": None,
              "number_energy_price": None,
            },
          ],
          "cost_adjustment_day": 0,
        },
        {
          "type": "solar",
          "stat_energy_from": "sensor.solar_production",
          "config_entry_solar_forecast": ["solar_forecast"],
        },
        {
          "type": "gas",
          "stat_energy_from": "sensor.energy_gas",
          "stat_cost": "sensor.energy_gas_cost",
          "entity_energy_price": None,
          "number_energy_price": None,
        },
      ],
      "device_consumption": [
        {
          "stat_consumption": "sensor.energy_car",
        },
        {
          "stat_consumption": "sensor.energy_ac",
        },
        {
          "stat_consumption": "sensor.energy_washing_machine",
        },
        {
          "stat_consumption": "sensor.energy_dryer",
        },
        {
          "stat_consumption": "sensor.energy_heat_pump",
        },
        {
          "stat_consumption": "sensor.energy_boiler",
        },
      ],
}

energy_info = { 
    "cost_sensors": {}, 
    "solar_forecast_domains": [] 
    }

energy_fossil_fuel_consumption = {
      "start": 250,
    }

energy_solar_forecast = {
      "solar_forecast": {
        "wh_hours": {
          1: 0,
          2: 6,
          3: 39,
          4: 28,
          5: 208,
          6: 352,
          7: 544,
          8: 748,
          9: 1259,
          10: 1361,
          11: 1373,
          12: 1370,
          13: 1186,
          14: 937,
          15: 652,
          16: 370,
          17: 155,
          18: 24,
          19: 0,
          # [`${tomorrowString}T06:01:00`]: 0,
        },
      },
    }

energy = {
    "get_prefs": energy_prefs,
    "info": energy_info,
    "fossil_energy_consumption": energy_fossil_fuel_consumption,
    "solar_forecast": energy_solar_forecast,
    "entity": energy_entities,
}

entity_items = {
    {
    "cover.living_room_garden_shutter": {
      "entity_id": "cover.living_room_garden_shutter",
      "state": "open",
      "attributes": {
        "current_position": 100,
        "device_class": "shutter",
        "friendly_name": "IOTERA Living room garden shutter",
        "supported_features": 15,
      },
    },
    "cover.living_room_graveyard_shutter": {
      "entity_id": "cover.living_room_graveyard_shutter",
      "state": "open",
      "attributes": {
        "current_position": 100,
        "device_class": "shutter",
        "friendly_name": "IOTERA Living room graveyard shutter",
        "supported_features": 15,
      },
    },
    "cover.living_room_left_shutter": {
      "entity_id": "cover.living_room_left_shutter",
      "state": "open",
      "attributes": {
        "current_position": 100,
        "device_class": "shutter",
        "friendly_name": "Living room left shutter",
        "supported_features": 15,
      },
    },
    "cover.living_room_right_shutter": {
      "entity_id": "cover.living_room_right_shutter",
      "state": "open",
      "attributes": {
        "current_position": 100,
        "device_class": "shutter",
        "friendly_name": "Living room right shutter",
        "supported_features": 15,
      },
    },
    "light.floor_lamp": {
      "entity_id": "light.floor_lamp",
      "state": "on",
      "attributes": {
        "min_color_temp_kelvin": 2000,
        "max_color_temp_kelvin": 6535,
        "min_mireds": 153,
        "max_mireds": 500,
        "supported_color_modes": ["color_temp", "xy"],
        "color_mode": "color_temp",
        "brightness": 178,
        "color_temp_kelvin": 2583,
        "color_temp": 387,
        "hs_color": [28.664, 69.597],
        "rgb_color": [255, 162, 77],
        "xy_color": [0.538, 0.389],
        "icon": "mdi:floor-lamp",
        "friendly_name": "Floor lamp",
        "supported_features": 44,
      },
    },
    "light.living_room_spotlights": {
      "entity_id": "light.living_room_spotlights",
      "state": "on",
      "attributes": {
        "supported_color_modes": ["brightness"],
        "color_mode": "brightness",
        "brightness": 126,
        "icon": "mdi:ceiling-light-multiple",
        "friendly_name": "Living room spotlights",
        "supported_features": 32,
      },
    },
    "light.bar_lamp": {
      "entity_id": "light.bar_lamp",
      "state": "on",
      "attributes": {
        "min_color_temp_kelvin": 2202,
        "max_color_temp_kelvin": 4504,
        "min_mireds": 222,
        "max_mireds": 454,
        "effect_list": ["None", "candle"],
        "supported_color_modes": ["color_temp"],
        "effect": null,
        "color_mode": null,
        "brightness": null,
        "color_temp_kelvin": null,
        "color_temp": null,
        "hs_color": null,
        "rgb_color": null,
        "xy_color": null,
        "mode": "normal",
        "dynamics": "none",
        "icon": "mdi:lightbulb-variant",
        "friendly_name": "Bar lamp",
        "supported_features": 44,
      },
    },
    "sensor.living_room_temperature": {
      "entity_id": "sensor.living_room_temperature",
      "state": "22.8",
      "attributes": {
        "state_class": "measurement",
        "unit_of_measurement": "°C",
        "device_class": "temperature",
        "friendly_name": "IOTERA Living room Temperature",
      },
    },
    "media_player.living_room_nest_mini": {
      "entity_id": "media_player.living_room_nest_mini",
      "state": "on",
      "attributes": {
        "device_class": "speaker",
        "volume_level": 0.18,
        "is_volume_muted": False,
        "media_content_type": "music",
        "media_duration": 300,
        "media_position": 0,
        "media_position_updated_at": (datetime.datetime.now() - datetime.timedelta(23000)).isoformat(),
        "media_title": "I Wasn't Born To Follow",
        "media_artist": "The Byrds",
        "media_album_name": "The Notorious Byrd Brothers",
        "source_list": ["It's A Party", "Radio HSL", "Retro 70s and 80s"],
        "shuffle": False,
        "night_sound": False,
        "speech_enhance": False,
        "friendly_name": localize(
          "ui.panel.page-demo.config.sections.entities.media_player.living_room_nest_mini"
        ),
        "entity_picture": "/assets/sections/images/media_player_family_room.jpg",
        "supported_features": 64063,
      },
    },
    "cover.kitchen_shutter": {
      "entity_id": "cover.kitchen_shutter",
      "state": "open",
      "attributes": {
        "current_position": 100,
        "device_class": "shutter",
        "friendly_name": "Kitchen shutter ",
        "supported_features": 15,
      },
    },
    "light.kitchen_spotlights": {
      "entity_id": "light.kitchen_spotlights",
      "state": "off",
      "attributes": {
        "supported_color_modes": ["brightness"],
        "color_mode": null,
        "brightness": null,
        "icon": "mdi:ceiling-light-multiple",
        "friendly_name": "Kitchen spotlights ",
        "supported_features": 32,
      },
    },
    "light.worktop_spotlights": {
      "entity_id": "light.worktop_spotlights",
      "state": "off",
      "attributes": {
        "supported_color_modes": ["brightness"],
        "color_mode": null,
        "brightness": null,
        "icon": "mdi:ceiling-light-multiple",
        "friendly_name": "Worktop spotlights ",
        "supported_features": 32,
      },
    },
    "binary_sensor.fridge_door": {
      "entity_id": "binary_sensor.fridge_door",
      "state": "off",
      "attributes": {
        "device_class": "door",
        "icon": "mdi:fridge",
        "friendly_name": "Fridge door",
      },
    },
    "media_player.kitchen_nest_audio": {
      "entity_id": "media_player.kitchen_nest_audio",
      "state": "on",
      "attributes": {
        "device_class": "speaker",
        "volume_level": 0.18,
        "is_volume_muted": False,
        "media_content_type": "music",
        "media_duration": 300,
        "media_position": 0,
        "media_position_updated_at": (datetime.datetime.now() - datetime.timedelta(23000)).isoformat(),
        "media_title": "I Wasn't Born To Follow",
        "media_artist": "The Byrds",
        "media_album_name": "The Notorious Byrd Brothers",
        "source_list": ["It's A Party", "Radio HSL", "Retro 70s and 80s"],
        "shuffle": False,
        "night_sound": False,
        "speech_enhance": False,
        "friendly_name": localize(
          "ui.panel.page-demo.config.sections.entities.media_player.kitchen_nest_audio"
        ),
        "entity_picture": "/assets/sections/images/media_player_family_room.jpg",
        "supported_features": 64063,
      },
    },
    "binary_sensor.tesla_wall_connector_vehicle_connected": {
      "entity_id": "binary_sensor.tesla_wall_connector_vehicle_connected",
      "state": "off",
      "attributes": {
        "device_class": "plug",
        "friendly_name": "Wall Connector Vehicle connected",
      },
    },
    "sensor.tesla_wall_connector_session_energy": {
      "entity_id": "sensor.tesla_wall_connector_session_energy",
      "state": "16.3",
      "attributes": {
        "state_class": "total_increasing",
        "unit_of_measurement": "kWh",
        "device_class": "energy",
        "friendly_name": "Tesla Wall Connector Session energy",
      },
    },
    "sensor.electric_meter_power": {
      "entity_id": "sensor.electric_meter_power",
      "state": "797.86",
      "attributes": {
        "state_class": "measurement",
        "unit_of_measurement": "W",
        "device_class": "power",
        "icon": "mdi:meter-electric",
        "friendly_name": "Electric meter Power",
      },
    },
    "sensor.eletric_meter_voltage": {
      "entity_id": "sensor.eletric_meter_voltage",
      "state": "232.19",
      "attributes": {
        "state_class": "measurement",
        "unit_of_measurement": "V",
        "device_class": "voltage",
        "friendly_name": "Electric meter voltage",
      },
    },
    "sensor.electricity_maps_grid_fossil_fuel_percentage": {
      "entity_id": "sensor.electricity_maps_grid_fossil_fuel_percentage",
      "state": "9.84",
      "attributes": {
        "state_class": "measurement",
        "country_code": "FR",
        "unit_of_measurement": "%",
        "attribution": "Data provided by Electricity Maps",
        "icon": "mdi:barrel",
        "friendly_name": "Electricity Maps Grid fossil fuel percentage",
      },
    },
    "sensor.electricity_maps_co2_intensity": {
      "entity_id": "sensor.electricity_maps_co2_intensity",
      "state": "62.0",
      "attributes": {
        "state_class": "measurement",
        "country_code": "FR",
        "unit_of_measurement": "gCO2eq/kWh",
        "attribution": "Data provided by Electricity Maps",
        "friendly_name": "Electricity Maps CO2 intensity",
        "icon": "mdi:molecule-co2",
      },
    },
    "sun.sun": {
      "entity_id": "sun.sun",
      "state": "above_horizon",
      "attributes": {
        "next_dawn": "2024-03-05T05:50:21.964405+00:00",
        "next_dusk": "2024-03-04T18:08:54.311334+00:00",
        "next_midnight": "2024-03-05T00:00:00+00:00",
        "next_noon": "2024-03-05T12:00:05+00:00",
        "next_rising": "2024-03-05T06:23:42.739159+00:00",
        "next_setting": "2024-03-04T17:35:26.271171+00:00",
        "elevation": 30.38,
        "azimuth": 204.42,
        "rising": False,
        "friendly_name": "Sun",
      },
    },
    "sensor.rain": {
      "entity_id": "sensor.moon_phase",
      "state": "7.2",
      "attributes": {
        "state_class": "total_increasing",
        "unit_of_measurement": "mm",
        "device_class": "precipitation",
        "friendly_name": "Rain",
      },
    },
    "climate.ground_floor": {
      "entity_id": "climate.ground_floor",
      "state": "heat",
      "attributes": {
        "hvac_modes": ["auto", "heat", "off"],
        "min_temp": 7,
        "max_temp": 35,
        "preset_modes": [
          "comfort",
          "away",
          "eco",
          "frost_protection",
          "external",
          "home",
        ],
        "current_temperature": 20.8,
        "temperature": 21,
        "preset_mode": "comfort",
        "icon": "mdi:home-floor-0",
        "friendly_name": "Ground floor Thermostat",
        "supported_features": 401,
      },
    },
    "climate.first_floor": {
      "entity_id": "climate.first_floor",
      "state": "heat",
      "attributes": {
        "hvac_modes": ["auto", "heat", "off"],
        "min_temp": 7,
        "max_temp": 35,
        "preset_modes": [
          "comfort",
          "away",
          "eco",
          "frost_protection",
          "external",
          "home",
        ],
        "current_temperature": 21.7,
        "temperature": 21,
        "preset_mode": "comfort",
        "icon": "mdi:home-floor-1",
        "friendly_name": "First floor Thermostat",
        "supported_features": 401,
      },
    },
    "cover.study_shutter": {
      "entity_id": "cover.study_shutter",
      "state": "open",
      "attributes": {
        "current_position": 100,
        "device_class": "shutter",
        "friendly_name": "Study shutter",
        "supported_features": 15,
      },
    },
    "light.study_spotlights": {
      "entity_id": "light.study_spotlights",
      "state": "off",
      "attributes": {
        "supported_color_modes": ["brightness"],
        "color_mode": null,
        "brightness": null,
        "icon": "mdi:ceiling-light-multiple",
        "friendly_name": "Study spotlights",
        "supported_features": 32,
      },
    },
    "media_player.study_nest_hub": {
      "entity_id": "media_player.study_nest_hub",
      "state": "off",
      "attributes": {
        "device_class": "speaker",
        "volume_level": 0.18,
        "is_volume_muted": False,
        "media_content_type": "music",
        "media_duration": 300,
        "media_position": 0,
        "media_position_updated_at": (datetime.datetime.now() - datetime.timedelta(23000)).isoformat(),
        "media_title": "I Wasn't Born To Follow",
        "media_artist": "The Byrds",
        "media_album_name": "The Notorious Byrd Brothers",
        "source_list": ["It's A Party", "Radio HSL", "Retro 70s and 80s"],
        "shuffle": False,
        "night_sound": False,
        "speech_enhance": False,
        "friendly_name": localize(
          "ui.panel.page-demo.config.sections.entities.media_player.study_nest_hub"
        ),
        "entity_picture": "/assets/sections/images/media_player_family_room.jpg",
        "supported_features": 64063,
      },
    },
    "sensor.standing_desk_height": {
      "entity_id": "sensor.standing_desk_height",
      "state": "72",
      "attributes": {
        "unit_of_measurement": "cm",
        icon: "mdi:tape-measure",
        "friendly_name": "Standing desk Height",
      },
    },
    "light.outdoor_light": {
      "entity_id": "light.outdoor_light",
      "state": "on",
      "attributes": {
        "supported_color_modes": ["brightness"],
        "color_mode": null,
        "brightness": 255,
        icon: "mdi:outdoor-lamp",
        "friendly_name": "Outdoor light",
        "supported_features": 32,
      },
    },
    "light.flood_light": {
      "entity_id": "light.flood_light",
      "state": "off",
      "attributes": {
        "effect_list": ["None", "candle"],
        "supported_color_modes": ["brightness"],
        "effect": null,
        "color_mode": null,
        "brightness": null,
        "mode": "normal",
        "dynamics": "none",
        icon: "mdi:light-flood-down",
        "friendly_name": "Flood light",
        "supported_features": 44,
      },
    },
    "sensor.outdoor_motion_sensor_temperature": {
      "entity_id": "sensor.outdoor_motion_sensor_temperature",
      "state": "10.2",
      "attributes": {
        "state_class": "measurement",
        "unit_of_measurement": "°C",
        "device_class": "temperature",
        "friendly_name": "Outdoor motion sensor Temperature",
      },
    },
    "binary_sensor.outdoor_motion_sensor_motion": {
      "entity_id": "binary_sensor.outdoor_motion_sensor_motion",
      "state": "off",
      "attributes": {
        "device_class": "motion",
        "friendly_name": "Outdoor motion sensor Motion",
      },
    },
    "sensor.outdoor_motion_sensor_illuminance": {
      "entity_id": "sensor.outdoor_motion_sensor_illuminance",
      "state": "555",
      "attributes": {
        "state_class": "measurement",
        "light_level": 27444,
        "unit_of_measurement": "lx",
        "device_class": "illuminance",
        "friendly_name": "Outdoor motion sensor Illuminance",
      },
    },
    "automation.home_assistant_auto_update": {
      "entity_id": "automation.home_assistant_auto_update",
      "state": "off",
      "attributes": {
        id: "1700669321947",
        "last_triggered": "2024-02-29T18:02:05.343139+00:00",
        "mode": "queued",
        "current": 0,
        max: 50,
        icon: "mdi:auto-mode",
        "friendly_name": "Home Assistant Auto-update",
      },
    },
    "update.home_assistant_operating_system_update": {
      "entity_id": "update.home_assistant_operating_system_update",
      "state": "off",
      "attributes": {
        "auto_update": False,
        "installed_version": "12.1",
        "in_progress": False,
        "latest_version": "12.1",
        "release_summary": null,
        "release_url":
          "https://github.com/home-assistant/operating-system/commits/dev",
        "skipped_version": null,
        "title": "Home Assistant Operating System",
        "entity_picture":
          "https://brands.home-assistant.io/homeassistant/icon.png",
        "friendly_name": "Home Assistant Operating System Update",
        "supported_features": 3,
      },
    },
    "update.home_assistant_supervisor_update": {
      "entity_id": "update.home_assistant_supervisor_update",
      "state": "off",
      "attributes": {
        "auto_update": True,
        "installed_version": "2024.02.2",
        "in_progress": False,
        "latest_version": "2024.02.2",
        "release_summary": null,
        "release_url":
          "https://github.com/home-assistant/supervisor/commits/main",
        "skipped_version": null,
        "title": "Home Assistant Supervisor",
        "entity_picture": "https://brands.home-assistant.io/hassio/icon.png",
        "friendly_name": "Home Assistant Supervisor Update",
        "supported_features": 1,
      },
    },
    "update.home_assistant_core_update": {
      "entity_id": "update.home_assistant_supervisor_update",
      "state": "off",
      "attributes": {
        "auto_update": False,
        "installed_version": "2024.4.0",
        "in_progress": False,
        "latest_version": "2024.4.0",
        "release_summary": null,
        "release_url": "https://github.com/home-assistant/core/commits/dev",
        "skipped_version": null,
        "title": "Home Assistant Core",
        "entity_picture":
          "https://brands.home-assistant.io/homeassistant/icon.png",
        "friendly_name": "Home Assistant Core Update",
        "supported_features": 11,
      },
    },
  }
}

entity = {
    "registry": entity_registry,
    "entity": entity_items,
}

area = {
    "registry": area_registry
}

consts = {
    "lovelace" : lovelace,
    "auth" : auth,
    "translation" : translation,
    "history" : history,
    "recorder" : recorder,
    "todo" : todo,
    "sensor" : sensor,
    "system_log" : system_log,
    "template" : template,
    "event" : event,
    "mediaplayer" : mediaplayer,
    "frontend" : frontend,
    "icon" : icon,
    "energy" : energy,
    "persistent_notification" : persistent_notification,
    "config_entry" : config_entry,
    "area" : area,
    "entity" : entity,
}

