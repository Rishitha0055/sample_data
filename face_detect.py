import shutil,random,os
path='/home/tgt/Downloads/reg_4'
dest_path='/home/tgt/Downloads/sample_reg1'
filename=random.sample(os.listdir(path),75)
for fname in filename:
    srcpath=os.path.join(path,fname)
    shutil.copy(srcpath,dest_path)
