from pathlib import Path
import PIL.Image as Image

DATA_FOLDER = '/home/prateek/Downloads/workshop-hpc-data/NFFA images sampled'
TARGET_FOLDER = '/home/prateek/Downloads/workshop-hpc-data/NFFA images sampled cropped'

# Create target folder if it does not exist
Path(TARGET_FOLDER).mkdir(parents=True, exist_ok=True)

# get the list of all files in the source folder
files = list(Path(DATA_FOLDER).rglob('*.jpg'))
print(len(files), 'total files found')

# get the dimension of the first image
img = Image.open(files[0])
print('Dimensions of the first image:', img.size)

# define the cropping function
def crop_image(file, data_folder, target_folder):
    img = Image.open(file)
    img = img.crop((0, 0, 1024, 600))
    # save the cropped image in the target folder matching the subfolder structure
    save_to_path = str(file).replace(data_folder, target_folder)
    # make sure the subfolder exists
    Path(save_to_path).parent.mkdir(parents=True, exist_ok=True)
    img.save(save_to_path)
    print('saved ' + save_to_path)

# crop all images
for file in files:
    crop_image(file, DATA_FOLDER, TARGET_FOLDER)