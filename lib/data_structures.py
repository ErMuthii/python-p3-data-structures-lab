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
    food_names = [food['name'] for food in spicy_foods]
    return food_names

def get_spiciest_foods(spicy_foods):
    spiciest = [food for food in spicy_foods if food.get('spiciness',0) > 5]
    return spiciest

def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
        name = food.get('name','Invalid')
        cuisine = food.get('cuisine','Invalid')
        heat_level = food.get('heat_level',0)

        emojis = '🌶' * heat_level 
        print(f'{name} ({cuisine}) | Heat Level: {emojis}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    sort_cuisines = [food for food in spicy_foods if food.get('cuisine','Invalid') == cuisine]
    #This function will not return a single dictionary but a list of all matching dictionaries. if not indexed to pich the first
    return sort_cuisines[0]

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get('name','Invalid')
        cuisine = food.get('cuisine','Invalid')
        heat_level =  food.get('heat_level',0) 
        
        if heat_level > 5:
            emojis = '🌶' * heat_level 
            print(f'{name} ({cuisine}) | Heat Level: {emojis}')

def get_average_heat_level(spicy_foods):
   heat_level = [food.get('heat_level',0) for food in spicy_foods ]
   count = len(heat_level)

   if count == 0:
        return 0
   else:
       return sum(heat_level) // count
       

def create_spicy_food(spicy_foods, spicy_food):
    spicy_food = {
        'name': spicy_food.get('name',''),
        'cuisine': spicy_food.get('cuisine',''),
        'heat_level': spicy_food.get('heat_level',0)
    }

    spicy_foods.append(spicy_food)
    return spicy_foods