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

def get_imgs_folder(folder_dir):

    imgs= glob.glob(folder_dir+'*.jpg')
    return imgs

def check_name(string):

    string = string.split('-')
    if 'Beschädigung' in string:
        return True
    else:
        return False

def name_parse(string):

    sp_string = string.split('/')[1:]
    img_name_temp = sp_string[-1]
    img_name =  img_name_temp.split('_')
    return check_name(img_name[1]),\
            img_name[1].split('-')[0],\
                img_name[1].split('-')[1],\
                    img_name[3]

if __name__ == "__main__":

    folders = sys.argv[1]+'*/'
    fts = sys.argv[2]
    #fts = '/home/mofassir/vwfs_test/new_data/'
    #folders = '/home/mofassir/vwfs_test/small/img/*/'
    tags = ['RC','AF','ROT']
    folder_dir = read_dir(folders)
    fin_tuple = (0,0,0)
    x=0
    for j in range(len(folder_dir)):
        img_list = get_imgs_folder(folder_dir[j])
        for x in range (len(img_list)):
            if name_parse(img_list[x])[0]:
                bool_test, tag, subid,imgno = name_parse(img_list[x])
                #print('loading:' ,img_list[x])
                img = load_img(img_list[x])
    
                RC_img = cv2.resize(imcv2_recolor(img), (224,224))
                AF_img = cv2.resize(imcv2_affine_trans(img), (224,224))
                ROT_img = cv2.resize(imcv2_rotate(img), (224,224))
                fin_tuple = (RC_img,AF_img,ROT_img)
    
                folder_id = folder_dir[0].split('/')[len(folder_dir[0].split('/'))-2]
                img_id_temp = img_list[x].split('/')[len(img_list[x].split('/'))-1]
                img_id = img_id_temp.split('_')[-1]
                for k in range(3):
                    #print(fts+folder_id+'_'+imgno+'_'+tag+'_'+subid+'_'+tags[k]+'.'+img_id.split('.')[1])
                    cv2.imwrite(fts+folder_id+'_'+imgno+'_'+tag+'_'+subid+'_'+tags[k]+'.'+img_id.split('.')[1],fin_tuple[k])