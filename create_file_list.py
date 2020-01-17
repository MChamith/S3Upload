import os

for root, dirs , filenames in os.walk('/home/ubuntu/librispeech/LibriSpeech/test-other'):

    for file in filenames:
        if file.endswith('.flac'):
            file_path = os.path.join(root, file)
            file_name = file_path.split('.flac')[0]
            save_file_name = file_name +'.m4a'
            os.system('ffmpeg -i {0} {1}'. format(file_path, save_file_name))