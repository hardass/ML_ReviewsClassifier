'''Train a recurrent convolutional network on the IMDB sentiment
classification task.

Gets to 0.8498 test accuracy after 2 epochs. 41s/epoch on K520 GPU.
'''
# from __future__ import print_function

# from keras.preprocessing import sequence

# from keras.datasets import imdb
# from __future__ import absolute_import
from keras.utils.data_utils import get_file
import numpy as np

# # Embedding
# max_features = 20000
# maxlen = 100
# embedding_size = 128

# # Convolution
# kernel_size = 5
# filters = 64
# pool_size = 4

# # LSTM
# lstm_output_size = 70

# # Training
# batch_size = 30
# epochs = 2

'''
Note:
batch_size is highly sensitive.
Only 2 epochs are needed as the dataset is very small.
'''

# print('Loading data...')
# (x_train, y_train), (x_test, y_test) = imdb.load_data(path="imdb.npz",num_words=max_features)
# print((x_train), 'train sequences')
# print((y_train), 'test sequences')

path = get_file('imdb.npz', origin='https://s3.amazonaws.com/text-datasets/imdb.npz')
with np.load(path) as f:
	x_train, labels_train = f['x_train'], f['y_train']
    # x_test, labels_test = f['x_test'], f['y_test']

for i in range (0,20):
	print(x_train[i])
# print(labels_train[0])
# print(len(x_train))
# print(len(labels_train))