import os

os.system("git --help")
#输入tag
name=input("name")
os.system("git tag " + name )
os.system("git tag origin " + name)