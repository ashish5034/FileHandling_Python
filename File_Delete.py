
import os

def main():
    print("Enter the name of file that u want to Delete: ")
    File_name = input()
    
    if os.path.exists(File_name):
        os.remove(File_name)
        print("File Deleted Successfully : ")
    else:
        print("There is no such file")
    
if __name__ == "__main__":
    main()