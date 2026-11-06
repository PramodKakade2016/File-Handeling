import sys

def main():

    filename = sys.argv[1]
    text = sys.argv[2]

    fobj = open(filename, 'r')

    count = 0
    present = False 

    for i in fobj:
        print(i)
        count = count + 1
        if text == i.strip():
            present = True

    if present:
        print(f"In file {filename} the {text} is present")

    else:
        print(f"In file {filename} the {text} is NOT present")

    print(f"Lines Scanned {count}")

    fobj.close()

if __name__ =="__main__":
     main()