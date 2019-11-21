import os

print('creating training dataset')
for root, dirs, filenames in os.walk('/home/ec2-user/dataset/SiW_release/Train'):
    for file in filenames:
        if file.endswith('.mov'):
            path = os.path.join(root, file)
            print(file + ' ' + str(path.split('/')[-3]))
            with open('train.csv', 'a') as fwriter:
                fwriter.write(file + ' ' + str(path.split('/')[-3]) + '\n')
print('creating test dataset ')
for root, dirs, filenames in os.walk('/home/ec2-user/dataset/SiW_release/Test'):
    for file in filenames:
        if file.endswith('.mov'):
            path = os.path.join(root, file)
            print(file + ' ' + str(path.split('/')[-3]))
            with open('test.csv', 'a') as fwriter:
                fwriter.write(file + ' ' + str(path.split('/')[-3]) + '\n')
