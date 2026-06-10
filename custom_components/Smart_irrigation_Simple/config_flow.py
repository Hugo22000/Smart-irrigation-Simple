import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN
from homeassistant.helpers import selector

class IrrigationFlow(config_entries.ConfigFlow, domain=DOMAIN):

    VERSION = 1

    async def async_step_user(self, user_input=None):

        if user_input is not None:
            return self.async_create_entry(title="Irrigation", data=user_input)

        schema = vol.Schema({
    vol.Required("SIS_pump1_switch"): selector.EntitySelector(selector.EntitySelectorConfig(domain="switch")),
    vol.Required("SIS_pump1_flow", default=120): selector.NumberSelector(selector.NumberSelectorConfig(
            min=1,max=1000,step=1,unit_of_measurement="ml/min" )),
    vol.Required("SIS_pump2_switch"): selector.EntitySelector(selector.EntitySelectorConfig( domain="switch" ) ),
    vol.Required("SIS_pump2_flow", default=120): selector.NumberSelector(selector.NumberSelectorConfig(
            min=1,  max=1000,  step=1, unit_of_measurement="ml/min"  )   ),
    vol.Required("SIS_pump3_switch"): selector.EntitySelector( selector.EntitySelectorConfig(  domain="switch"    )   ),
    vol.Required("SIS_pump3_flow", default=120): selector.NumberSelector(  selector.NumberSelectorConfig(
           min=1,   max=1000,    step=1,    unit_of_measurement="ml/min"  )   ),
})

        return self.async_show_form(step_id="user", data_schema=schema)
