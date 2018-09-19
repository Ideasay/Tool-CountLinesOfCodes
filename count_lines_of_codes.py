import os
import re

#获取一个文件的后缀名
def getend(file):
    return os.path.splitext(file)[1]

#统计c,verilog,py,sh四个文件的有效行数的函数
## countc
def countc(fhand):
    nums = 0
    isblock = 0
    for line in fhand:
        line = line.strip()
        if(isblock == 0):
            if line.startswith('//') or not len(line):
                continue
            if line.startswith('/*'):
                if not re.search('.*\*/$',line):
                    isblock = 1
                if re.search('.*\*/.*',line):
                    nums = nums + 1
                continue
            elif re.search('.*/\*$',line):
                isblock = 1
            elif re.search('.*/\*.*',line):
                if not re.search('.*/\*.*\*/[$,.*]',line):
                    isblock = 1
            nums = nums + 1

        elif(isblock == 1):
            if  re.search('.*\*/$',line):
                isblock = 0
            if re.search('^\*/',line):
                if not re.search('^\*/.*/\*',line):
                    isblock = 0
            if re.search('.*\*/.*',line):
                if not re.search('.*\*/.*/\*',line):
                    isblock = 0

    return nums

##countpy
def countpy(fhand):
   return countsh(fhand)


##countv
countv = countc
        

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
sum_all_language = {'C语言':0,'Python':0,'Verilog':0,'Unix脚本文件':0}
sum_all_name_end = {'.c':0,'.h':0,'.py':0,'.v':0,'.sh':0}
typename = {'.c':'C语言','.h':'C语言','.py':'Python','.v':'Verilog','.sh':'Unix脚本文件'}
print(type(sum_all_language))

#主函数

##输入路径,模式
print('###################################################')
print("# 目前仅支持C语言，verilog，python,shell文件的处理  #\n# mode1:按照代码语言进行统计请输入0                 #\n# mode2:按照文件后缀名进行统计输入1                 #")
print('###################################################')
mode = int(input("请输入选择的模式："))
dir = input("输入文件夹路径名:")



##判断路径是否存在
if not os.path.exists(dir):
    print('this dir is not existent')
    exit()
    
##统计
if mode == 0:
    for root,dirs,files in os.walk(dir):
        for file in files:
            name_tmp = os.path.join(file)
            suffix = getend(name_tmp)
            if suffix not in type2func:
                continue
            with open(os.path.join(root,file),encoding = 'utf  -8') as fhand:
                countfile = type2func[suffix]
                nums_tmp = countfile(fhand)
                fhand.close()
            print(name_tmp,':',nums_tmp)
            sum_all_language[typename[suffix]] += nums_tmp
    print('###################################################')
    for i in sum_all_language:
        print(i,':',sum_all_language[i])


elif mode == 1:
    require = input("请输入需要统计的目标文件后缀，例如.py,.v：")
    lang = require.split(',')
    for root,dirs,files in os.walk(dir):
        for file in files:
            name_tmp = os.path.join(file)
            suffix = getend(name_tmp)
            if suffix not in type2func or suffix not in lang:
                continue
            with open(os.path.join(root,file),encoding = 'utf-8') as fhand:
                countfile = type2func[suffix]
                nums_tmp = countfile(fhand)
                fhand.close()
            print(name_tmp,':',nums_tmp)
            sum_all_name_end[suffix] += nums_tmp
    print('###################################################')
    for i in lang:
        print(i,':',sum_all_name_end[i])

