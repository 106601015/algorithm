import os
import random
import numpy as np
from PIL import Image
#import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.models import save_model, load_model
from tensorflow.keras.applications import ResNet152V2, ResNet50
from tensorflow.keras.utils import to_categorical
from matplotlib import pyplot as plt
import datetime

#x, y(label) preprocess
def data_x_y_preprocess(datapath):
    print('data_x_y_preprocess init')
    img_row, img_col = 28, 28
    data_x = np.zeros((28, 28)).reshape(1, 28, 28)
    pic_counter = 0
    data_y = []
    num_class = 10

    for root, dirs, files in os.walk(datapath):
        for f in files:
            data_y.append(int(root.split('\\')[-1]))
            fullpath = os.path.join(root, f)
            img = Image.open(fullpath)
            img = (np.array(img)/255).reshape(1, 28, 28) #nomalize
            data_x = np.vstack((data_x, img))
            pic_counter += 1
    data_x = np.delete(data_x, 0, axis=0)
    data_x = data_x.reshape(pic_counter, img_row, img_col, 1)
    #data_y = np_utils.to_categorical(data_y, num_class)
    data_y = to_categorical(data_y, num_class)
    return data_x, data_y

# basic version
def create_cnn_model_v1():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.1))

    model.add(Flatten())
    model.add(Dropout(0.1))

    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.25))

    model.add(Dense(10, activation='softmax'))
    model.summary()
    return model

# deeper version
def create_cnn_model_v2():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.1))

    model.add(Conv2D(128, kernel_size=(5, 5), activation='relu'))
    model.add(Dropout(0.1))

    model.add(Flatten())
    model.add(Dropout(0.1))

    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.25))

    model.add(Dense(10, activation='softmax'))
    model.summary()
    return model

# kernel_size 7->5->3 version
def create_cnn_model_v3():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(7, 7), activation='relu', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.1))

    model.add(Conv2D(64, kernel_size=(5, 5), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.1))

    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(Dropout(0.1))

    model.add(Flatten())
    model.add(Dropout(0.1))

    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.25))

    model.add(Dense(10, activation='softmax'))
    model.summary()
    return model

# just test
def create_cnn_model_v4():
    model = Sequential()
    model.add(Conv2D(16, kernel_size=(5, 5), activation='relu', padding='same', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.1))

    model.add(Conv2D(36, kernel_size=(5, 5), activation='relu', padding='same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.1))

    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation='softmax'))
    model.summary()
    return model

# just test2
def create_cnn_model_v5():
    model = Sequential()

    model.add(Conv2D(32, (5,5), activation="relu", padding="same", input_shape=(28,28,1)))
    model.add(Conv2D(32, (5,5), activation="relu", padding="same", input_shape=(28,28,1)))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3,3), activation="relu", padding="same"))
    model.add(Conv2D(64, (3,3), activation="relu", padding="same"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation="softmax"))
    model.summary()
    return model

# just test3
def create_cnn_model_v6():
    model = Sequential()

    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation="softmax"))
    model.summary()

    return model

# deeper 3 3 3 version
def create_cnn_model_v7():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.1))

    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(Dropout(0.1))

    model.add(Flatten())
    model.add(Dropout(0.1))

    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.25))

    model.add(Dense(10, activation='softmax'))
    model.summary()
    return model

# more deeper 3 3 3 3 version
def create_cnn_model_v8():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.1))

    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(Dropout(0.1))

    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(Dropout(0.1))

    model.add(Flatten())
    model.add(Dropout(0.1))

    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.25))

    model.add(Dense(10, activation='softmax'))
    model.summary()
    return model

# no MaxPooling2D, more deeper 3 3 3 3 3 version
def create_cnn_model_v9():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(Dropout(0.1))

    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(Dropout(0.1))

    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(Dropout(0.1))

    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(Dropout(0.1))

    model.add(Flatten())
    model.add(Dropout(0.1))

    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.25))

    model.add(Dense(10, activation='softmax'))
    model.summary()
    return model

