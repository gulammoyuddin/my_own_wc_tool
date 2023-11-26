import locale
import sys,os

args=sys.argv
if len(args)>1 and args[len(args)-1][0] != '-':
    try:
        if args[1] == "-c":
            with open(args[2]) as file:
                file.seek(0,os.SEEK_END)
                print(file.tell(),args[2])
                file.close()
        elif args[1] == "-l":
            with open(args[2]) as file:
                data = file.readlines()
                print(len(data),args[2])
                file.close()
        elif args[1] == "-w":
            with open(args[2]) as file:
                data = file.readlines()
                wordslen=0
                for line in data:
                    wordslen=wordslen+len(line.split())
                print(wordslen,args[2])
                file.close()
        elif args[1] == "-m":
            with open(args[2],encoding="utf-8") as file:
                
                dat=file.read()
                print(len(dat),args[2])
                file.close()
        else:
            with open(args[1]) as file:
                data = file.readlines()
                wordslen=0
                for line in data:
                    wordslen=wordslen+len(line.split())
                file.seek(0,os.SEEK_END)
                print(len(data),wordslen,file.tell(),args[1])            
    except IOError:
        print("cannot open the file",args[1])
else:
    text=sys.stdin.read()
    bt=len(text.encode('utf-8'))
    lc=len(text.split('\n'))
    wc=0
    for line in text.split('\n'):
        wc=wc+len(line.split())
    ch=len(text)
    if len(args)>1:
        if args[1] == "-c":
            print(bt)
        elif args[1] == "-l":
            print(lc)
        elif args[1] == "-w":
            print(wc)
        elif args[1] == "-m":
            print(ch)
    else:
        print(lc,wc,bt)

    
