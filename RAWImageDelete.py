""" RawImageDelete

A short python script delete raw image files (.nef) in a directory that doesn't have the .jpeg files with the same name.

Uses send2trash module to delete files and tkinter for prompting message boxes, etc.

"""

import os
from send2trash import send2trash
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

is_verbose = True

def customprint(message):
    """Prints a message to console."""
    if is_verbose: print(message)

def starttk():
    """Starts tk with the tk window hidden."""
    root = tk.Tk()
    root.withdraw()

starttk()

messagebox.showinfo('RawImageDelete', 'Select the target folder')

# filedialog.askdirectory does not return the path in the os format, so using os.path.normpath() to convert
currentdir = os.path.normpath(filedialog.askdirectory())

if not os.path.isdir(currentdir): 
    exit()

neffiles = [f for f in os.listdir(currentdir) if os.path.isfile(os.path.join(currentdir, f)) and os.path.splitext(f)[1].lower() == '.nef']

if (len(neffiles) == 0):
    messagebox.showwarning('Warning', 'No raw images in the directory. Terminating program.')
    exit()

jpegfiles = [os.path.splitext(f)[0] for f in os.listdir(currentdir) if os.path.isfile(os.path.join(currentdir, f)) and os.path.splitext(f)[1].lower() in ['.jpg', '.jpeg']]

if(len(jpegfiles) == 0):
    response = messagebox.askyesno('Confirmation', 'There aren\'t any jpeg files in the directory. All the raw images will be deleted. Continue?')
    if response == False:
        exit()

deleted_files = []

for neffile in neffiles:
    if os.path.splitext(neffile)[0]  not in jpegfiles:
        send2trash(os.path.join(currentdir, neffile))
        deleted_files.append(neffile)

messagebox.showinfo('Task complete', 'Task complete. {0} files deleted.'.format(str(len(deleted_files))))