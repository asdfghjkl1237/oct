from packages import *

framerate = 44100
chunk = 1024
channels = 1
bit_duration = 0.001

path_folder_oct = os.path.abspath(__file__)
path_folder_octavia_core = os.path.dirname(path_folder_oct)

path_folder__test_sound_listen = os.path.join(path_folder_octavia_core, 'storage', 'test', 'sound_listen')
path_folder__test_sound_gen = os.path.join(path_folder_octavia_core, 'storage', 'test', 'sound_gen')
