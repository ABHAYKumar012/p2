import csv
from random import randint

# Define the dataset file name
dataset_file = 'food.csv'

# Load the dataset from the CSV file
def load_dataset(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        data = [row for row in reader]
    return data

# Define the food categories based on the loaded dataset
protein = []
fruit = []
vegetable = []
grains = []
protein_snack = []
taste_enhancer = []

dataset = load_dataset(dataset_file)
for row in dataset:
    protein.append(row[1])
    fruit.append(row[2])
    vegetable.append(row[3])
    grains.append(row[4])
    protein_snack.append(row[5])
    taste_enhancer.append(row[6])

def calc_tdee(name, weight, height, age, gender, phys_act):
    if gender == 'Female':
        bmr = 655 + (9.6 * weight) + (1.8 * height ) - (4.7 * age)
    else:
        bmr = 66 + (13.7 * weight) + (5 * height ) - (6.8 * age)

    if phys_act == 'value1':
        tdee = bmr * 1.2
    elif phys_act == 'value2':
        tdee = bmr * 1.375
    elif phys_act == 'value3':
        tdee = bmr * 1.55
    elif phys_act == 'value4':
        tdee = bmr * 1.735
    else:
        tdee = bmr * 1.9 
    return tdee

def bfcalc(tdee):
    breakfast = protein[randint(0, len(protein)-1)] + ", "
    breakfast += fruit[randint(0, len(fruit)-1)]

    if tdee >= 2200:
        breakfast += ", " + grains[randint(0, len(grains)-1)]

    return breakfast

def s1calc(tdee):
    snack1 = ""
    if tdee >= 1800:
        snack1 = protein_snack[randint(0, len(protein_snack)-1)]

    return snack1

def lcalc(tdee):
    lunch = ""
    lunch += protein[randint(0, len(protein)-1)] + ", "
    lunch += vegetable[randint(0, len(vegetable)-1)] + ", "
    lunch += "Leafy greens, "
    lunch += taste_enhancer[randint(0, len(taste_enhancer)-1)] + ", "
    lunch += grains[randint(0, len(grains)-1)]

    if tdee >= 1500:
        lunch += ", " + fruit[randint(0, len(fruit)-1)]

    if tdee >= 1800:
        lunch += ", " + protein[randint(0, len(protein)-1)] + ", "
        lunch += vegetable[randint(0, len(vegetable)-1)]
    return lunch

def s2calc(tdee):
    snack2 = protein_snack[randint(0, len(protein_snack)-1)] + ", "
    snack2 += vegetable[randint(0, len(vegetable)-1)]
    return snack2

def dcalc(tdee):
    dinner = ""
    dinner += protein[randint(0, len(protein)-1)] + ", "
    dinner += "2 vegetables 80g, "
    dinner += "Leafy Greens, "
    dinner += grains[randint(0, len(grains)-1)] + ", "
    dinner += taste_enhancer[randint(0, len(taste_enhancer)-1)]

    if tdee >= 1500:
        dinner += ", " + protein[randint(0, len(protein)-1)]

    if tdee >= 2200:
        dinner += ", " + grains[randint(0, len(grains)-1)] + ", "
        dinner += taste_enhancer[randint(0, len(taste_enhancer)-1)]
    return dinner

def s3calc(tdee):
    snack3 = fruit[randint(0, len(fruit)-1)]
    return snack3

# Example usage
name = "John"
weight = 70  # in kg
height = 170  # in cm
age = 30
gender = "Male"
phys_act = "value3"  # Adjust this value based on activity level

tdee = calc_tdee(name, weight, height, age, gender, phys_act)
breakfast = bfcalc(tdee)
snack1 = s1calc(tdee)
lunch = lcalc(tdee)
snack2 = s2calc(tdee)
dinner = dcalc(tdee)
snack3 = s3calc(tdee)

print(f"Name: {name}")
print(f"TDEE: {tdee} calories")
print("Diet Recommendations:")
print(f"Breakfast: {breakfast}")
print(f"Snack 1: {snack1}")
print(f"Lunch: {lunch}")
print(f"Snack 2: {snack2}")
print(f"Dinner: {dinner}")
print(f"Snack 3: {snack3}")
