## this is to read write append a text file

with open("IO_file.txt",'a') as fa:
    fa.write("This is the append statement")

with open("IO_file.txt",'w') as fw:
    fw.write("This is the write statement")

with open("IO_file.txt",'r') as fr:
    print(fr.read())

