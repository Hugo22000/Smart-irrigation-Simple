from homeassistant.components.sensor import SensorEntity

class IrrigationVolumeSensor(SensorEntity):

    def __init__(self, pump_id, number_entity, flow_rate):
        self.pump_id = pump_id
        self.number_entity = number_entity
        self.flow_rate = flow_rate
        self._attr_name = f"Pompe {pump_id} volume"

    @property
    def native_value(self):
        duration = self.number_entity.native_value
        return round(self.flow_rate * duration / 60)

    @property
    def native_unit_of_measurement(self):
        return "ml"
