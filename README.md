# Smart Irrigation Simple
Homeassistant integration

Integration Home Assistant pour gestion simplifiée d'arrosage :

- 3 pompes
- durée 5–180 secondes
- calcul automatique du volume
- arrosage manuel

## Installation

Via HACS → Custom repository

## Configuration

Ajoutez vos pompes et débits via l'interface Home Assistant.

## Structure 

```yaml
custom_components/
└── smart_irrigation_simple/
    ├── __init__.py
    ├── manifest.json
    ├── config_flow.py
    ├── number.py
    ├── sensor.py
    ├── button.py
    ├── switch.py
    ├── coordinator.py
    ├── services.yaml
    └── translations/```
