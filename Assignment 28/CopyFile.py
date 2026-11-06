import sys

def main():

    try:
        fileName = sys.argv[1]
        file2 =  sys.argv[2]
        Fobj = open(fileName , "r")
        Fobj2 = open(file2 , "w")
        
        
        #print(Fobj.read())

        for i in Fobj:
            Fobj2.write(i)
        #Fobj2.write(Fobj.read())


        Fobj.close()
    except FileNotFoundError:
        print("Invalid file")

if __name__ == "__main__":
    main()
    
