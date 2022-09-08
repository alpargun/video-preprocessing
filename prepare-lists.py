
# Iterate through splits and generate the train, validation and test set lists

#%%

import csv
import os


ROOT = '/home/alpargun/Desktop/bdd100k/videos/'

splits = ['train', 'val', 'test']

for split in splits:

    file_name = split + '.csv'
    with open(file_name, 'w') as f:

        writer = csv.writer(f)

        for subdir, dirs, files in os.walk(ROOT + split):
            for file in files:
                print(os.path.join(subdir, file))

                writer.writerow([os.path.join(subdir, file)])

print('completed')

#%%
