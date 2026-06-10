import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

class IrrigationFlow(config_entries.ConfigFlow, domain=DOMAIN):

    VERSION = 1

    async def async_step_user(self, user_input=None):

        if user_input is not None:
            return self.async_create_entry(title="Irrigation", data=user_input)

        schema = vol.Schema({
            vol.Required("pump1_switch"): str,
            vol.Required("pump1_flow"): int,

            vol.Required("pump2_switch"): str,
            vol.Required("pump2_flow"): int,

            vol.Required("pump3_switch"): str,
            vol.Required("pump3_flow"): int,
        })

        return self.async_show_form(step_id="user", data_schema=schema)
