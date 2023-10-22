import esphome.codegen as cg
import esphome.config_validation as cv

from esphome import pins
from esphome.components import display
from esphome.const import (
    CONF_HEIGHT,
    CONF_ID,
    CONF_LAMBDA,
    CONF_WIDTH,
    CONF_CS_PIN,
    CONF_DC_PIN,
    CONF_RESET_PIN,
    CONF_NUMBER,
)

from esphome.const import __version__ as ESPHOME_VERSION

st7789_gmt130v1_ns = cg.esphome_ns.namespace("st7789_gmt130v1")

DEPENDENCIES = ["esp32"]

CONF_BACKLIGHT = "backlight"
CONF_LOAD_FONTS = "load_fonts"
CONF_LOAD_SMOOTH_FONTS = "load_smooth_fonts"
CONF_ENABLE_LIBRARY_WARNINGS = "enable_library_warnings"

ST7789_GMT130V1 = st7789_gmt130v1_ns.class_(
    "ST7789_GMT130V1", cg.PollingComponent, display.DisplayBuffer
)

CONFIG_SCHEMA = cv.All(
    display.FULL_DISPLAY_SCHEMA.extend(
        {
            cv.GenerateID(): cv.declare_id(ST7789_GMT130V1),
            cv.Optional(CONF_HEIGHT, default=240): cv.uint16_t,
            cv.Optional(CONF_WIDTH, default=240): cv.uint16_t,
            cv.Optional(CONF_BACKLIGHT, default=False): cv.boolean,
            cv.Optional(CONF_LOAD_FONTS, default=False): cv.boolean,
            cv.Optional(CONF_LOAD_SMOOTH_FONTS, default=False): cv.boolean,
            cv.Optional(CONF_ENABLE_LIBRARY_WARNINGS, default=False): cv.boolean,
            cv.Optional(CONF_RESET_PIN, default=4): pins.gpio_output_pin_schema,
            cv.Optional(CONF_DC_PIN, default=2): pins.gpio_output_pin_schema,
        }
    ).extend(cv.polling_component_schema("5s")),
)

