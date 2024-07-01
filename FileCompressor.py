import FreeSimpleGUI as sg
import shutil
import os

label1 = sg.Text("Select files to compress")
label2 = sg.Text("Select destination folder")
label3 = sg.Text("Selected Folders")

selected_folder_box = sg.Input(key='selected_folder')
destination_box = sg.Input(key='destination')

user_selected_folders = []

folder_list = sg.Listbox(user_selected_folders, enable_events=True, size=(50,10), expand_x=True, key='folder_clicked')


choose_files_button = sg.FolderBrowse("Browse")
choose_destination_button = sg.FolderBrowse("Browse")
compress_button = sg.Button("Compress")
add_folder_button = sg.Button('Add', key='add_folder_button')
remove_folder_button = sg.Button("Remove", key="Remove")

window = sg.Window("File Zipper", layout=[[label1, selected_folder_box, choose_files_button, add_folder_button],
                                          [label2, destination_box, choose_destination_button],
                                          [label3, remove_folder_button],
                                          [folder_list],
                                          [compress_button]])

while True:

    action, folders = window.read()
    print(action)
    print(folders)
    selected_folder = folders["selected_folder"]
    destination = folders["destination"]

    match action:
        case 'Compress':

            temp_folder = './temp' 

            for folder in user_selected_folders:
                # source_path = os.path.join(folder) 
                # Write function that will get the last folder name in a filepath.
                shutil.copytree(folder, temp_folder, dirs_exist_ok=True)
            shutil.make_archive(destination + '/archive', 'zip', temp_folder)
            shutil.rmtree(temp_folder)
    
        case 'add_folder_button':
            user_selected_folders.append(folders['selected_folder'])
            folder_list.update(user_selected_folders)

        case sg.WIN_CLOSED:
            break

        case "Remove":
            print(folders["folder_clicked"])
            user_selected_folders.remove(folders["folder_clicked"][0])
            folder_list.update(user_selected_folders)
        
    
    
window.close()