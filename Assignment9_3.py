

import os
import sys
def main():
    if (len(sys.argv) != 2):
        print("Usage: Python copy_file.py <input_file>")
        exit()

    print("Enter the file name you want to creat: ")
    filename = input()
    
    if os.path.exists(filename):
        print(f"{filename} file is exist")
    else:
        fobj = open(filename,"x")
        fobj.close()

        fobj = open(filename,"a")
        if fobj:
            print(f"{filename} sucessfully open in Append mode:")
            data = input()
            fobj.write(data)
            fobj.close()
            
        fobj = open(filename,"r")
        if fobj:
            print(f"{filename} sucessfully open in read mode:")
            data = fobj.read()
            print(f"Data from {filename} is:",data)
            fobj.close()

        # fobj = open('Demo.txt',"w")
        # if fobj:
        #     print(f"{filename} sucessfully open in write mode:")
        #     # data = input()
        #     fobj.write(data)
        #     fobj.close()
    

if __name__ == "__main__":
    main()