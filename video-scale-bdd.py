
import os


splits = ['train', 'val', 'test']

DATA_ROOT = '/home/alpargun/Desktop/bdd-alp/'

output_path = '/home/alpargun/Desktop/bdd-256/'

if not os.path.exists(output_path):
    os.mkdir(output_path)

# Repeat for each data split
for split in splits:

    print('Split: ', split)
    if not os.path.exists(output_path + split):
        os.mkdir(output_path + split)

    # Get lists
    list_path = DATA_ROOT + split + '.csv'

    file_list = []

    f = open(list_path, 'r')

    for line in f:
        rows = line.split()
        fname = rows[0]
        file_list.append(fname)

    f.close()

    for file_name in file_list:
        print(file_name)
        if (file_name.endswith(".mov")): #or .avi, .mpeg, whatever.
            
            name_set  = file_name.split('/')
            video_name = name_set[-1]
            part_name = name_set[-2]

            output_folder = output_path + split + '/' + part_name
            if os.path.isdir(output_folder) is False:
                try:
                    os.mkdir(output_folder)
                except:
                    print(output_folder, ' exists')

            out_name = output_folder + '/' + video_name

            command = f"ffmpeg  -loglevel panic -i {file_name} -filter:v scale=\"trunc(oh*a/2)*2:256\" -q:v 1 -c:a copy {out_name}"
            os.system(command=command)
                

        else:
            print('error')
            continue