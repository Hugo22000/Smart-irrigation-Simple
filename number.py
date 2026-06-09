from homeassistant.components.number import NumberEntity

class IrrigationDuration(NumberEntity):
    _attr_native_min_value = 5
    _attr_native_max_value = 180
    _attr_native_step = 1
    _attr_native_unit_of_measurement = "s"

    def __init__(self, name):
        self._attr_name = f"{name} durée"
        self._value = 30

    @property
    def native_value(self):
        return self._value

    async def async_set_native_value(self, value):
        self._value = value
        self.async_write_ha_state()
