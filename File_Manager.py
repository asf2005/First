from pathlib import Path
import os, shutil
import string

def main():
    dirs, pth = Get_drives()
    print("""Hi there, it's a file manager simulator. You can walk through folders,c for copy,
m for move, d for delete, r for rename.
====""")
    while True: 
 
        DisplayPt(dirs) 
        y = input('Enter: ')
        if y=='c':
            Copy(pth, dirs)
        
        elif y=='m':
            Move(pth, dirs)
        
        elif y=='r':
            Rename(pth, dirs)
            
        elif y=='d':
            Remove(pth, dirs)
        
        elif y=='b'or type(int(y))==int:
            if pth in Get_drives():
                pth = dirs[int(y) - 1]
            pth, dirs = DirChg(pth, dirs, y)

        
def Get_drives():
    drives = []
    
    for letter in string.ascii_uppercase:
        drive = Path(f"{letter}:\\")
        
        if drive.exists():
            drives.append(drive)
               
    return drives, drives

def Get_directory():
    pth = Path.cwd()   #First step, where program is run.
    x = 0
    try:
        while True:
            y = os.listdir(pth.parents[x])    #Tries to find the root path.
            x+=1
        
    except:
        pth = pth.parents[x -1]       #Signs pth to root path.
        dirs = os.listdir(pth)      #Lists all existing folders and files in root path.
        
    return pth, dirs

def DisplayPt(dirs):
    y = 1
    for g in dirs:
        print(y,g)
        y += 1   
        
def DirChg(pth, dirs, y):
        
        if y == 'b':
            try:    
                os.chdir(Path(pth.parents[0]))     #Changes current path to its parent path.
                print('====\n')
                pth = Path.cwd()
                dirs = os.listdir(pth)
            except:
                dirs, pth = Get_drives()
            
        elif int(y) != 0:
            target = pth/dirs[int(y)-1]
            if target.is_dir():
                os.chdir(pth/dirs[int(y)-1])  #Goes into desired folder.
                print('====\n')
                pth = Path.cwd()
                dirs = os.listdir(Path.cwd())
            else:
                print('Not directory...')
                 
        return pth, dirs

def Copy(pth, dirs):
    
    y = input('Which folder or file do you want to copy: ')
    
    source = Path(pth/dirs[int(y)-1])
    pth, dirs = Get_directory()

    while True:
        DisplayPt(dirs) 
        y = input('To which folder, d for copying here: ')
        if y != 'd':
            pth, dirs = DirChg(pth, dirs, y)
        elif y == 'd':
            distenation = Path(pth)
            break
        
    if source.is_dir():
        shutil.copytree(source, distenation/source.name)
    else:
        shutil.copy2(source, distenation)
    
    pth = Path.cwd()
    dirs = os.listdir(Path.cwd())  
      
    return pth, dirs       
      
def Move(pth, dirs):
    y = input('Which folder or file do you want to move: ')
    
    source = Path(pth/dirs[int(y)-1])
    pth, dirs = Get_directory()

    while True:
        DisplayPt(dirs) 
        y = input('To which folder, d for moving here: ')
        if y != 'd':
            pth, dirs = DirChg(pth, dirs, y)
        elif y == 'd':
            distenation = Path(pth)
            break
        
    shutil.move(source, distenation)
    
    pth = Path.cwd()
    dirs = os.listdir(Path.cwd())
    
    return pth, dirs       

def Remove(pth, dirs):
    y = input('Which folder or file do you wnat to delete: ')
    answer = input(f'Are you sure want to delete it:(y/n) {Path(pth, dirs[int(y) - 1])} ').lower().startswith('y')
    
    if answer:
        try:
            try:
                os.rmdir(Path(pth, dirs[int(y) - 1]))
            except:
                os.unlink(Path(pth, dirs[int(y) - 1]))
        
        except:
            shutil.rmtree(Path(pth, dirs[int(y) - 1]))
            
    
    pth = pth
    dirs = os.listdir(pth)
    
    return pth, dirs
   
def Rename(pth, dirs):
    y = input('Which folder or file do you want to rename: ')
    
    old_Name = Path(pth/dirs[int(y) - 1])
    new_Name = input('New name: ')
    new_Name = Path(pth/new_Name)
    
    shutil.move(old_Name, new_Name)
    
    pth = new_Name
    dirs = os.listdir(pth)
    
    return pth, dirs




if __name__ == '__main__':
    main()