import sys

def main():

    try:
        fileName = sys.argv[1]
        Fobj = open(fileName , "r")
        
        
        #print(Fobj.read())

        for i in Fobj:
            print(i , end="")


        Fobj.close()
    except FileNotFoundError:
        print("Invalid file")

if __name__ == "__main__":
    main()
    
