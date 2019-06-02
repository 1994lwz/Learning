###########列表表达式 for函数的用法 条件判断###################
for i in range(3, 31, 3):
    print(i)

million = [i**3 for i in range(1, 11)]
print(million)
#print(max(million))
#print(sum(million))

print('Mi' == 'mi')
print('MIK'.lower() == 'mik')
print('Mi' == 'mi' and 'MIK'.lower() == 'mik')
print('Mi' == 'mi' or 'MIK'.lower() == 'mik')
print(9 in million)
print(9 not in million)

price = 9
print('Your admission cost is $' + str(price) +'.')

###############列表对比不区分大小写###################
current_users = ['Tin', 'Tris', 'Yang', 'Fred', 'Vicky']
check_users = []
new_users = ['Ashley', 'Lucy', 'TIN', 'yAng', 'Clare']

for current_user in current_users:
    check_users.append(current_user.lower())
    
for new_user in new_users:
    if new_user.lower() in check_users:
        print(new_user + ' is in the current_users')
    else:
        print('Welcome ' + new_user)


