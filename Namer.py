import os

def rename_images(folder_path, prefix='ai', file_extension='.jpg'):
    files = [f for f in os.listdir(folder_path)] #files = [f for f in os.listdir(folder_path) if f.endswith(file_extension)]
    files.sort()

    for i, filename in enumerate(files):
        new_name = f"{prefix}_{i:05d}{file_extension}"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))


# Example usage
folder_path = 'C:/Users/junse/Downloads/aiTrainingImages/class_ai'
rename_images(folder_path, prefix='ai', file_extension='.jpg')

folder_path = 'C:/Users/junse/Downloads/aiTrainingImages/class_human'
rename_images(folder_path, prefix= 'human', file_extension='.jpg')