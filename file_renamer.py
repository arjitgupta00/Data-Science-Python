import os


def renamer():
    i = 1
    # path = 'C:\\Users\\username\\Desktop\\img\\'
    # Enter path name here to the image folder in the above given format
    for filename in os.listdir(path):
        names = f'pic - {i}.jpg'
        src = path+filename
        dest = path+names
        os.rename(src, dest)
        i = i+1


if __name__ == "__main__":
    renamer()
