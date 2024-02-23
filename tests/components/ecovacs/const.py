"""Test ecovacs constants."""


from homeassistant.components.ecovacs.const import (
    CONF_CONTINENT,
    CONF_OVERRIDE_MQTT_URL,
    CONF_OVERRIDE_REST_URL,
    CONF_VERIFY_MQTT_CERTIFICATE,
)
from homeassistant.const import CONF_COUNTRY, CONF_PASSWORD, CONF_USERNAME

VALID_ENTRY_DATA_CLOUD = {
    CONF_USERNAME: "username@cloud",
    CONF_PASSWORD: "password",
    CONF_COUNTRY: "IT",
}

VALID_ENTRY_DATA_SELF_HOSTED = VALID_ENTRY_DATA_CLOUD | {
    CONF_USERNAME: "username@self-hosted",
    CONF_OVERRIDE_REST_URL: "http://localhost:8000",
    CONF_OVERRIDE_MQTT_URL: "mqtt://localhost:1883",
}

VALID_ENTRY_DATA_SELF_HOSTED_WITH_VALIDATE_CERT = VALID_ENTRY_DATA_SELF_HOSTED | {
    CONF_VERIFY_MQTT_CERTIFICATE: True,
}

IMPORT_DATA = VALID_ENTRY_DATA_CLOUD | {CONF_CONTINENT: "EU"}
