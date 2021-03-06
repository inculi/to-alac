import os
import sys
from shutil import copyfile

def convert(filename, filetype):
    if "." not in filetype:
        filetype = "." + filetype
    ffilename = filename.rsplit(filetype)[0]
    if not "\._" in ffilename:
        if not os.path.isfile(os.curdir + "\\alac\\" + ffilename + ".m4a"):
            print "Converting " + ffilename + filetype
            os.system("ffmpeg -i \"" + ffilename + filetype + "\" -c:a alac -vf \"scale=trunc(iw/2)*2:trunc(ih/2)*2\" \"" + os.curdir + "\\alac\\" + ffilename + ".m4a\" -loglevel quiet")
            print "Done"
        else:
            print ffilename + ".m4a exists. Skipping."

def getFiles(filetype):
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(filetype)]:
            if not os.path.exists(os.curdir  + "\\alac\\" + dirpath):
                os.makedirs(os.curdir + "\\alac\\" + dirpath)
            convert(os.path.join(dirpath, filename), filetype)

def copyFiles(filetype):
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if not f.endswith(filetype)]:
            if filename != "alac.py":
                if not os.path.exists(os.curdir  + "\\alac\\" + dirpath):
                    os.makedirs(os.curdir + "\\alac\\" + dirpath)
                if dirpath == ".":
                    dirpath = ""
                print "Found file: " + os.path.join(dirpath, filename)
                print "Copying " + filename
                copyfile(os.path.join(dirpath, filename), os.path.join(os.curdir + "\\alac\\" + dirpath, filename))
                print "Done"
    getFiles(filetype)

if not os.path.exists(os.curdir + "\\alac\\"):
    os.makedirs(os.curdir + "\\alac\\")
if(len(sys.argv) == 2):
    copyFiles(sys.argv[1])
elif(len(sys.argv) < 2):
    print "No filetype found. Please specify filetype to convert."
    print "Example: python alac.py .flac"
elif(len(sys.argv) > 2):
    print "Too many arguments. Only argument needed is filetype to convert."
    print "Example: python alac.py .flac"
