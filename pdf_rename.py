#encoding:utf-8
import os
import re
import sys

def format(filename):
    if (isinstance(filename, str)):
        tuple=('?','╲','*','/',',','"','<','>','|','“','"','，','‘','”',',','/',':')
        for char in tuple:
            if (filename.find(char)!=-1):
                filename=filename.replace(char," ")
        return filename
    else:
        return 'None'

def scan_files(dir, postfix):
    files_list=[]
    for root, sub_dirs, files in os.walk(dir):
        for special_file in files:
            if special_file.endswith(postfix):
                    files_list.append(os.path.join(special_file))
                          
    return files_list



path = "/Users/wangyisen/Desktop"
postfix = ".pdf"
files_list = scan_files(path,postfix)

for i in range(len(files_list)):
    print files_list[i]
    change_format = 'pdf2txt.py -o test.txt -t text -p 1 \''+files_list[i]+'\''
    os.system(change_format)
    f = open("test.txt")
    title = ""
    a = f.readline()
    while( a not in ("\r\n","\n") ):
        title += a
        a = f.readline()
    title = title.replace("\r\n"," ").strip()
    title = format(title)
    new =  title + ".pdf"
    print new
    os.rename(files_list[i], new)


