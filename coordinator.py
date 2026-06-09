class IrrigationCoordinator:
    def __init__(self, hass, config):
        self.hass = hass
        self.config = config

        self.durations = {
            1: 30,
            2: 30,
            3: 30,
        }
