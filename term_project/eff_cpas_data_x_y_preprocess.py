import os
import numpy as np
from PIL import Image
from tensorflow.keras.utils import to_categorical

term_project_path = os.path.join('C:\\', 'Users', 'user', 'Desktop', 'algorithm', 'term_project')
train_datapath = os.path.join(term_project_path, 'train_image')
test_datapath = os.path.join(term_project_path, 'test_image')
datapath_list = [train_datapath, test_datapath]
save_path = os.path.join(term_project_path, 'eff_cpas_dataset')
if __name__ == '__main__':
    print('----data_x_y_preprocess init----')
    img_row, img_col = 28, 28
    num_class = 10

    for datapath in datapath_list:
        data_x = np.zeros((img_row, img_col)).reshape(1, img_row, img_col).astype('float32')
        pic_counter = 0
        data_y = []
        for root, dirs, files in os.walk(datapath):
            for f in files:
                data_y.append(int(root.split('\\')[-1]))
                fullpath = os.path.join(root, f)
                img = Image.open(fullpath)
                img = (np.array(img)/255).reshape(1, img_row, img_col).astype('float32') #nomalize
                #data_x = np.vstack((data_x, img))
                data_x = np.concatenate((data_x, img), axis=0)
                pic_counter += 1
        data_x = np.delete(data_x, 0, axis=0)
        data_x = data_x.reshape(pic_counter, img_row, img_col, 1)
        data_y = to_categorical(data_y, num_class)
        print(data_x.shape, data_y.shape)

        if datapath == train_datapath:
            np.save(os.path.join(save_path, 'train_data_x.npy'), data_x)
            np.save(os.path.join(save_path, 'train_data_y.npy'), data_y)
            print('train data save ok!')
        elif datapath == test_datapath:
            np.save(os.path.join(save_path, 'test_data_x.npy'), data_x)
            np.save(os.path.join(save_path, 'test_data_y.npy'), data_y)
            print('test data save ok!')