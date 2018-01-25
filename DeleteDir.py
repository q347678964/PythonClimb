import shutil
import os
OutputDir = 'output'
if os.path.exists(OutputDir) == True:
    shutil.rmtree(OutputDir)
    
for i in range(1000):
    ExitDir = OutputDir + '%d'%i
    if os.path.exists(ExitDir) == True:
        shutil.rmtree(ExitDir)
print('Delete Over')
