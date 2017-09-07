"""
Support for  Laser egg generation1 without homekit support

Author: OctavianX 
Date: 2017/09/01

"""

import logging
import voluptuous as vol



DEFAULT_NAME = 'LaserEgg'
DEFAULT_TIMEOUT = 0
DEFAULT_RETRY = 3


from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import ( CONF_FRIENDLY_NAME, CONF_USERNAME, CONF_PASSWORD)


import homeassistant.helpers.config_validation as cv




_LOGGER = logging.getLogger(__name__)






def setup_platform(hass, config, add_devices,descovery_info=None):
    """dev_friendlyname = config.get(CONF_FRIENDLY_NAME) """
    friendly_name = config.get(CONF_FRIENDLY_NAME)
    
    add_devices([LaserEggGen1Sensor()])



class LaserEggGen1Sensor(Entity):
    def __init__(self):
        """Initialize the sensor."""
        self._state = 23 

    @property
    def name(self):
        """Return the name of the sensor."""
        return DEFAULT_NAME
    
    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return TEMP_CELSIUS
                                                                                                        
    def update(self):
        """Fetch new state data for the sensor.This is the only method that should fetch new data for Home Assistant."""
        self._state = 23

