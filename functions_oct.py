from packages import *
from functions import *

def get_last_file_path_with_recording_id(folder_path, recording_id = None, file_format = 'wav', is_return_full_path = False):
    file_names_list = os.listdir(folder_path)
    file_names_list_format = [file_name for file_name in file_names_list if file_name.split('.')[-1]]

    f_get_recording_id_from_full_name = lambda x: x.split('__')[-1].split('.')[0]

    if not(recording_id):
        list_recording_id = [f_get_recording_id_from_full_name(file_name) for file_name in file_names_list_format]
        list_recording_id_checked = []
        for recording_id_ in list_recording_id:
            try:
                list_recording_id_checked.append(int(recording_id_.replace('_', '|')))
            except:
                pass
        recording_id = max(list_recording_id_checked)

    file_names_list_format.sort()
    full_file_name = [file_name for file_name in file_names_list_format if int(f_get_recording_id_from_full_name(file_name)) == recording_id][-1]

    if is_return_full_path:
        return os.path.join(os.path.abspath(folder_path), full_file_name)
    else:
        return full_file_name
