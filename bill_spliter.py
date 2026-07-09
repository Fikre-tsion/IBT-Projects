# Write a small Python program that splits a restaurant bill
#with a tip across friends — using variables, operators, a function, and a loop.

total= 1000
People=5

fam = [
    "Dawit",
    "Wudasie",
    "Leul",
    "Fikre"
]

def split_bill(rate=0.10):
    total_bill = total + total * 0.10
    per_person_bill= total_bill/People

    for name in fam:
        print(f"Dear {name}, we kindly ask you to pay {per_person_bill} for the lunch based on the fair distribution among all of us.")
        print("==========================  ====================================== ==================================")


split_bill()