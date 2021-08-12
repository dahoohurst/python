 # -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:24:01 2021
Used to find duplicate files in a folder on Linux
@author: Dahoo
"""

import os
from collections import Counter

dup_list = []

def listfolder(absPath):
    '''List all folders in one folder with an absolute path'''
    dirs = [d for d in os.listdir(absPath) if os.path.isdir(absPath+'/'+d)]
    return dirs
    
def listfiles(absPath):
    '''List all files in one folder with an absolute path'''
    files = [f for f in os.listdir(absPath) if os.path.isfile(absPath+'/'+f)]
    return files
    
def findDuplicate(filelist):
    '''Print duplicate File list'''
    lower_list = [f.lower() for f in filelist]
    duplicate_list = [item for item, count in Counter(lower_list).items() if count > 1]
    return duplicate_list

def listAllFiles(absFolder, temp_rank = 0):
    '''Process the folder recursively'''
    dirs = listfolder(absFolder)
    print(' '*temp_rank*4+"(Rank "+str(temp_rank)+"): " + absFolder)
    if not dirs:       # means this is a bottom folder
        #print(' '*temp_rank*4+"This folder does not have any subfolders. ")
        filelist = listfiles(absFolder)
        if not filelist:
            print(' '*temp_rank*4+"Empty folder here!")
        else:
            print(' '*temp_rank*4+"No subfolders here, so the file list is: " + ', '.join(filelist))
            files = findDuplicate(filelist)
            if files:
                print(' '*temp_rank*4+'Duplicate Files: '+', '.join(listfiles(absFolder)))
                global dup_list
                dup_list.extend([absFolder+'/'+f for f in filelist])
            print('')
        
    else:
        print(' '*temp_rank*4+"This folder has files: " + ', '.join(listfiles(absFolder)))
        files = findDuplicate(listfiles(absFolder))
        if files:
            print(' '*temp_rank*4+'Duplicate Files: '+', '.join(listfiles(absFolder)))
            global dup_list
            dup_list.extend([absFolder+'/'+f for f in filelist])
        print('')

        print(' '*temp_rank*4+"This folder has subfolders: ["+'],['.join(dirs)+']')
        for d in dirs:
            listAllFiles(os.path.abspath(absFolder)+'/'+d, temp_rank+1)

if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    if args == 1:
        currentAbsPath = os.path.dirname(os.path.abspath(__file__))
        print('Start from the current folder: '+currentAbsPath)
        listAllFiles(currentAbsPath)
        print('Duplicate file list is:\n'+'\n'.join(dup_list))
    elif args > 2:
        print('Error: too many arguments.')
        print('Usage: '+sys.argv[0]+' [The relative/absolute path of a folder]')
    else:
        print('Current working directory is: '+os.getcwd())
        print('Processing the folder: ' + sys.argv[1])
        if os.path.isdir(sys.argv[1]):
            listAllFiles(sys.argv[1])
        else:
            print('The folder does not exist!')
        print('Duplicate file list is:\n'+'\n'.join(dup_list))
        