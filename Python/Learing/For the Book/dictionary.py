
#################字典的用法##########################
me = {}
me['first_name'] = 'Li'
me['last_name'] = 'Vicky'
me['age'] = 23
me['city'] = 'ChengDu'
#print(me)
for key, value in me.items():
    print('The ' + key.title() + ' is: ' + str(value) + '.')
print('\n')

family_name = ['first_name', 'last_name']
for key in me:  #等效于for key in me.keys():
    if key.lower() in family_name:
        print('The ' + key.title() + ' is: ' + str(me[key]) + '.')
    else:
        print('The key is: ' + key.title())
print('\n')

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'rudy',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()): #按照顺序遍历字典中的所有键
    print('Hi ' + name.title())
print('\n')
for language in set(favorite_languages.values()): #set避免遍历字典中的值中有重复的
    print(language.title())
print('\n')

#########################列表中存储字典###########################
name_1 = {'first_name': 'Vicky', 'last_name': 'Li', 'age': 23, 'city': 'ZY'}
name_2 = {'first_name': 'Yang', 'last_name': 'Liu', 'age': 24, 'city': 'CD'}
name_3 = {'first_name': 'Ashley', 'last_name': 'Pan', 'age': 23, 'city': 'DY'}
peoples = [name_1, name_2, name_3]
for people in peoples:
    print(people)

#########################字典中存储列表###########################
favorite_languages_list = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages_list.items():#遍历字典
    if len(languages) == 1:
        print('\n' + name.title() + "'s favorite languages are: " + languages[0])
    else:
        print('\n' + name.title() + "'s favorite languages are:")
        for language in languages:#遍历与key相关联的value列表里的值
            print('\t' + language.title())

#######################字典中存储字典############################
users = {
    '1994lwz': {
        'first': 'Vicky',
        'last': 'Li',
        'location': 'ZY',
        },
    'OMG': {
        'first': 'Yang',
        'last': 'Liu',
        'location': 'CD',
        },
    }#构造一个包含字典的字典
for username, user_info in users.items():#遍历该嵌套字典中的内容
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    #location = user_info['location']
    
    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + user_info['location'])
