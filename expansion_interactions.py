import numpy as np

# Set parameters...just using default from my experiments
Dw = 0.07
v = 1.19
Ro = 3.5

Dg = 1. #TODO: PUT IN THE ACTUAL VALUE

class Strain(object):
    def __init__(self, name, strain_index, growth_rate=None):
        self.name = name
        self.strain_index = strain_index # shorthand for the strain; its number
        self.growth_rate = growth_rate

class Strain_Interaction(object):
    """Defines all properties via the combination of both strains."""
    def __init__(self, strain_1, strain_2, wave_type):
        self.strain_1 = strain_1
        self.strain_2 = strain_2

        g1 = strain_1.growth_rate
        g2 = strain_2.growth_rate
        self.s = 2.*(g1 - g2)/(g1 + g2)

        self.vw = None
        if wave_type is 'deterministic':
            self.vw = 2 * np.sqrt(self.s*Dw)
        if wave_type is 'noisy':
            self.vw = 2*self.s*Dw/Dg

class Derive_From_Weakest_Strain(object):

    def __init__(self, strain_names, vw_strains):
        """Assumes that velocities are relative to strain 0!"""
