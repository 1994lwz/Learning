<<<<<<< HEAD
#############结合使用位置实参、任意数量实参、任意数量的关键字实参###############
def make_pizza(*toppings):
    #使用任意数量实参
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
    #结合使用位置实参和任意数量实参
    print("\n Making a " + str(size) + 
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def make_car(manufacturer, model, **car_info):
    profile = {}
    profile['manu'] = manufacturer
    profile['model'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print("\n")
print(car)
=======
#############结合使用位置实参、任意数量实参、任意数量的关键字实参###############
def make_pizza(*toppings):
    #使用任意数量实参
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
    #结合使用位置实参和任意数量实参
    print("\n Making a " + str(size) + 
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def make_car(manufacturer, model, **car_info):
    profile = {}
    profile['manu'] = manufacturer
    profile['model'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print("\n")
print(car)
>>>>>>> cfa80884cff10c00f67618eff25d92d2a1efd2ef
