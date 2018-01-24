import shutil
import os
OutputDir = 'output'
for i in range(1000):
    ExitDir = OutputDir + '%d'%i
    if os.path.exists(ExitDir) == True:
        shutil.rmtree(ExitDir)
print('Delete Over')
