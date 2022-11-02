from sys import argv
from pathlib import Path
import shutil

if __name__=='__main__':
    # if len(argv)!=1:
    #     exit()
    dirc=Path(argv[1])
    #dirc=Path("./test")
    files=[]
    for file in dirc.iterdir():
        if file.is_dir():
            continue
        files.append(file)
    files.sort(key=lambda x:int(x.stem))
    for i in range(1,len(files)):
        shutil.copyfile(files[i],files[i-1])
    files[-1].unlink()