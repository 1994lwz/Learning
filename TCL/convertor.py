import xlrd
import itertools
import os.path
import sys

ROWNUMBER=4
STEP=5
PREFIX="cx20921_"

class Item():
    
    
    def __init__(self,title):
        self.title=title
        self.items={}
        self.length=0
    def setColumNum(self,list):
        
        for index,name in enumerate(list):
            if name!='':
               self.items[index]=[]
        self.length=len(self.items.keys())
    def setValue(self,list):       
        for i in range(self.length):
            self.items[i].append(list[i])
                   
    
class DataGenerator(): 
    def __init__(self):
        self.output=[]          
    def open_file(self,path):
    
         book=xlrd.open_workbook(path)            
         first_sheet=book.sheet_by_index(0)  
            
         for rowindex in range(first_sheet.nrows):
             eachRow=first_sheet.row_values(rowindex)
             if eachRow[0]!='':
                 eachItem=Item(eachRow[0])
                 eachItem.setColumNum(eachRow[1:])
            
             else:
            
                 eachItem.setValue(eachRow[1:])
                 if (rowindex+1)%(ROWNUMBER+1)==0:
                     self.output.append(eachItem)
         
    def __construct_output(self):
        for result in self.output:
            for key in result.items:
                myList=result.items[key]
                if myList[1]=='':
                    min=myList[0]
                    max=myList[2]
                    gap=max-min
                    weight=round(gap/(STEP-1),3)
                    del myList[1]
                    for i in range(1,STEP-1):
                        result.items[key].insert(1,round(max-i*weight,3)) 
                else:
                    del result.items[key][0]
                    del result.items[key][1]  
                lastSlice=result.items[key][-1]
                if lastSlice=="int":
                    for i in range(0,len(result.items[key])-1):
                        result.items[key][i]=int(result.items[key][i])
                    
    def remove_int(self,line):
        myStr='(int)'
        index=line.index(myStr)
        line=line[:index]+line[index+5:]
        return line
        
              
    def write_file(self,path=None):
         self.__construct_output()
         fileNo=0
         file_accout = 0
         head="golem::setup_topology    {ALEX}\n"
         head2=""
         end="golem::execute_tuned_script {Z000}"
         begin="golem::sendcmd CAPT 30 "
         myList=[]
         titleList=[]
         for result in self.output:
            titleList.append(result.title)            
            for i in result.items.values():                
                myList.append(i[:-1])
                titleList.append(i[-1])
        
         for x in itertools.product(*myList):
            line=head+head2+begin+titleList[0]+" {" 
            line=line+"({}){}, ({}){}, ({}){}, ({}){}, ({}){}, ({}){},({}){},({}){}".\
            format(titleList[1],x[0],titleList[2],x[1],titleList[3],x[2],titleList[4],x[3],titleList[5],x[4],titleList[6],x[5],titleList[7],\
            x[6],titleList[8],x[7])
            line=line+'}\n'
            line=line+"{}{}".format(begin,titleList[9])
            line=line+' {'
            line=line+"({}){}, ({}){}, ({}){}, ({}){}, ({}){},({}){},({}){},({}){},({}){}".format(\
            titleList[10],x[8],titleList[11],x[9],titleList[12],x[10],titleList[13],\
            x[11],titleList[14],x[12],titleList[15],x[13],titleList[16],x[14],titleList[17],x[15],titleList[18],x[16])
            line=line+'}\n'      
            line=line+end
            while(line.find('(int)')!=-1):
                line=self.remove_int(line)
            
            
            if path is None:
                path=os.path.dirname(__file__)
                
            
            if fileNo >= 1000 :
                path_t = path + "\\" + str(file_accout)
                file_accout+=1
                fileNo=fileNo-1000
                               
            if fileNo < 10 :
                mode = "Z00" + str(fileNo)
            if 10 <= fileNo < 100 :
                mode = "Z0" + str(fileNo)
            if 100 <= fileNo < 1000 :
                mode = "Z" + str(fileNo)

            filepath = path + "\\" + str(file_accout)
            if os.path.isdir(filepath):
                print (filepath)
            else:
                os.mkdir(filepath)
                print ('create ' + filepath)


                
            filepath=filepath+'\\'+PREFIX+mode+'_scan.tcl'
            print(filepath)
            try:
               f=open(filepath,'w')
               f.write(line)
               f.close()            
               fileNo+=1
               
                
               
            except Exception as err:
                print(err)
            
           
             
    
if __name__=='__main__':
    
    mypath = os.getcwd()
    FW_path = mypath + '\\scan'
    #path='C:\shuaixiang_python\Scan_SSP_input.xlsx'
    DG=DataGenerator()
    DG.open_file(mypath + '\Scan_SSP.xlsx')
    
    DG.write_file(FW_path)
    #/***********************/
    
    #path='C:\shuaixiang_pythonn'
    #DG.write_file(path)
    
    
    '''
    try:
        path=sys.argv[1]        
    except IndexError:
        print("usage:%s{<source file> <destination file>(optional) |help}"%os.path.basename(sys.argv[0]))
    args=sys.argv[1:]  
    try:
        if len(args)==2 :
           DG=DataGenerator()
           DG.open_file(args[0])
           DG.write_file(args[1])
        else:
           DG=DataGenerator()
           DG.open_file(args[0])
           DG.write_file()
    except Exception as err:
        print(err)
    '''
    
