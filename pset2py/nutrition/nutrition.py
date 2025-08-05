def main():
    fruits = input("Item: ")

    nutrition(fruits)

def nutrition(fruit):
    calorie = {
        "cantaloupe" : 50,
        "avocado" : 50,
        "banana" : 110,
        "watermelon": 80,
        "lime": 20,
        "apple" : 130,
        "lemon": 15,
        "pineaple": 50,
        "sweet cherries": 100,
        "grapes": 90,
        "orange": 80,
        "grapefruit" : 60,
        "kiwifruit": 90,
        "plums": 70,
        "nectarine": 60,
        "peach": 60,
        "strawberries": 50,
        "tangerine": 50,
        "pear": 100,
        "honeydew melon": 50,
    }

    if fruit.lower() in calorie:
        print(f"Calories: {calorie[fruit.lower()]}")

main()