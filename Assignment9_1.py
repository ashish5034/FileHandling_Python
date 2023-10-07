import os

def main():
    
    print("Enter the file name you want to create: ")
    filename = input()
    
    if os.path.exists(filename):
        print(f"{filename} file is exist")
    else:
        open(filename,"x")
    
if __name__ == "__main__":
    main()