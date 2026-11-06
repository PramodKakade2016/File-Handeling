import sys 
import os 

def main():
    
    Filename = sys.argv[1]

    if (os.path.exists(Filename)):
        print("file is in current directory")
    else:
        print("file is Not in current directory")
    

if __name__ =="__main__":
    main()