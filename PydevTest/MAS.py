'''
Created on Nov 9, 2012

@author: school
'''

FoodStore = ["Bread", "Butter"]

def BBread():
    if "Bread" in FoodStore:
        return "Bread"
    return None

def BButter ():
    if "Butter" in FoodStore:
        return "Butter"
    return None

def Bjam ():
    if "Jam" in FoodStore:
        return "Jam"
    return "The store had no Jam"

Food = []

def MAS ():
    Food.append(BBread())
    Food.append(BButter())
    Food.append(Bjam())

MAS ()

print (Food)