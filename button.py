import asyncio

from homeassistant.components.button import ButtonEntity

class IrrigationButton(ButtonEntity):

    def __init__(self, hass, switch_entity, duration_entity):
        self.hass = hass
        self._switch_entity = switch_entity
        self._duration_entity = duration_entity

    async def async_press(self):

        duration = self._duration_entity.native_value

        await self.hass.services.async_call(
            "switch",
            "turn_on",
            {"entity_id": self._switch_entity},
            blocking=True,
        )

        await asyncio.sleep(duration)

        await self.hass.services.async_call(
            "switch",
            "turn_off",
            {"entity_id": self._switch_entity},
            blocking=True,
        )
