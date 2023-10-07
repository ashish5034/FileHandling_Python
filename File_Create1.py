
import os

def main():
    print("Enter the name of file that u want to create: ")
    File_name = input()
    
    if os.path.exists(File_name):       #check whether file is exist or not
        print("unable to create file as file is already existing")
    else:                               #if not exist
        fobj = open(File_name,"x")      #open function to create and open file
    
if __name__ == "__main__":
    main()