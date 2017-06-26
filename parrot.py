#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Un lloro Europeu sempre vola a 12 km/h.
 
# Un lloro Africà vola depenent de quants cocos porti. 
# Si no porta cap coco, vola tan ràpid com un lloro Europeu. 
# Per cada coco que porta és s’alenteix 9 km/h. (Evidentment, no pot tenir velocitat negativa).
 
# Un lloro blau noruec pot estar clavat. Si està clavat, no pot volar. 
# Si no ho està, vola depenent del voltatge que hi apliquem. 
# El voltatge multiplica la velocitat a la que vola un lloro (com ja havíem dit, 12 km/h), per exemple amb 1.5 V vola a 18 km/h. 
# Per molt voltatge que hi apliquem, mai volarà a més de 24 km/h.

from abc import ABCMeta
from abc import abstractmethod

class Parrot(object):
    __metaclass__ = ABCMeta
    BASE_SPEED = 12

    @abstractmethod
    def speed(self):
        return self.BASE_SPEED


class EuropeanParrot(Parrot):
    def speed(self):
        return super(EuropeanParrot, self).speed()


class AfricanParrot(Parrot):
    LOAD_FACTOR = 9

    def __init__(self, number_of_coconuts):
        super(AfricanParrot, self).__init__()
        self.number_of_coconuts = number_of_coconuts

    def speed(self):
        return max(0, self.BASE_SPEED - self.LOAD_FACTOR * self.number_of_coconuts)
    

class NorwegianParrot(Parrot):
    MAX_SPEED = 24

    def __init__(self, voltage, nailed):
        super(NorwegianParrot, self).__init__()
        self.voltage = voltage
        self.nailed = nailed
 
    def speed(self):
        if self.nailed:
            return 0
        else: 
            return self._compute_base_speed_for_voltage(self.voltage)
    
    def _compute_base_speed_for_voltage(self, voltage):
       return min([self.MAX_SPEED, voltage * self.BASE_SPEED])
