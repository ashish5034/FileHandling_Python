import os

def main():
    print("Enter the name of file that u want to open for read purpose: ")
    File_name = input()
    
    if os.path.exists(File_name):
        fobj = open(File_name,"r")#r=read mode
        
        if fobj:
            print("File sucessfully opened in read mode:")
            
            print("Data Frome file :")
            for line in fobj:
                print(line)
                
            fobj.close()
        else:
            print("Unable to open file:")
    else:
        print("There is no such file:")
    
if __name__ == "__main__":
    main()