import asyncio
from homeassistant.components.button import ButtonEntity

class IrrigationButton(ButtonEntity):

    def __init__(self, hass, switch_entity, number_entity):
        self.hass = hass
        self.switch_entity = switch_entity
        self.number_entity = number_entity

        self._attr_name = f"Arroser"

    async def async_press(self):

        duration = self.number_entity.native_value

        await self.hass.services.async_call(
            "switch",
            "turn_on",
            {"entity_id": self.switch_entity},
            blocking=True,
        )

        await asyncio.sleep(duration)

        await self.hass.services.async_call(
            "switch",
            "turn_off",
            {"entity_id": self.switch_entity},
            blocking=True,
        )
