import os
import shutil

folder_path = r"D:\\QuangLinh\\Hoc\\orderby"

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
     "QuangLinh","Hoc","orderby","CSDL_SOHOA_TBHG",
     "NCC","TKN",
     "BQ","MV","BM","VX","TP","QBI","DV","HSP","QBA","XM","YM"
]
output_paths = []
def main():
    
    add_folder_name(folder_path, folder_root, folder_root_name, folder_root_level2_name)
    print("OK")

def add_folder_name(folder_path, folder_root, folder_root_name, folder_root_level2_name):
    root = folder_path + folder_root
    if not os.path.exists(root):
        os.mkdir(root)
    print(root)
    print(folder_path)
    print(folder_root_name)
    print(folder_root_level2_name)
    

             
if __name__ == "__main__":
    main()