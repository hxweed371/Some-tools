import os

def print_all_pdf_files_v2(root_path, folder_name_list, move_files_pdf):
    for item in os.listdir(root_path):
        item_path = os.path.join(root_path, item)
        if os.path.isdir(item_path):
            print_all_pdf_files_v2(item_path, folder_name_list, move_files_pdf)
        elif item.lower().endswith(".pdf"):
            file_size = os.path.getsize(item_path)
            move_files_pdf.append((item_path, file_size))
            sql_insert_statement = f"INSERT INTO YourTableName (FileName, FileSize) VALUES ( '{item_path}', {file_size});"
            print(sql_insert_statement)  # Print the path and size of the PDF file

# Example usage
root_path = r"D:\QuangLinha\Learn\python\OrderFile\file"
folder_name_list = []  # Assuming you don't need to use folder_name_list
move_files_pdf = []

print_all_pdf_files_v2(root_path, folder_name_list, move_files_pdf)
