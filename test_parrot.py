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

from parrot import EuropeanParrot
from parrot import AfricanParrot
from parrot import NorwegianParrot


def test_european_parrot_speed():
    parrot = EuropeanParrot()
    assert parrot.speed() == 12


def test_african_parrot_speed():
    parrot = AfricanParrot(0)
    assert parrot.speed() == 12

def test_african_parrot_speed_one_coco():
    parrot = AfricanParrot(1)
    assert parrot.speed() == 3

def test_african_parrot_speed_two_coco():
    parrot = AfricanParrot(2)
    assert parrot.speed() == 0


def test_norwegian_parrot_speed_nailed():
    parrot = NorwegianParrot(1, True)
    assert parrot.speed() == 0

def test_norwegian_parrot_speed_with_one_volt():
    parrot = NorwegianParrot(1, False)
    assert parrot.speed() == 12

def test_norwegian_parrot_speed_with_one_volt_and_half():
    parrot = NorwegianParrot(1.5, False)
    assert parrot.speed() == 18

def test_norwegian_parrot_speed_with_three_volt():
    parrot = NorwegianParrot(3, False)
    assert parrot.speed() == 24

def test_norwegian_parrot_speed_with_no_volt():
    parrot = NorwegianParrot(0, False)
    assert parrot.speed() == 0
