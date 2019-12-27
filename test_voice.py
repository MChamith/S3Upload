import json
import os
from upload_data import upload_file
import requests

DIR = '/home/ubuntu/librispeech/test-clean'
enroll_url = 'http://ab6040ee8989c11e98cff0a75697d87c-1513868072.us-east-1.elb.amazonaws.com/v1.0/voice/enroll_voice/'
verify_url = 'http://ab6040ee8989c11e98cff0a75697d87c-1513868072.us-east-1.elb.amazonaws.com/v1.0/voice/verify_voice/'

parent_dirs = [os.path.join(DIR, subDir) for subDir in os.listdir(DIR) if os.path.isdir(os.path.join(DIR, subDir))]


def enroll():
    for direct in parent_dirs:
        # print(direct)
        sub_parent_dirs = [os.path.join(direct, subsubDir) for subsubDir in os.listdir(direct)]
        # print(sub_parent_dirs)
        for root, dirs, filenames in os.walk(sub_parent_dirs[0]):
            count = 0
            for file in filenames:
                if count == 3:
                    break
                if file.endswith('.m4a'):
                    path = os.path.join(root, file)
                    count += 1
                    speakerid = path.split('/')[-3]
                    print(speakerid)
                    upload_file(path, 'ustlkcomdev-test-biometric',
                                'meetsid/' + str(speakerid) + '/voice/voice.m4a')
                    data = {"file_path": 'meetsid/' + str(speakerid) + '/voice/voice.m4a', "wallet_id": str(speakerid)}
                    response = requests.post(enroll_url,
                                             headers={'content-type': 'application/json'},
                                             data=json.dumps(data))
                    print(response.text)


def verify():
    with open('libri_test_clean.csv', 'a') as writer:
        writer.write('verify,enroll,status,score,file\n')
    speakerids = [i.split('/')[-1] for i in parent_dirs]
    for direct in parent_dirs:
        # print(direct)
        sub_parent_dirs = [os.path.join(direct, subsubDir) for subsubDir in os.listdir(direct)]
        # print(sub_parent_dirs)
        for spk_dir in sub_parent_dirs:
            for root, dirs, filenames in os.walk(spk_dir):
                for file in filenames:
                    print(file)
                    if file.endswith('.m4a'):
                        path = os.path.join(root, file)

                        speakerid = path.split('/')[-3]
                        print(speakerid)
                        upload_file(path, 'ustlkcomdev-test-biometric',
                                    'meetsid/' + str(speakerid) + '/verify/' + str(file))
                        for spkr in speakerids:
                            data = {"file_path": 'meetsid/' + str(speakerid) + '/verify/' + str(file),
                                    "wallet_id": str(spkr)}
                            response = requests.post(verify_url,
                                                     headers={'content-type': 'application/json'},
                                                     data=json.dumps(data))
                            result = response.json()
                            with open('libri_test_clean.csv', 'a') as writer:
                                writer.write(
                                    str(speakerid) + ',' + str(spkr) + ',' + result['matching'] + ',' + str(
                                        result['score']) + ',' + str(path)+'\n')
                            print(response.json())


verify()
