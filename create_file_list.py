import os

for root, dirs, filenames in os.walk('/home/ec2-user/dataset/SiW_release/Train'):
    for file in filenames:
        if file.endswith('.mov'):
            path = os.path.join(root, file)

            with open('train.csv', 'a') as fwriter:
                fwriter.write(file + ' ' + str(path.split('/')[-3]))

for root, dirs, filenames in os.walk('/home/ec2-user/dataset/SiW_release/Test'):
    for file in filenames:
        if file.endswith('.mov'):
            path = os.path.join(root, file)

            with open('test.csv', 'a') as fwriter:
                fwriter.write(file + ' ' + str(path.split('/')[-3]))
