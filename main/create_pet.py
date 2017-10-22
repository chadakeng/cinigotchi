from init_pet import *
from random import randint

def gender_generate():
    gender = randint(0,1) # if 0 ->girl, if 1-> guy
    if gender == 0:
        def_gen = "F"
    else:
        def_gen = "M"
    return def_gen


def create_pet():
    temp_gender = gender_generate()
    print("Your pet's gender is:",temp_gender)
    # pet_name = input("Please name your pet: ") this will come later
    pet_name = "gotchi"
    pet = Pet(pet_name,temp_gender)

create_pet()
