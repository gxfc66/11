import argparse

parser = argparse.ArgumentParser(description='传入一个数字')
#type是传入的参数的数据类型，help是参数的提示信息
parser.add_argument('--tag',type=str,help='传入的数字')
parser.add_argument('--commit',type=str,help='传入的数字')
parser.add_argument('a',type=str,help='传入的数字')
args= parser.parse_args()

#获得传入的参数

print(args.commit)
print(args.tag)
print(args.a)