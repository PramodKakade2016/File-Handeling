import sys 

def main():

    file = sys.argv[1]
    text = sys.argv[2]

    fobj = open(file, "r")

    count = 0
    for i in fobj.readlines():
        
        for j in i.split():
            if text == j:
                count = count + 1       
    print(count)

if __name__ == "__main__":
    main()