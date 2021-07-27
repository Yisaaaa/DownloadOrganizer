import os
import shutil

src = '/storage/emulated/0/Download'

def main():
    for file in os.listdir(src):
        if file.endswith('pdf'):
            directoryPath = os.path.join(src, 'Pdf')
            if not os.path.exists(directoryPath):
                os.mkdir(directoryPath)
                print(directoryPath, 'created')
            shutil.move(os.path.join(src, file), directoryPath)
            print(file, 'moved')
        elif file.endswith('jpg') or file.endswith('png'):
            directoryPath = os.path.join(src, 'Images')
            if not os.path.exists(directoryPath):
                os.mkdir(directoryPath)
                print(directoryPath, 'created')
            shutil.move(os.path.join(src, file), directoryPath)
            print(file, 'moved')

if __name__ == '__main__':
    print('Starting...\n')
    main()
    print('\nFinished.')