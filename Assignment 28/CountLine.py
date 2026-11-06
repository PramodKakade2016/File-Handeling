import sys

def main():

    try:
        fileName = sys.argv[1]
        Fobj = open(fileName , "r")
        print(len(Fobj.readlines()))

        Fobj.close()
    except FileNotFoundError:
        print("Invalid file")

if __name__ == "__main__":
    main()
    
