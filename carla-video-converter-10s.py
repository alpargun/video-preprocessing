#%%

import cv2
import numpy as np
import glob
import os
import pandas as pd

ROOT = '/home/shawanmohammed/Desktop/carla-for-drl/sample_data/no-terminate-no-frameskip-high-quality-2/'
TARGET = '/home/shawanmohammed/Desktop/carla-videos/no-terminate_10s/'


#%%

if not os.path.exists(TARGET):
    os.makedirs(TARGET)

#%%

COLLECTIONS = ['rgb']

# Iterate through training and test splits
for split in os.listdir(ROOT):
    print('dir: ', split)
    if not os.path.exists(TARGET + split):
        os.makedirs(TARGET + split)

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

                    # TODO
                    # add code here

                    # 300 frames make 10sec
                    num_vids = len(list_imgs) // 300
                    num_remainder = len(list_imgs) % 300

                    # Drop remainder imgs from the beginning since there is waiting during
                    # initialization
                    remaining_imgs = list_imgs[num_remainder:] 

                    # Iterate through images

                    img_array = []

                    for idx, img in enumerate(remaining_imgs):
                        #print(img)
                        
                        path_img = os.path.join(path_collection, img)
                        
                        img = cv2.imread(os.path.join(ROOT, path_img))
                        height, width, layers = img.shape
                        size = (width,height)
                        img_array.append(img)


                        if idx % 300 == 0 and idx > 0:

                            # Save as video
                            video_name = collection + str(idx // 300) + '.mp4'
                            video_dir = os.path.join(TARGET, split, route)

                            if not os.path.exists(video_dir):
                                os.mkdir(video_dir)

                            video_path = os.path.join(video_dir, video_name)
                            print('video path: ', video_path)
                            out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30, size)
                        
                            for i in range(len(img_array)):
                                out.write(img_array[i])
                            out.release()
                            print('video created: ')

                            img_array = []

      

print('complete')


