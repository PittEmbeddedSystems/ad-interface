"""
Concrete interface to the MCP3008 A/D source

In addition to handling the communiction with the A/D hardware, this provides
a testing seam between the A/D and the actual hardware so that a software
alternative can be switched in.
This closely follows the interface provided by the Adafruit-MCP3008 device
"""

import Adafruit_GPIO.SPI as SPI
from Adafruit_MCP3008 import MCP3008

SPI_PORT = 0
SPI_DEVICE = 0

class AdMcp3008(object): # pylint: disable=too-few-public-methods
    """
    Implementation of the interface to the MCP3008
    """

    def __init__(self):
        """
        Initialize the MCP3008 hardware interface used by this class
        """
        self.mcp = MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


    def read_adc(self, channel):
        """
        Reads the specified channel of the A/D and returns the results.

        The result will be a single positive value between 0 and 1023
        channel must be a value in the range [0, 7]
        """
        return self.mcp.read_adc(channel)