# more deeper 3->3->5->7 version
def create_cnn_model_v10():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(Dropout(0.1))

    model.add(Conv2D(128, kernel_size=(5, 5), activation='relu'))
    model.add(Dropout(0.1))

    model.add(Conv2D(128, kernel_size=(7, 7), activation='relu'))
    model.add(Dropout(0.1))

    model.add(Flatten())
    model.add(Dropout(0.1))

    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.25))

    model.add(Dense(10, activation='softmax'))
    model.summary()
    return model

'''
def create_ResNet50():
    model = ResNet50(include_top=False, weights='imagenet', input_tensor=None, input_shape=(28, 28, 1)) #[(None, 224, 224, 3)
    #model = ResNet50()
    model.summary()
    return model
'''

def show_training_curve(train_history):
    plt.plot(train_history.history['loss'])
    plt.plot(train_history.history['val_loss'])
    plt.title('train history')
    plt.ylabel('loss')
    plt.xlabel('epochs')
    plt.legend(['loss', 'val_loss'], loc='upper left')
    plt.savefig(os.path.join('.', 'term_project', datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S")))
    #plt.show()

def main(operator='train'):
    print('-----main {} init-----'.format(operator))
    term_project_path = os.path.join('C:\\', 'Users', 'user', 'Desktop', 'algorithm', 'term_project')
    model_dict = {
        'cnn_v1':create_cnn_model_v1(),
        'cnn_v2':create_cnn_model_v2(),
        'cnn_v3':create_cnn_model_v3(),
        'cnn_v4':create_cnn_model_v4(),
        'cnn_v5':create_cnn_model_v5(),
        'cnn_v6':create_cnn_model_v6(),
        'cnn_v7':create_cnn_model_v7(),
        'cnn_v8':create_cnn_model_v8(), #best
        'cnn_v9':create_cnn_model_v9(),
        'cnn_v10':create_cnn_model_v10(),
        #'ResNet50':create_ResNet50(),
    }

    if operator == 'train':
        train_datapath = os.path.join(term_project_path, 'train_image')
        # get train data
        if os.path.isfile(os.path.join(term_project_path, 'train_data_x.npy')):
            train_data_x, train_data_y = np.load(os.path.join(term_project_path, 'train_data_x.npy')), np.load(os.path.join(term_project_path, 'train_data_y.npy'))
        else:
            train_data_x, train_data_y = data_x_y_preprocess(train_datapath)
            np.save(os.path.join(term_project_path, 'train_data_x.npy'), train_data_x)
            np.save(os.path.join(term_project_path, 'train_data_y.npy'), train_data_y)
        print('---> train_data_x.shape, train_data_y.shape:', train_data_x.shape, train_data_y.shape)
        # loop in model_dict
        for model_name, model in model_dict.items():
            if os.path.isfile(os.path.join(term_project_path, '{}.h5'.format(model_name))):
                print('{} has been train!!!'.format(model_name))
            else:
                model.compile(
                    loss='categorical_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy']
                )
                train_history = model.fit(
                    train_data_x, train_data_y,
                    batch_size=32,
                    epochs=30,
                    verbose=1,
                    validation_split=0.1
                )
                show_training_curve(train_history)
                save_model(model, os.path.join(term_project_path, '{}.h5'.format(model_name)))
    elif operator == 'test':
        test_datapath = os.path.join(term_project_path, 'test_image')
        if os.path.isfile(os.path.join(term_project_path, 'test_data_x.npy')):
            test_data_x, test_data_y = np.load(os.path.join(term_project_path, 'test_data_x.npy')), np.load(os.path.join(term_project_path, 'test_data_y.npy'))
        else:
            test_data_x, test_data_y = data_x_y_preprocess(test_datapath)
            np.save(os.path.join(term_project_path, 'test_data_x.npy'), test_data_x)
            np.save(os.path.join(term_project_path, 'test_data_y.npy'), test_data_y)
        print('test_data_x.shape, test_data_y.shape:', test_data_x.shape, test_data_y.shape)

        #for all h5
        for file_name in os.listdir(term_project_path):
            if file_name.split('.')[-1] == 'h5':
                model = load_model(os.path.join(term_project_path, file_name))
                score = model.evaluate(test_data_x, test_data_y, verbose=0)
                print('{} test acc: {:.5f}, test loss: {:.5f}'.format(file_name, score[1], score[0]))
    else:
        print('operator error!!!')


if __name__ == '__main__':
    main(operator='train')
    main(operator='test')