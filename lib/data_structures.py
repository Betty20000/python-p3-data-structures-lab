spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods if 'name' in food]



def get_spiciest_foods(spicy_foods):
    
    return  [food for food in spicy_foods if food["heat_level"] > 5]
    

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]  
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
    return

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
    
    

def print_spiciest_foods(spicy_foods):
    spici_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spici_foods)
    return spici_foods

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    if num_foods == 0:
        return 0 
    average_heat_level = total_heat_level / num_foods
    return average_heat_level
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
get_names(spicy_foods)





