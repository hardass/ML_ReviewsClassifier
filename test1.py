'''Train a recurrent convolutional network on the IMDB sentiment
classification task.

Gets to 0.8498 test accuracy after 2 epochs. 41s/epoch on K520 GPU.
'''
from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import LSTM
from keras.layers import Conv1D, MaxPooling1D
from keras.datasets import imdb
import string

# Embedding
max_features = 20000
maxlen = 100
embedding_size = 128

# Convolution
kernel_size = 5
filters = 64
pool_size = 4

# LSTM
lstm_output_size = 70

# Training
batch_size = 30
epochs = 2

'''
Note:
batch_size is highly sensitive.
Only 2 epochs are needed as the dataset is very small.
'''

print('Loading data...')
# (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

words = {}
i = 0
# words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"

x_train = []
y_train = []
for line in open("train.txt"):
    post_line = []
    if int(line.split(' ', 1)[0]) == 2:
        continue
    if int(line.split(' ', 1)[0]) < 2:
        y_train.append(0)
    else:
        y_train.append(1)
    for word in line.split():
        word = word.strip(strip)
        if len(word) >= 2:
            if words.get(word, 0) == 0:
                words[word] = i
                i = i + 1
            post_line.append(words[word])
    x_train.append(post_line)

x_test = []
y_test = []
for line in open("train.txt"):
    post_line = []
    y_test.append(int(line.split(' ', 1)[0]))
    for word in line.split():
        word = word.strip(strip)
        if len(word) >= 2:
            if words.get(word, 0) == 0:
                words[word] = i
                i = i + 1
            post_line.append(words[word])
    x_test.append(post_line)



print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')

print('Pad sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

print('Build model...')

model = Sequential()
model.add(Embedding(max_features, embedding_size, input_length=maxlen))
model.add(Dropout(0.25))
model.add(Conv1D(filters,
                 kernel_size,
                 padding='valid',
                 activation='relu',
                 strides=1))
model.add(MaxPooling1D(pool_size=pool_size))
model.add(LSTM(lstm_output_size))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(x_test, y_test))
score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)
