"""
Concrete interface to a fake A/D source

this class implements the same interface defined in the AdMcp3008 object, but
does not actually interface with the hardware. This provides a testing seam
to allow for testing of the AD object as well as to inject test data into the
real system.
"""

from random import randrange

class AdFake(object): # pylint: disable=too-few-public-methods
    """
    Implementation of the interface to a fake A/D
    """

    def __init___(self):
        pass

    def read_adc(self, channel):
        """
        Returns a random integer in the valid range when a valid channel
        is specified.
        """
        return randrange(0, 1023, 1)
