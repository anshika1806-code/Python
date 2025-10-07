import math
'''Name : Anshika Gupta
   Date : 8-10-2025
   Project : Building a Calorie Tracking Console App
'''
print("Welcome to a calorie tracker app")
print("This App keeps the track of your calories and gives you the an average of your calories intake ")
n=int(input(" how Many meals do You want to enter?"))
Meal_lst=[]
Calorie_lst=[]
Calorie_limit=int(input("Enter your daily calorie limit "))
for i in range(n):
    Meal_name =input("Enter Your meal name eg.Breakfast")
    Calorie_amount=int(input("Enter Your calorie amount eg.360.0,or366.0"))
    Meal_lst.append(Meal_name)
    Calorie_lst.append(Calorie_amount)
total=sum(Calorie_lst)
avg= total/n
if total == Calorie_limit:
    print("Bravo! You are going good with accurate calories amount🥳🥳")
elif total> Calorie_limit:
    print("Keep your diet tight still more than enough calories intake!😢")
elif total<Calorie_limit:
    print("Relax! There is a still a limit of sweet🍨😉")
print("\nMeal Name       Calories")
print("-" * 32)
for meal, cal in zip(Meal_lst, Calorie_lst):
    print(f"{meal:<15}{cal:>10.0f}")
print("-" * 32)
print(f"{'Total:':<15}{total:>10.0f}")
print(f"{'Average:':<15}{avg:>10.2f}")

    
