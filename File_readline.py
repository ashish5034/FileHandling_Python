import os

def main():
    print("Enter the name of file that u want to open for read purpose: ")
    File_name = input()
    
    if os.path.exists(File_name):
        fobj = open(File_name,"r")#r=read mode
        
        if fobj:
            print("File sucessfully opened in read mode:")
            
            line1 = fobj.readline()
            line2 = fobj.readline()
            line3 = fobj.readline()
            
            print("First line is: ",line1)
            print("Second line is: ",line2)
            print("Third line is: ",line3)
            
            fobj.close()
        else:
            print("Unable to open file:")
    else:
        print("There is no such file:")
    
if __name__ == "__main__":
    main()