import sys

def main():

    try:
        fileName = sys.argv[1]
        Fobj = open(fileName , "r")
        #print(len(Fobj.readlines()))
        
        count = 0
        for i in Fobj.readlines():
            #print(len(i.split()))

            count = count + len(i.split())
        print(count)   

        Fobj.close()
    except FileNotFoundError:
        print("Invalid file")

if __name__ == "__main__":
    main()
    
