import os

#获取一个文件的后缀名
def getend(file):
    return os.path.splitext(file)[1]

#统计c,verilog,py,sh四个文件的有效行数的函数
## countc
def countc(fhand):
    nums = 0
    for line in fhand:
        line = line.strip()
        if line.startswith('//') or line.startswith('/*') or not len(line):
            continue
        nums = nums + 1
    return nums

##countpy
def countpy(fhand):
    return(countsh(fhand))


##countv
def countv(fhand):
    nums = 0
    flag = 1
    for line in fhand:
        line = line.strip()
        if line.startswith('//') or line.startswith('/*') or not len(line):
            continue
        if flag == 1:
            if line.startswith('module'):
                flag = 0
            else:
                break
        nums = nums + 1
    if flag == 0:
        return nums
    else:
        return 'this is not  a verilog codes file'
        

##countsh
def countsh(fhand):
    nums = 0
    for line in fhand:
        line = line.strip()
        if line.startswith('#') or not len(line):
            continue
        nums = nums + 1
    return nums

#定义一个后缀对应处理方式的字典,以及编码方式的字典,以及统计各类型文件的总和
type2func =  {'.c':countc,'.h':countc,'.py':countpy,'.v':countv,'.sh':countsh}
encode = {'.c':'ISO-8859-1','.h':'ISO-8859-1','.py':'utf-8','.v':'utf-8','.sh':'utf-8'}
sum_all = {'C语言':0,'C语言':0,'Python':0,'Verilog':0,'Unix脚本文件':0}
typename = {'.c':'C语言','.h':'C语言','.py':'Python','.v':'Verilog','.sh':'Unix脚本文件'}

#主函数

##输入路径
dir = input("enter the folder path:")

##判断路径是否存在
if not os.path.exists(dir):
    print('this dir is not existent')
    exit()
    
##统计并输出
for root,dirs,files in os.walk(dir):
    for file in files:
        name_tmp = os.path.join(file)
        if getend(name_tmp) not in type2func:
            continue
        fhand = open(os.path.join(root,file),encoding = encode[getend(name_tmp)])
        countfile = type2func[getend(name_tmp)]
        nums_tmp = countfile(fhand)
        fhand.close()
        print(name_tmp,':',nums_tmp)
        if type(nums_tmp) == int:
            sum_all[typename[getend(name_tmp)]] += nums_tmp
print('************************************\n',sum_all)
        
        
        

        
        
