
import os


path = '/home/alp/Desktop/abseiling/'

for filename in os.listdir(path):
    print(filename)
    if (filename.endswith(".mp4")): #or .avi, .mpeg, whatever.
        #os.system(f"ffmpeg -i {path + filename} -f image2 -vf fps=fps=1 output%d.png")

        inname = '"%s"' % filename
        outname = f'rescaled/{filename}'
        #print(outname)
        command = f"ffmpeg  -loglevel panic -i {path + filename} -filter:v scale=\"trunc(oh*a/2)*2:256\" -q:v 1 -c:a copy {outname}"
        os.system(command=command)
           

    else:
        continue


