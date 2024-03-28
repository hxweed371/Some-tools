import os

folder_path = r"D:\\QuangLinha\\Learn\\python\\OrderFile"

folder_root = "\\File"
folder_root_name = ["HSBB","MVNAH","TCML","HSTB","DBTD","HSLS","CDHH","NCC","TKN"]
folder_root_level2_name = ["BQ","MV","BM","VX","TP","QBI","DV","HSP","QBA","XM","YM"]

folder_root_orderby = "\\CSDL_SOHOA_TBHG"

renamed_folders = []
folder_name_list = [
    ('NCC', 'NCC2'),
    ('BacQuang', 'BQ'),
]


def main():
    
    add_folder_name(folder_path, folder_root_name, folder_root_level2_name, folder_root)
    print_all_folders(folder_path+folder_root_orderby, folder_name_list, renamed_folders)
    print("List of old and new paths:")
    for old_path, new_path in renamed_folders:
        print(f"Old path: {old_path}")
        print(f"New path: {new_path}")
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
        os.rename(old_path, new_path)
              
if __name__ == "__main__":
    main()