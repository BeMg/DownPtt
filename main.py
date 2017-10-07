from utils import *
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--l", "--link", help='Download direct from article link')
parser.add_argument("--b", "--board", help='Download link from board')
parser.add_argument("--p", "--page", help='Download from board page limit')
parser.add_argument("--d", "--download", help='Download Content from file of data')
parser.add_argument("--s", "--save", help='Save result to file, Default data')

args = parser.parse_args()

filename = 'data' if args.s == None else args.s
page_size = 10000000 if args.p == None else args.p

if(args.l != None):
    content = getContent(args.l)
    String2File(content, filename)
elif(args.b != None):
    DownLoadFromBoard(args.b, page_size, filename)
elif(args.d != None):
    DownLoadFromListOFLink(args.d, filename)