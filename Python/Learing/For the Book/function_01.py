<<<<<<< HEAD
#####################函数的使用##################

###############让实参变成可选的，并在用户没有提供该实参时不使用该实参#################
def get_formatted_name(first_name, last_name, middle_name = ''):
    #有默认值的实参放在最后
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician + '\n')

##########################函数返回字典##########################
def build_person(first_name, last_name, age = ''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
    
while True:
    print("Please input your name(input 'q' anytime to quit the system)")
    first_name = input('First_name: ')
    if first_name == 'q':
        break
    last_name = input('Last_name: ')
    if last_name == 'q':
        break
    print("Did you want enter your age? (y/n)")
    flag = input()
    if flag == 'q':
        break
    elif flag == 'y':
        person_age = input('Age: ')
        if person_age == 'q':
            break
        musician = build_person(first_name, last_name, person_age)
        print(musician)
    else:
        musician = build_person(first_name, last_name)
        print(musician)

print('\n')
=======
#####################函数的使用##################

###############让实参变成可选的，并在用户没有提供该实参时不使用该实参#################
def get_formatted_name(first_name, last_name, middle_name=''):
    #有默认值的实参放在最后
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician + '\n')

##########################函数返回字典##########################
def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
   
    
while True:
    print("Please input your name(input 'q' anytime to quit the system)")
    first_name = input('First_name: ')
    if first_name == 'q':
        break
    last_name = input('Last_name: ')
    if last_name == 'q':
        break
    print("Did you want enter your age? (y/n)")
    flag = input()
    if flag == 'q':
        break
    elif flag == 'y':
        person_age = input('Age: ')
        if person_age == 'q':
            break
        musician = build_person(first_name, last_name, person_age)
        print(musician)
    else:
        musician = build_person(first_name, last_name)
        print(musician)

print('\n')
>>>>>>> cfa80884cff10c00f67618eff25d92d2a1efd2ef
