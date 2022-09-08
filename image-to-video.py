#%%

import cv2
import numpy as np
import glob
import os
import pandas as pd

ROOT = '/home/alpargun/Desktop/lgsvl_data_collection/svl_videos/'
TARGET = '/home/alpargun/Desktop/lgsvl-videos/'


#%%

if not os.path.exists(TARGET):
    os.mkdir(TARGET)

#%%

# Iterate through collections: curve, straight and temp
for collection in os.listdir(ROOT):

    if not os.path.exists(TARGET + collection):
        os.mkdir(TARGET + collection)

    f = os.path.join(ROOT, collection)
    print(f)

    path_dfs = os.path.join(f, 'data_frames/')
    
    # Iterate through data_frames
    for path_df in os.listdir(path_dfs):
        #print(path_df)

        # Read csv and iterate
        df = pd.read_csv(os.path.join(path_dfs, path_df))
        img_array = []

        for index, row in df.iterrows():
            path_img = row[0].replace('/home/mohammed/kastouri/data_collection/svl_videos/', '')
            #print(path_img)

            img = cv2.imread(os.path.join(ROOT, path_img))
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)

        # Save as video
        video_name = path_df.replace('csv', '') + 'mp4'
        video_path = os.path.join(TARGET, collection, video_name)

        out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 10, size)
    
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()

print('complete')




#%%
