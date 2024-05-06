import os
import shutil
import argparse

def copy_files_recursively(src_dir, dest_dir):
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        
        if os.path.isdir(src_path):
            # Рекурсивний виклик функції для вкладених директорій
            copy_files_recursively(src_path, dest_dir)
        else:
            # Копіювання файлу до відповідної піддиректорії
            file_extension = os.path.splitext(item)[1][1:]
            dest_subdir = os.path.join(dest_dir, file_extension)
            
            if not os.path.exists(dest_subdir):
                os.makedirs(dest_subdir)
            
            dest_path = os.path.join(dest_subdir, item)
            shutil.copy2(src_path, dest_path)

def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description='Copy files recursively and sort by file extension.')
    parser.add_argument('src_dir', help='Source directory path')
    parser.add_argument('dest_dir', nargs='?', default='dist', help='Destination directory path (default: dist)')
    args = parser.parse_args()
    
    src_dir = args.src_dir
    dest_dir = args.dest_dir
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    try:
        copy_files_recursively(src_dir, dest_dir)
        print('Files copied and sorted successfully.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

if __name__ == '__main__':
    main()