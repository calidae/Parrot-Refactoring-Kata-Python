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



from enum import Enum

class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3

class Parrot:

    LOAD_FACTOR = 9
    BASE_SPEED = 12
    MAX_SPEED = 24

    def __init__(self, type, number_of_coconuts, voltage, nailed):
        self.type = type
        self.number_of_coconuts = number_of_coconuts
        self.voltage = voltage
        self.nailed = nailed

    def speed(self):
        if self.type == ParrotType.EUROPEAN:
            return self._base_speed()
        if self.type == ParrotType.AFRICAN:
            return max(0, self._base_speed() - self._load_factor() * self.number_of_coconuts)
        if self.type == ParrotType.NORWEGIAN_BLUE:
            if self.nailed:
                return 0
            else: 
                return self._compute_base_speed_for_voltage(self.voltage)

        raise ValueError("should be unreachable")

    def _compute_base_speed_for_voltage(self, voltage):
       return min([self.MAX_SPEED, voltage * self._base_speed()])

    def _load_factor(self):
      return self.LOAD_FACTOR

    def _base_speed(self):
      return self.BASE_SPEED


class EuropeanParrot(Parrot):
    pass

class AmericanParrot(Parrot):
    pass

class NorwegianParrot(Parrot):
    pass 