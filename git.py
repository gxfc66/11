import argparse
import os
parser = argparse.ArgumentParser(description='传入一个数字')
#type是传入的参数的数据类型，help是参数的提示信息
parser.add_argument('--add',type=str,help='传入的数字')
parser.add_argument('--commit',type=str,help='传入的数字')
parser.add_argument('--branch',type=str,help='传入的数字')
parser.add_argument('--push',type=str,help='传入的数字')
args= parser.parse_args()

#获得传入的参数

print(args.add)
print(args.commit)
print(args.push)

if args.branch==None:
    print("no branch")
    os.system("git add " + args.add)
    os.system("git commit -m " + args.commit)
    os.system("git push ")

else:
    os.system("git add " + args.add)
    os.system("git commit -m " + args.commit)
    os.system("git push ")
    os.system("git checkout -b " + args.branch)
    os.system("git push origin " + args.branch)
