from packages import *

framerate = 96000 # 44100
chunk = 1024
channels = 1
bit_duration = 0.001
primary_recording_id = 8

path_folder_oct = os.path.dirname(os.path.abspath(__file__))
path_folder_octavia_core = os.path.dirname(path_folder_oct)

path_folder__test_sound_listen = os.path.join(path_folder_octavia_core, 'storage', 'test', 'sound_listen')
path_folder__test_sound_gen = os.path.join(path_folder_octavia_core, 'storage', 'test', 'sound_gen')

del_sample_size_multiplier = 1000

dict_frequencies = {0: 1000, 1: 3000}
dict_frequencies_reverse = {v: k for k, v in dict_frequencies.items()}
