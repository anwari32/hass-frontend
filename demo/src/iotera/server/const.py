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

entity = {
    "registry": entity_registry
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

