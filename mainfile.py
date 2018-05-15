#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 22:33:54 2018

@author: mofassir
"""
from transformation import imcv2_affine_trans, imcv2_recolor,imcv2_rotate
import cv2
import glob
import sys

def load_img(url):
    img = cv2.imread(url,1)
    return img
def read_dir(dirc):
    folder_dir = glob.glob(dirc)
    return folder_dir

def get_name_imgs_first_folder(folder_dir):
    imgs= glob.glob(folder_dir+'*.jpg')
    return imgs

if __name__ == "__main__":
    print(sys.argv)
    folders = sys.argv[1]+'*/'
    fts = '/home/mofassir/vwfs_test/new_data/'
    #folders = '/home/mofassir/VMFS_TEST/small/img/*/'
    #fts = '/home/mofassir/VMFS_TEST/new_data/'
    tags = ['RC','AF','ROT']
    folder_dir = read_dir(folders)
    #img_list = get_name_imgs_first_folder(folder_dir)
    fin_tuple = (0,0,0)
    x=0
    for j in range(len(folder_dir)):
        img_list = get_name_imgs_first_folder(folder_dir[j])
        for x in range (len(img_list)):
            img = load_img(img_list[x])
            RC_img = cv2.resize(imcv2_recolor(img), (256,256))
            AF_img = cv2.resize(imcv2_affine_trans(img), (256,256))
            ROT_img = cv2.resize(imcv2_rotate(img), (256,256))
            fin_tuple = (RC_img,AF_img,ROT_img)
            folder_id = folder_dir[0].split('/')[len(folder_dir[0].split('/'))-2]
            img_id_temp = img_list[x].split('/')[len(img_list[x].split('/'))-1]
            img_id = img_id_temp.split('_')[-1]
            for k in range(3):
                
                cv2.imwrite(fts+folder_id+'_'+img_id.split('.')[0]+'_'+tags[k]+'.'+img_id.split('.')[1],fin_tuple[k])
                print('img: ',k)