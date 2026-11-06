import sys 
import os 

def main():
    
    Filename1 = sys.argv[1]
    Filename2 = sys.argv[2]

    if (os.path.exists(Filename1)):
        print("file is in current directory")
    else:
        print("file is Not in current directory")
    
    fobj1 = open(Filename1 , "r")
    fobj2= open(Filename2 , "w")

    fobj2.write(fobj1.read())
    print(fobj2.read())

    fobj1.close()
    fobj2.close()

if __name__ =="__main__":
    main()