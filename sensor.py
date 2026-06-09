from homeassistant.components.sensor import SensorEntity

class IrrigationVolumeSensor(SensorEntity):

    def __init__(self, name, duration_entity, flow_rate):
        self._name = f"{name} volume"
        self._duration_entity = duration_entity
        self._flow_rate = flow_rate

    @property
    def native_value(self):
        duration = self._duration_entity.native_value
        return round(self._flow_rate * duration / 60)

    @property
    def native_unit_of_measurement(self):
        return "ml"
