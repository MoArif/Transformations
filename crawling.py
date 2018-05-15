#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 18:37:23 2018

@author: mofassir
"""
import pandas as pd
import numpy as np
import glob


def load_img(url):
    img = cv2.imread(url,1)
    return img
def read_dir(dirc):
    folder_dir = glob.glob(dirc)
    return folder_dir

def get_name_imgs_first_folder(folder_dir):
    imgs= glob.glob(folder_dir+'*.jpg')
    return imgs

def check_name(string):
    string = string.split('-')
    if 'Beschädigung' in string:
        return True
    else:
        return False

def best (string):
    img_list = []
    sp_string = string.split('/')[1:]
    img_name_temp = sp_string[-1]
    img_name =  img_name_temp.split('_')
    #print(img_name[1],check_name(img_name[1]))
    return check_name(img_name[1])

if __name__ == "__main__":
    print(sys.argv)
    #folders = sys.argv[1]+'*/'
    fts = '/home/mofassir/vwfs_test/new_data/'
    folders = '/home/mofassir/vwfs_test/small/img/*/'
    tags = ['RC','AF','ROT']
    folder_dir = read_dir(folders)
    #img_list = get_name_imgs_first_folder(folder_dir)
    fin_tuple = (0,0,0)
    x=0
    for j in range(len(folder_dir)):
        img_list = get_name_imgs_first_folder(folder_dir[j])
        for x in range (len(img_list)):
            if best(img_list[x]):
                img = load_img(img_list[x])

#def getCSV_list(dir):
#    dir = dir+'*/*.csv'
#    csv_files = glob.glob(dir)
#    return csv_files
#
#def loadCSV_file(file):
#    df = pd.read_csv(file,sep='|')
#    return df
#if __name__ == '__main__':
#    dir = '/home/mofassir/vwfs_test/small/img/'
#    csv_files = getCSV_list(dir)
#    sample = loadCSV_file(csv_files[0])
#    x = sample.as_matrix()
#    for k in range(len(x)):
#        if x[k][1][0] == 'B':
#            print(x[k][1])
#
##    
##    for k,v in x.items():
##        if k == 'heading':
##            for k in range(len(v)):
##                if v[k][0] == 'B':
##                    print(v[k])