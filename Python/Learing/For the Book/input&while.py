<<<<<<< HEAD
#######################输入超过两行的提示信息######################
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello," + name + "!")

#######################While + remove的用法######################
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
=======
#######################输入超过两行的提示信息######################
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello," + name + "!")

#######################While + remove的用法######################
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
>>>>>>> cfa80884cff10c00f67618eff25d92d2a1efd2ef
