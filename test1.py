from sys import argv

script,filename = argv #赋值给argv变量

txt = open(filename)#将赋值给argv的文件名的内容打开并赋值给txt



print("Here's your file %r:" %filename )


print(txt.read())#读取txt的内容并打印

txt.close()

print ("type the filename again:")

file_again = input(">")#输入你想打开的文件名，赋值给file_again

txt_again = open(file_again)#打开你输入的文件并赋值给txt_again



print(txt_again.read())

txt_again.close()


