#!/usr/bin/env python3
"""
Contains the AD class
"""

class AD(object): # pylint: disable=too-few-public-methods
    """
    AD is a high level abstraction of all A/D channels in the system. This class
    acts as an interface to get the current measurement from all the A/D channels
    registered in the system.
    """
    def __init__(self, concrete_ad, num_connected_ads):
        """
        When creating an AD object one must provide a concrete A/D object such
        as AdMcp3008 as well as the number of channels that are valid. These
        channels are assumed to be sequential. For example - 4 => 0 - 3 rather
        than 1, 3, 5, 7 or 3 - 6.
        """
        self.concrete_ad = concrete_ad
        self.num_ads = num_connected_ads

    def get_samples(self):
        """
        Query a list of the current A/D measurements
        """
        samples = []
        for index in range(0, self.num_ads):
            samples.append(self.concrete_ad.read_adc(index))

        return samples
