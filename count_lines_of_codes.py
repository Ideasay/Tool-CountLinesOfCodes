import os

#获取一个文件的后缀名
def getend(file):
    return os.path.splitext(file)[1]

#统计c,verilog,py,sh四个文件的有效行数的函数
## countc
def countc(file):
    fhand = open(os.path.join(file),encoding = 'ISO-8859-1')
    nums = 0
    for line in fhand:
        line = line.strip()
        if line.startswith('//') or line.startswith('/*') or not len(line):
            continue
        nums = nums + 1
    return nums

##countpy
def countpy(file):
    fhand = open(os.path.join(file),encoding = 'utf-8')
    nums = 0
    for line in fhand:
        line = line.strip()
        if line.startswith('#') or not len(line):
            continue
        nums = nums + 1
    return nums

##countv
def countv(file):
    fhand = open(os.path.join(file),encoding = 'utf-8')
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
def countsh(file):
    fhand = open(os.path.join(file),encoding = 'ISO-8859-1')
    nums = 0
    for line in fhand:
        line = line.strip()
        if line.startswith('#') or not len(line):
            continue
        nums = nums + 1
    return nums

#定义一个后缀对应处理方式的字典
type2func =  {'.c':countc,'.py':countpy,'.v':countv,'.sh':countsh}


#主函数

##输入路径
dir = input("enter the folder path:")

##判断路径是否存在
if not os.path.exists(dir):
    print('this dir is not existent')
    
##统计并输出
for root,dirs,files in os.walk(dir):
    for file in files:
        name_tmp = os.path.join(file)
        if getend(name_tmp) not in type2func:
            continue
        countfile = type2func[getend(os.path.join(root,file))]
        
        nums_tmp = countfile(os.path.join(root,file))
        print(name_tmp,':',nums_tmp)
        
        
