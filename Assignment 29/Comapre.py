import sys 

def main():

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    fobj1 = open(file1 ,"r")
    fobj2 = open(file2 ,"r")

    if fobj1.read() == fobj2.read():
        print("Success")
    else:
        print("Failure")

if __name__ =="__main__":
    main()