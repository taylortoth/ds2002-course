#!/Users/taylortoth/miniconda3/bin/python3

import os

os.environ["FAV_ANIMAL"] = "Dinosaur"
os.environ["AGE"] = "34"
os.environ["UVA_YEAR"] = "Third"

FAV_ANIMAL_INPUT = input("What is your favorite animal? ")
AGE_INPUT = input("What is your mom's age? ")
UVA_YEAR_INPUT = input("What year are you at UVA? ")

os.environ["FAV_ANIMAL"] = FAV_ANIMAL_INPUT
os.environ["AGE"] = AGE_INPUT
os.environ["UVA_YEAR"] = UVA_YEAR_INPUT

FAV_ANIMALENV = os.getenv("FAV_ANIMAL")
AGEENV = os.getenv("AGE")
UVA_YEARENV = os.getenv("UVA_YEAR")

print(FAV_ANIMALENV)
print(AGEENV)
print(UVA_YEARENV)

