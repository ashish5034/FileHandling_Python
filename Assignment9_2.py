
import os

def main():
    
    print("Enter file name that U want to write:")
    filename = input()          
    
    if os.path.exists(filename):
        fobj = open(filename,"a")
        
        if fobj:
            print(f"{filename} successfuly open in append mode:")
            print(f"Enter data you want to write in {filename} :")
            data = input()
            fobj.write(data)
            fobj.close()
            
        fobj = open(filename,"r")
        if fobj:
            print(f"{filename} successfully open in reading mode:")
            data = fobj.read()
            print(f"Data from {filename} is:",data)
            fobj.close()
        
    
if __name__ == "__main__":
    main()