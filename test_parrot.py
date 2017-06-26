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

from parrot import Parrot
from parrot import ParrotType


def test_european_parrot_speed():
    parrot = Parrot(ParrotType.EUROPEAN, 0, 0, False)
    assert parrot.speed() == 12

def test_european_parrot_speed_nailed():
    parrot = Parrot(ParrotType.EUROPEAN, 0, 0, True)
    assert parrot.speed() == 12

def test_european_parrot_speed_one_coco():
    parrot = Parrot(ParrotType.EUROPEAN, 1, 0, False)
    assert parrot.speed() == 12

def test_european_parrot_speed_with_voltage():
    parrot = Parrot(ParrotType.EUROPEAN, 0, 1.5, False)
    assert parrot.speed() == 12

def test_african_parrot_speed():
    parrot = Parrot(ParrotType.AFRICAN, 0, 0, False)
    assert parrot.speed() == 12

def test_african_parrot_speed_one_coco():
    parrot = Parrot(ParrotType.AFRICAN, 1, 0, False)
    assert parrot.speed() == 3

def test_african_parrot_speed_two_coco():
    parrot = Parrot(ParrotType.AFRICAN, 2, 0, False)
    assert parrot.speed() == 0

def test_african_parrot_speed_with_norwgian_conditions():
    parrot = Parrot(ParrotType.AFRICAN, 1, 3, True)
    assert parrot.speed() == 3

def test_norwegian_parrot_speed_nailed():
    parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 1, True)
    assert parrot.speed() == 0

def test_norwegian_parrot_speed_with_one_volt():
    parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 1, False)
    assert parrot.speed() == 12

def test_norwegian_parrot_speed_with_one_volt_and_half():
    parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 1.5, False)
    assert parrot.speed() == 18

def test_norwegian_parrot_speed_with_three_volt():
    parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 3, False)
    assert parrot.speed() == 24

def test_norwegian_parrot_speed_with_no_volt():
    parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 0, False)
    assert parrot.speed() == 0

def test_norwegian_parrot_speed_with_african_conditions():
    parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 1, 1, False)
    assert parrot.speed() == 12