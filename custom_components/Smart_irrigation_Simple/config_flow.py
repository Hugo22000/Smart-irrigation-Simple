"""Config flow for Smart Irrigation Simple integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import selector

from .const import (
    DOMAIN,
    SIS_PUMP1_SWITCH,
    SIS_PUMP1_FLOW,
    SIS_PUMP2_SWITCH,
    SIS_PUMP2_FLOW,
    SIS_PUMP3_SWITCH,
    SIS_PUMP3_FLOW,
)

_LOGGER = logging.getLogger(__name__)


async def validate_pump_config(
    hass: HomeAssistant, user_input: dict[str, Any]
) -> dict[str, Any]:
    """Validate that the switch entities exist in Home Assistant."""
    for pump_key in [SIS_PUMP1_SWITCH, SIS_PUMP2_SWITCH, SIS_PUMP3_SWITCH]:
        switch_entity = user_input.get(pump_key)
        if switch_entity and not hass.states.get(switch_entity):
            raise InvalidPumpError(f"Entity {switch_entity} does not exist")
    return user_input


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Smart Irrigation Simple."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step for user configuration."""
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                validated_input = await validate_pump_config(self.hass, user_input)
                return self.async_create_entry(
                    title="Smart Irrigation Simple",
                    data=validated_input,
                )
            except InvalidPumpError as e:
                errors["base"] = "invalid_pump"
                _LOGGER.error("Invalid pump configuration: %s", e)
            except Exception as e:
                _LOGGER.exception("Unexpected error during config flow")
                errors["base"] = "unknown"

        schema = vol.Schema(
            {
                vol.Required(SIS_PUMP1_SWITCH): selector.EntitySelector(
                    selector.EntitySelectorConfig(domain="switch")
                ),
                vol.Required(
                    SIS_PUMP1_FLOW, default=120
                ): selector.NumberSelector(
                    selector.NumberSelectorConfig(
                        min=1, max=1000, step=1, unit_of_measurement="ml/min"
                    )
                ),
                vol.Required(SIS_PUMP2_SWITCH): selector.EntitySelector(
                    selector.EntitySelectorConfig(domain="switch")
                ),
                vol.Required(
                    SIS_PUMP2_FLOW, default=120
                ): selector.NumberSelector(
                    selector.NumberSelectorConfig(
                        min=1, max=1000, step=1, unit_of_measurement="ml/min"
                    )
                ),
                vol.Required(SIS_PUMP3_SWITCH): selector.EntitySelector(
                    selector.EntitySelectorConfig(domain="switch")
                ),
                vol.Required(
                    SIS_PUMP3_FLOW, default=120
                ): selector.NumberSelector(
                    selector.NumberSelectorConfig(
                        min=1, max=1000, step=1, unit_of_measurement="ml/min"
                    )
                ),
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )


class InvalidPumpError(HomeAssistantError):
    """Error raised when a pump entity is invalid."""