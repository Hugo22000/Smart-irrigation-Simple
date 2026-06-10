class IrrigationCoordinator:

    def __init__(self, hass, config):
        self.hass = hass
        self.config = config

    def get_flow(self, pump):
        return self.config.get(f"pump{pump}_flow", 100)

    def get_switch(self, pump):
        return self.config.get(f"pump{pump}_switch")
