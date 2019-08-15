import numpy as np
import pandas as pd
import random
import os

from PIL import Image
import rawpy
import exifread
import image_utils

from datetime import datetime

photo_prefix = 'g:/My Drive/Photo_Backup/' #windows
#photo_prefix = '/g/My\ Drive/Photo_Backup/' #unix

df_path_pred = pd.read_csv('kmeans4_resnet50_res.csv')

### Add some masks to limit photos ###
portland_mask = df_path_pred['path'].str.contains('Portland')
nyc_mask = df_path_pred['path'].str.contains('NYC_NYE')

#mask_df = portland_mask | nyc_mask
mask_df = portland_mask 
######################################

df_path_pred = df_path_pred[mask_df]

print('df_path_pred')
print(df_path_pred)


print("df_path_pred['0_y'].unique()")
print(df_path_pred['0_y'].unique())

raw_img_types = ['nef', 'dng']
reg_img_types = ['jpg', 'jpeg', 'png', 'tif', 'tiff']

def read_raw_img(filename, size=(1024, 1024)):
   raw = rawpy.imread(filename)
   rgb = raw.postprocess()
   im_raw = Image.fromarray(rgb) # Pillow image
   im_raw.thumbnail(size)
   return im_raw

def read_reg_img(filename, size=(1024, 1024)):
   im_reg = Image.open(filename)
   im_reg.thumbnail(size)
   return im_reg

def single_cluster_grab(cluster, num_pics=1):
    idx = df_path_pred[df_path_pred['0_y']==cluster].index
    ridx = random.choices(idx, k=num_pics)
    img_sav = []
    for x in range(num_pics):
        ridx0 = ridx[x]
        path_ridx0 = df_path_pred.loc[ridx0]['path'][2:]
        print(path_ridx0)
        tmp_ext=os.path.basename(path_ridx0).split('.')[-1]
        tmp_ext_lower = tmp_ext.lower()
        israw = tmp_ext_lower in raw_img_types
        isreg = tmp_ext_lower in reg_img_types
        if israw:
            img_pred_test = read_raw_img(photo_prefix+path_ridx0)
        elif isreg:
            img_pred_test = read_reg_img(photo_prefix+path_ridx0)
        img_name = path_ridx0
        img_base64 = image_utils.img_to_base64(img_pred_test)

        #print('img_base64')
        #print(img_base64)

        ### Get Date from Exif Info - RAW Image
        # Open image file for reading (binary mode)
        f = open(photo_prefix+img_name, 'rb')

        # Return Exif tags
        tags = exifread.process_file(f)

        date_raw = tags['EXIF DateTimeOriginal']
        print('date_raw')
        print(date_raw)

        date_object = datetime.strptime(str(date_raw), '%Y:%m:%d %H:%M:%S')
        print('date_object')
        print(date_object)

        img_date = date_object.strftime('%d-%b-%Y')
        print('img_date')
        print(img_date)

        return img_name, img_date, img_base64

def all_cluster_grab(num_clusters=4):
    img_dict = {}
    img_dict['num_images'] = num_clusters
    #print('img_dict')
    #print(img_dict)

    for idx in range(num_clusters):
        tmp_dict = {}
        img_name, img_date, img_base64 = single_cluster_grab(idx)

        tmp_dict['img_name'] = img_name
        tmp_dict['img_date'] = img_date
        tmp_dict['img_base64'] = img_base64

        img_dict[idx] = tmp_dict


    #print('img_dict')
    #print(img_dict)

    return img_dict

if __name__ == "__main__":
    img_name, img_date, img_base64 = single_cluster_grab(1)
    img_dict = all_cluster_grab()
