import numpy as np 
import os 
import PIL 
import PIL.Image 
import tensorflow as tf 
import tensorflow_datasets as tfds 
print(tf.__version__)

import pathlib 
dataset_url \
  = 'https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz'

data_dir = tf.keras.utils.get_file(
  origin=dataset_url,
  fname='flower_photos',
  untar=True)
print(data_dir)
data_dir = pathlib.Path(data_dir)
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

roses = list(data_dir.glob('roses/*'))
PIL.Image.open(str(roses[0]))

PIL.Image.open(str(roses[1]))

batch_size = 32
height = width = 180

train_ds = tf.keras.preprocessing \
  .image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='training',
    seed=123, 
    image_size=(height, width),
    batch_size=batch_size)


print(train_ds)

val_ds = tf.keras.preprocessing \
  .image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='validation',
    seed=123, 
    image_size=(height, width),
    batch_size=batch_size)


class_names = train_ds.class_names 
print(class_names)

import matplotlib.pyplot as plt 

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i+1)
    plt.imshow(images[i].numpy().astype(np.uint8))
    plt.title(class_names[labels[i]])
    plt.axis('off')

for image_batch, label_batch in train_ds:
  print(image_batch.shape)
  print(label_batch.shape)
  break

from tensorflow.keras import (
  layers, activations, regularizers, initializers,
  losses, optimizers, metrics,
  callbacks,
)


normalization_layer = layers.experimental \
  .preprocessing.Rescaling(1/255, offset=0)

normalized_ds = train_ds.map(
  lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0].numpy()
print(first_image.min(), first_image.max())



AUTOTUNE = tf.data.experimental.AUTOTUNE 

print(AUTOTUNE)
print(type(AUTOTUNE))
train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)


num_classes = len(class_names)


from tensorflow.keras.models import Sequential 

model = Sequential([
  layers.experimental.preprocessing.Rescaling(1/255),
  layers.Conv2D(
    filters=1<<5, kernel_size=3,
    activation=activations.relu, 
    kernel_regularizer=regularizers.L2(l2=0.001)),
  layers.MaxPooling2D(),
  layers.Dropout(0.5),
  layers.Conv2D(
    filters=1<<5, kernel_size=3,
    activation=activations.relu, 
    kernel_regularizer=regularizers.L2(l2=0.001)),
  layers.MaxPooling2D(),
  layers.Dropout(0.5),
  layers.Conv2D(
    filters=1<<5, kernel_size=3,
    activation=activations.relu, 
    kernel_regularizer=regularizers.L2(l2=0.001)),
  layers.MaxPooling2D(),
  layers.Dropout(0.5),
  layers.Flatten(),
  layers.Dense(
    1<<7, activation=activations.relu,
    kernel_regularizer=regularizers.L2(l2=0.001)),
  layers.Dropout(0.5),
  layers.Dense(num_classes),
])

model.compile(
  loss=losses.SparseCategoricalCrossentropy(from_logits=True),
  optimizer=optimizers.Adam(learning_rate=0.001),
  metrics=[metrics.SparseCategoricalAccuracy()],
)

model.fit(
  train_ds, validation_data=val_ds, epochs=2, verbose=2,
)


list_ds = tf.data.Dataset.list_files(
  str(data_dir/'*/*'), shuffle=False,
)
list_ds = list_ds.shuffle(
  image_count,
  reshuffle_each_iteration=False)


for f in list_ds:
  print(f.numpy())


class_names = np.array(sorted([
  item.name for item in data_dir.glob('*')
  if item.name != 'LICENCE.txt']))

print(class_names)

val_size = int(image_count * 0.2)
train_ds = list_ds.skip(val_size)
val_ds = list_ds.take(val_size)

print(tf.data.experimental.cardinality(train_ds).numpy())
print(tf.data.experimental.cardinality(val_ds).numpy())

def get_label(file_path):
  parts = tf.strings.split(file_path, os.path.sep)
  print(type(parts))
  one_hot = parts[-2] == class_names
  return tf.argmax(one_hot)


def decode_img(img):
  img = tf.image.decode_jpeg(img, channels=3)
  return tf.image.resize(img, [height, width])

def process_path(file_path):
  label = get_label(file_path)
  img = tf.io.read_file(file_path)
  img = decode_img(img)
  return img, label

train_ds = train_ds.map(
  process_path, num_parallel_calls=AUTOTUNE)
val_ds = val_ds.map(
  process_path, num_parallel_calls=AUTOTUNE)

for image, label in train_ds.take(1):
  print('image shape: ', image.numpy().shape)
  print('label: ', label.numpy())


def configure_for_performance(ds):
  return ds.cache() \
    .shuffle(buffer_size=1000) \
    .batch(batch_size) \
    .prefetch(buffer_size=AUTOTUNE)

train_ds = configure_for_performance(train_ds)
val_ds = configure_for_performance(val_ds)

image_batch, label_batch = next(iter(train_ds))

plt.figure(figsize=(10, 10))
for i in range(9):
  ax = plt.subplot(3, 3, i+1)
  plt.imshow(image_batch[i].numpy().astype(np.uint8))
  label = label_batch[i]
  plt.title(class_names[label])
  plt.axis('off')


model.fit(
  train_ds, validation_data=val_ds,
  epochs=3, verbose=2)


(train_ds, val_ds, test_ds), metadata = tfds.load(
  'tf_flowers',
  split=['train[:80%]', 'train[80%:90%]', 'train[90%:]'],
  with_info=True,
  as_supervised=True,
)


num_classes = metadata.features['label'].num_classes 
print(num_classes)

get_label_name = metadata.features['label'].int2str 
image, label = next(iter(train_ds))
_ = plt.imshow(image)
_ = plt.title(get_label_name(label))

train_ds = configure_for_performance(train_ds)
val_ds = configure_for_performance(val_ds)
test_ds = configure_for_performance(test_ds)



