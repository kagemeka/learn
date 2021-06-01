import matplotlib.pyplot as plt 
import os, re, shutil, string 
import tensorflow as tf 
from tensorflow.keras import (
  layers, losses, optimizers, preprocessing) 
from tensorflow.keras.layers \
  .experimental.preprocessing import TextVectorization 

from tensorflow.keras.models import Sequential
import os 
cfd: str = os.path.dirname(os.path.abspath(__file__))

print(tf.__version__)

# url = 'https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz'

# dataset = tf.keras.utils.get_file(
#   'aclImdb_v1.tar.gz', url, untar=True, 
#   cache_dir='/root', cache_subdir='')

# dataset_dir = f'{os.path.dirname(dataset)}/aclImdb'
dataset_dir = '/root/aclImdb'


print(os.listdir(dataset_dir))

train_dir = f'{dataset_dir}/train'
print(os.listdir(train_dir))

sample_file = f'{train_dir}/pos/1181_9.txt'
with open(sample_file) as f: print(f.read())


remove_dir = os.path.join(train_dir, 'unsup')
shutil.rmtree(remove_dir)


batch_size = 32
seed = 42

raw_train_ds = tf.keras.preprocessing \
  .text_dataset_from_directory(
    train_dir, 
    batch_size=batch_size, 
    validation_split=0.2, 
    subset='training', 
    seed=seed)


import string
import numpy as np 
# my_dict = np.vectorize(dict)
# a = my_dict([
#   ('a', 1),
#   ('b', 2),
# ])
# print(a)
print(string.punctuation)

import dataclasses 

for x_batch, y_batch in raw_train_ds.take(1):
  for i in range(3):
    print(x_batch.numpy()[i])
    print(y_batch.numpy()[i])



raw_val_ds = tf.keras.preprocessing \
  .text_dataset_from_directory(
    train_dir,
    batch_size=batch_size,
    validation_split=0.2,
    subset='validation',
    seed=seed,
  )


raw_test_ds = tf.keras.preprocessing \
  .text_dataset_from_directory(
    train_dir,
    batch_size=batch_size,
  )



def custom_standardization(input_data):
  lowercase = tf.strings.lower(input_data)
  stripped_html = tf.strings.regex_replace(
    lowercase, '<br />', ' ')
  return tf.strings.regex_replace(
    stripped_html, '[%s]' % re.escape(string.punctuation), '')


max_features = 1<<14
sequence_length = 1<<8


vectorize_layer = TextVectorization(
  standardize=custom_standardization,
  max_tokens=max_features,
  output_mode='int',
  output_sequence_length=sequence_length)

train_text = raw_train_ds.map(lambda x, y: x)
vectorize_layer.adapt(train_text)

def vectorize_text(text, label):
  text = tf.expand_dims(text, -1)
  return vectorize_layer(text), label

x_batch, y_batch = next(iter(raw_train_ds))
first_review, first_label = x_batch[0], y_batch[0]
print(first_review)
print(first_label)
print(vectorize_text(first_review, first_label))


train_ds = raw_train_ds.map(vectorize_text)
val_ds = raw_val_ds.map(vectorize_text)
test_ds = raw_test_ds.map(vectorize_text)

print(train_ds)
print(type(train_ds))


AUTOTUNE = tf.data.experimental.AUTOTUNE

train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)


embedding_dim = 16
model = Sequential([
  layers.Embedding(max_features+1, embedding_dim),
  layers.Dropout(0.2),
  layers.GlobalAveragePooling1D(),
  layers.Dropout(0.2),
  layers.Dense(1),
])

model.summary()

from tensorflow.keras import metrics
model.compile(
  loss=losses.BinaryCrossentropy(from_logits=True),
  optimizer=optimizers.Adam(learning_rate=5e-4),
  metrics=metrics.BinaryAccuracy(threshold=0.0),
)


epochs = 10 
history = model.fit(
  train_ds, 
  validation_data=val_ds,
  epochs=epochs,
  verbose=2,
)

print(history)


loss, acc = model.evaluate(test_ds)
print(f'loss: {loss}, accuracy: {acc}')

history = history.history 
print(history.keys())




