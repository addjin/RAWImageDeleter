import os
from send2trash import send2trash
import sys

is_verbose = True

def customprint(message):
    if is_verbose: print(message)

inputDir = ''

if len(sys.argv) > 1:
    inputDir = sys.argv[1]

if os.path.exists(inputDir):
    currentdir = inputDir
    customprint('Set \'{0}\' as the target directory.'.format(currentdir))
else:
    currentdir = os.getcwd()
    if inputDir == '':
        message = 'Set \'{0}\' as the target directory.'.format(currentdir)
    else:
        message = '\'{0}\' is not a valid directory. Setting \'{1}\' as the target directory.'.format(inputDir, currentdir)    
    customprint(message)

neffiles = [f for f in os.listdir(currentdir) if os.path.isfile(os.path.join(currentdir, f)) and os.path.splitext(f)[1].lower() == '.nef']

if (len(neffiles) == 0):
    customprint('No raw images in the directory. Terminating program.')
    exit()

jpegfiles = [os.path.splitext(f)[0] for f in os.listdir(currentdir) if os.path.isfile(os.path.join(currentdir, f)) and os.path.splitext(f)[1].lower() in ['.jpg', '.jpeg']]

if(len(jpegfiles) == 0):
    customprint('There aren\'t any jpeg files in the directory. All the raw images will be deleted. Continue? (Y/N)')
    inp = input()
    if inp.lower() == 'n':
        exit()

deleted_files_count = 0

for neffile in neffiles:
    if os.path.splitext(neffile)[0]  not in jpegfiles:
        send2trash(os.path.join(currentdir, neffile))
        deleted_files_count += 1
        customprint('{0} deleted.'.format(neffile))

customprint('Task complete.{0} files deleted.'.format(str(deleted_files_count)))