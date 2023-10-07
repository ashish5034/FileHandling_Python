
import os

def main():
    
    print("Enter the name of file that u want to open for read purpose: ")
    File_name = input()
    
    if os.path.exists(File_name):
        fobj = open(File_name,"r")                         #r=file open in read mode
        
        if fobj:
            print("File sucessfully opened in read mode:")
            
            Data = fobj.read(3)  #for read 10 bytes
            print("Data from file is: ",Data)
            
            fobj.close()
        else:
            print("Unable to open file:")
    else:
        print("There is no such file:")
    
if __name__ == "__main__":
    main()