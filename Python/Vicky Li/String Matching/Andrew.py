# stringMatch
def stringMatch():
    sum = 0
    with open('Sample.txt','r',encoding='utf-8') as f:  
        for index, line in enumerate(f.readlines()):
            pos = 0
            while pos < len(line):
                pos = line.find('水',pos)
                if pos != -1:
                    if index == 0:
                        print(index+1,pos-1)                                                     
                    else:
                        print(index+1,pos)         
                    sum += 1
                    pos += 1
                if pos == -1:
                    break
    print(sum)
