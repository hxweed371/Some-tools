import os
import shutil

folder_path = r"D:\QuangLinha\Learn\python\OrderFile"

folder_root = "\\File"
folder_root_name = ["HSBB","MVNAH","TCML","HSTB","DBTD","HSLS","CDHH","NCC","TKN"]
folder_root_level2_name = ["BQ","MV","BM","VX","TP","QBI","DV","HSP","QBA","XM","YM"]

folder_root_orderby = "\\CSDL_SOHOA_TBHG"
renamed_folders = []
move_files_pdf = []

folder_name_list = [
    ('BacQuang', 'BQ'),
    ('QuanBa', 'QBA'),
    ('TP HaGiang', 'TP'),
    ('ViXuyen', 'VX'),
    ('YenMinh', 'YM'),
    ('BacMe', 'BM'),
    ('QuangBinh', 'QBI'),
    ('HoangSuPhi', 'HSP'),
    ('XinMan', 'XM'),
    ('DongVan', 'DV'),
    ('MeoVac', 'MV'),
]
target_folders = [
     "D:", "QuangLinha", "Learn", "python", "OrderFile", "CSDL_SOHOA_TBHG",
     "HSBB","MVNAH","TCML","HSTB","DBTD","HSLS","CDHH","NCC","TKN",
     "BQ","MV","BM","VX","TP","QBI","DV","HSP","QBA","XM","YM"
]
output_paths = []
def main():
    
    add_folder_name(folder_path, folder_root_name, folder_root_level2_name, folder_root)
    
    print_all_folders(folder_path+folder_root_orderby, folder_name_list, renamed_folders)
    rename_folders_in_list(renamed_folders)
    '''
        print_all_pdf_files_v2(folder_path+folder_root_orderby, folder_name_list, move_files_pdf)
        output_paths = process_paths(move_files_pdf, target_folders)
        add_folder_name(folder_path, folder_root_name, folder_root_level2_name, folder_root_orderby)
        move_files(output_paths)
    '''
    
    '''
        print_all_pdf_files_v2(folder_path+folder_root_orderby, folder_name_list, move_files_pdf)
        out_rename_paths = rename_paths(move_files_pdf)
        move_files(out_rename_paths)
    '''
    
    print_all_pdf_files_v2(folder_path+folder_root, folder_name_list, move_files_pdf)
    for x in move_files_pdf:
        print(x)
    print("OK")

def add_folder_name(folder_path, folder_root_name, folder_root_level2_name, folder_root):
    root = folder_path + folder_root
    if not os.path.exists(root):
        os.mkdir(root)
        
    for x in folder_root_name:
     root_x =root+"\\"+x
     if not os.path.exists(root_x):
        os.mkdir(root_x)
     for x2 in folder_root_level2_name:
         root_x2 =root_x+"\\"+x2
         if not os.path.exists(root_x2):
            os.mkdir(root_x2)

def print_all_folders(root_path, folder_name_list, renamed_folders):
    
    for item in os.listdir(root_path):
       
        item_path = os.path.join(root_path, item)
        if os.path.isdir(item_path):
            rename_folders(item_path, folder_name_list, renamed_folders)
            print_all_folders(item_path, folder_name_list, renamed_folders)

def rename_folders(directory_path, folder_name_list, renamed_folders):
    
    parent_directory = os.path.dirname(directory_path)
    for old_name, new_name in folder_name_list:
        old_path = os.path.join(parent_directory, old_name)
        new_path = os.path.join(parent_directory, new_name)
        if os.path.exists(old_path):
            renamed_folders.append((old_path, new_path))
            
def rename_folders_in_list(renamed_folders):
    for old_path, new_path in renamed_folders:
        if os.path.exists(old_path):
            os.rename(old_path, new_path) 
      
def print_all_pdf_files_v2(root_path, folder_name_list, move_files_pdf):
    for item in os.listdir(root_path):
        item_path = os.path.join(root_path, item)
        if os.path.isdir(item_path):
            print_all_pdf_files_v2(item_path, folder_name_list, move_files_pdf)
        elif item.lower().endswith(".pdf"):
            move_files_pdf.append((item_path))
            
def process_paths(input_paths, target_folders):
    output_paths = []
    for path in input_paths:
        dir_path, file_name = os.path.split(path)
        dir_names = dir_path.split(os.sep)
        filtered_dirs = [dir_name for dir_name in dir_names if dir_name in target_folders]
        
        # Ensure the drive letter is followed by a backslash
        new_dir_path = os.path.join(filtered_dirs[0] + os.sep if len(filtered_dirs) > 0 else "", *filtered_dirs[1:])
        new_path = os.path.join(new_dir_path, file_name)
        output_paths.append((path, new_path))
        
    return output_paths

def rename_paths(file_paths):
    renamed_paths = []
    for path in file_paths:
        new_path = path.replace("CSDL_SOHOA_TBHG", "File")
        renamed_paths.append((path, new_path))
    return renamed_paths

def move_files(output_paths):
    for old_path, new_path in output_paths:
        dir_path, file_name = os.path.split(new_path)
        if os.path.exists(old_path) and os.path.exists(dir_path) and old_path != new_path:
            ##shutil.move(old_path, new_path)
            print(f"Moved {old_path} to {new_path}")
             
if __name__ == "__main__":
    main()