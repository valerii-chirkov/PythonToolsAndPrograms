import os
from PIL import Image

basedir = '/Users/valerii/Downloads/Transmetropolitan'
folders_list = sorted(os.path.join(basedir, folder) for folder in os.listdir(basedir) if 'Trans' in folder)
images = []
for folder in folders_list:
    list_of_imgs = []
    for fn in os.listdir(folder):
        if 'Trans' not in fn:
            continue
        list_of_imgs.append(os.path.join(basedir, folder, fn))
    images.append(sorted(list_of_imgs))

all_imgs = []
for vol in images:
    for img in vol:
        all_imgs.append(img)

# print(sorted(all_imgs))
images = [Image.open(f) for f in sorted(all_imgs)]
pdf_path = "/Users/valerii/Downloads/TransmetropolitanFull"
images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
