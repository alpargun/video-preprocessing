#%%

import cv2
import numpy as np
import glob
import os
import pandas as pd

ROOT = '/home/shawanmohammed/Desktop/carla-for-drl/sample_data/no-terminate-no-frameskip/'
TARGET = '/home/shawanmohammed/Desktop/carla-videos/'


#%%

if not os.path.exists(TARGET):
    os.mkdir(TARGET)

#%%

COLLECTIONS = ['rgb', 'rgb_right', 'rgb_left']

# Iterate through training and test splits
for split in os.listdir(ROOT):
    print('dir: ', split)
    if not os.path.exists(TARGET + split):
        os.mkdir(TARGET + split)

    path_split = os.path.join(ROOT, split)
    print(path_split)

    # Iterate through route directories
    for route in os.listdir(path_split):
        path_route = os.path.join(path_split, route)
        if os.path.isdir(path_route):
            print('route: ', route)

            # Iterate through collection directories
            for collection in os.listdir(path_route):

                if collection in COLLECTIONS:
                    print('collection: ', collection)
                    path_collection = os.path.join(path_route, collection)

                    # Get the list of images
                    list_imgs = os.listdir(path_collection)

                    # Sort images by the number
                    list_imgs.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

                    # Iterate through images
                    img_array = []

                    for img in list_imgs:
                        #print(img)

                        path_img = os.path.join(path_collection, img)
                        
                        img = cv2.imread(os.path.join(ROOT, path_img))
                        height, width, layers = img.shape
                        size = (width,height)
                        img_array.append(img)
                    print('img array complete')

                    # Save as video
                    video_name = collection + '.mp4'
                    video_dir = os.path.join(TARGET, split, route)

                    if not os.path.exists(video_dir):
                        os.mkdir(video_dir)

                    video_path = os.path.join(video_dir, video_name)
                    print('video path: ', video_path)
                    out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30, size)
                
                    for i in range(len(img_array)):
                        out.write(img_array[i])
                    out.release()
                    print('video created')
      

print('complete')





#%% Count number of imgs

import os

COLLECTIONS = ['rgb', 'rgb_right', 'rgb_left']

ROOT = '/home/shawanmohammed/Desktop/carla-for-drl/sample_data/no-terminate-no-frameskip/'

count = 0

min_imgs = 999999999
max_imgs = 0

for dir, subdir, files in os.walk(ROOT):
    #print('dir: ', dir)
    #print('subdir: ', subdir)
    #print(files)
    
    base_name = os.path.basename(dir)

    if base_name in COLLECTIONS:
        count = count + len(files)
        if len(files) < min_imgs:
            min_imgs = len(files)
            min_path = dir
        if len(files) > max_imgs:
            max_imgs = len(files)
            max_path = dir

print('img count: ', count)
print('min number of imgs in a collection: ', min_imgs, ' in path: ', min_path)
print('max number of imgs in a collection: ', max_imgs, ' in path: ', max_path)

# %%
