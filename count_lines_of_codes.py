import os

dir = input("enter the folder path:")
#输入路径

if not os.path.exists(dir):
    print('this dir is not existent')
#判断路径是否存在

a = 0
b = 0
c = 0
d = 0


for root,dirs,files in os.walk(dir):
    for file in files:
        if  os.path.splitext(file)[1] == '.py':
            a = 1
        if  os.path.splitext(file)[1] == '.cpp':
            b = 1
        if  os.path.splitext(file)[1] == '.c':
            c = 1
        if  os.path.splitext(file)[1] == '.JAVA':
            d = 1
total = a + b + c + d
#统计文件夹内的编程语言数目
        
name = list() 
number = list()

for i in range(total):
    name.append([])
    number.append([])
#创建一个多维列表

for root,dirs,files in os.walk(dir):
    for file in files:
        if  os.path.splitext(file)[1] == '.py':
            name[a - 1].append(str(os.path.join(file)))
            fhand = open(os.path.join(root,file),encoding = 'utf-8')
            nums_0 = 0
            for line in fhand:
                line = line.strip()
                if line.startswith('#') or not len(line):
                    continue
                nums_0 = nums_0 + 1
            number[a - 1].append(nums_0)
        if  os.path.splitext(file)[1] == '.c':
            name[a + b  - 1].append(str(os.path.join(file)))
            fhand = open(os.path.join(root,file),encoding = 'ISO-8859-1')
            nums_1 = 0
            for line in fhand:
                line = line.strip()
                if line.startswith('//') or line.startswith('/*') or not len(line):
                    continue
                nums_1 = nums_1 + 1
            number[a + b  - 1].append(nums_1)
        if  os.path.splitext(file)[1] == '.cpp':
            name[a + b + c  - 1].append(str(os.path.join(file)))
            fhand = open(os.path.join(root,file),encoding = 'ISO-8859-1')
            nums_2 = 0
            for line in fhand:
                line = line.strip()
                if line.startswith('//') or line.startswith('/*') or not len(line):
                    continue
                nums_2 = nums_2 + 1
            number[a + b + c  - 1].append(nums_2)
        if  os.path.splitext(file)[1] == '.JAVA':
            name[a + b + c + d  - 1].append(str(os.path.join(file)))
            fhand = open(os.path.join(root,file),encoding = 'ISO-8859-1')
            nums_3 = 0
            for line in fhand:
                line = line.strip()
                if line.startswith('//') or line.startswith('/*') or not len(line):
                    continue
                nums_3 = nums_3 + 1
            number[a + b + c + d  - 1].append(nums_3)
#统计行数

for i in range(total):
    for j in range(len(name[i])):
        print(name[i][j],':',number[i][j])
#输出
        
    
input()
