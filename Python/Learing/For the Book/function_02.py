<<<<<<< HEAD
###################向函数的参数里面传递列表的副本并对列表进行修改####################
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        #模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

def add_msg(unprinted_designs):
    #for unprinted_design in unprinted_designs:  #这样无法改变列表内每个元素的值
        #unprinted_design += " the great"
    for i in range(len(unprinted_designs)):
        unprinted_designs[i] += " the great"
    

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
add_msg(unprinted_designs)
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
#add_msg(unprinted_designs)
#show_completed_models(unprinted_designs)
=======
###################向函数的参数里面传递列表的副本并对列表进行修改####################
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        #模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


def add_msg(unprinted_designs):
    #for unprinted_design in unprinted_designs:  #这样无法改变列表内每个元素的值
        #unprinted_design += " the great"
    for i in range(len(unprinted_designs)):
        unprinted_designs[i] += " the great"
    

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
add_msg(unprinted_designs)
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
#add_msg(unprinted_designs)
#show_completed_models(unprinted_designs)
>>>>>>> cfa80884cff10c00f67618eff25d92d2a1efd2ef
