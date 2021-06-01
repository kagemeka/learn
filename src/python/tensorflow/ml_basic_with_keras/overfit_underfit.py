'''TODO
- Regularize, e.g., L1, L2, 
- Dropout 
'''

import tensorflow  as tf

print(tf.__version__)

from tensorflow.keras import (
  layers, activations, losses, optimizers, 
  regularizers, metrics, callbacks
)

from tensorflow.keras.models import Sequential


import tensorflow_docs as tfdocs 
import tensorflow_docs.modeling 
import tensorflow_docs.plots


from IPython import display 
from matplotlib import pyplot as plt 

import numpy as np 

import pathlib 
import shutil 
import tempfile 


logdir = pathlib.Path(tempfile.mkdtemp())/"tensorboard_logs"
shutil.rmtree(logdir, ignore_errors=True)

gz = tf.keras.utils.get_file(
  'HIGGS.csv.gz',
  'https://mlphysics.ics.uci.edu/data/higgs/HIGGS.csv.gz'
)


FEATURES = 28 

ds = tf.data.experimental.CsvDataset(
  gz, [float(),]*(FEATURES+1), compression_type='GZIP')


def pack_row(*row):
  label = row[0]
  features = tf.stack(row[1:], 1)
  return features,label

packed_ds = ds.batch(10000).map(pack_row).unbatch()

for features, label in packed_ds.batch(1000).take(1):
  print(features[0])
  plt.hist(features.numpy().flatten(), bins=101)


N_VALIDATION = int(1e3)
N_TRAIN = int(1e4)
BUFFER_SIZE = int(1e4)
BATCH_SIZE = 500 
STEPS_PER_EPOCH = N_TRAIN//BATCH_SIZE

validation_ds = packed_ds.take(N_VALIDATION).cache() 
train_ds = packed_ds.skip(N_VALIDATION).take(N_TRAIN).cache()

validation_ds = validation_ds.batch(BATCH_SIZE)
train_ds \
  = train_ds.shuffle(BUFFER_SIZE).repeat().batch(BATCH_SIZE)

lr_schedule = optimizers.schedules.InverseTimeDecay(
  initial_learning_rate=0.001,
  decay_steps=STEPS_PER_EPOCH*1000,
  decay_rate=1, 
  staircase=False,
)

def get_optimizer():
  return optimizers.Adam(lr_schedule=lr_schedule)



lr_schedule = optimizers.schedules.InverseTimeDecay(
  initial_learning_rate=1e-3,
  decay_steps=1,
  decay_rate=1e-3, 
  staircase=False,
)

# lr_schedule = optimizers.schedules.PolynomialDecay(
#   initial_learning_rate=1e-3,
#   decay_steps=1<<18,
#   power=1<<6,
#   end_learning_rate=1e-5,
# )

# optimizers.Adam(lr_schedule=lr_schedule)
print(lr_schedule(np.arange(1000)))

def get_optimizer():
  return optimizers.Adam(learning_rate=lr_schedule)

import numpy as np 

step = np.linspace(0, 10**5)
lr = lr_schedule(step)
plt.figure(figsize=(8, 6))
plt.plot(step/STEPS_PER_EPOCH, lr)
plt.ylim((0, max(plt.ylim())))
plt.xlabel('Epoch')
_ = plt.ylabel('Learning Rate')


def get_callbacks(name):
  return [
    tfdocs.modeling.EpochDots(),
    callbacks.EarlyStopping(
      monitor='val_binary_crossentropy', patience=200),
    callbacks.TensorBoard(logdir/name),
  ]


def compile_and_fit(
    model, name, optimizer=None, max_epochs=10000):
  if optimizer is None: 
    optimizer = get_optimizer() 
  model.compile(
    optimizer=optimizer,
    loss=losses.BinaryCrossentropy(from_logits=True),
    metrics=[
      losses.BinaryCrossentropy(
        from_logits=True,
        name='binary_crossentropy'
      ),
      metrics.BinaryAccuracy()]
  )

  model.summary()

  history = model.fit(
    train_ds,
    steps_per_epoch=STEPS_PER_EPOCH,
    validation_data=validation_ds,
    callbacks=get_callbacks(name),
    verbose=0)

  return history 



tiny_model = Sequential([
  layers.Dense(
    1<<4, activation=activations.elu, input_shape=(FEATURES, )),
    layers.Dense(1)
])
size_histories = {}

size_histories['Tiny'] = compile_and_fit(
  tiny_model, 'sizes/Tiny')


plotter = tfdocs.plots.HistoryPlotter(
  metric='binary_crossentropy',
  smoothing_std=10)

plotter.plot(size_histories)
plt.ylim([0.5, 0.7])

small_model = Sequential([
  layers.Dense(
    1<<4, activation=activations.elu, input_shape=(FEATURES, )),
  layers.Dense(1<<4, activation=activations.elu),
  layers.Dense(1),
])


size_histories['Small'] = compile_and_fit(
  small_model, 'sizes/Small')


medium_model = Sequential([
  layers.Dense(
    64, activation=activations.elu, input_shape=(FEATURES, )),
  layers.Dense(1<<6, activation=activations.elu),
  layers.Dense(1<<6, activation=activations.elu),
  layers.Dense(1),
])

size_histories['Medium'] = compile_and_fit(
  medium_model, 'sizes/Medium')


large_model = Sequential([
  layers.Dense(
    1<<9, activation=activations.elu, input_shape=(FEATURES,)),
  layers.Dense(1<<9, activation=activations.elu),
  layers.Dense(1<<9, activation=activations.elu),
  layers.Dense(1<<9, activation=activations.elu),
  layers.Dense(1<<9, activation=activations.elu),
  layers.Dense(1),
])


size_histories['Large'] = compile_and_fit(
  large_model, 'sizes/Large')



plotter.plot(size_histories)
a = plt.xscale('log')
plt.xlim([5, max(plt.xlim())])
plt.ylim([0.5, 0.7])
plt.xlabel('Epochs [Log Scale]')

display.IFrame(
  src="https://tensorboard.dev/experiment/vW7jmmF9TmKmy3rbheMQpw/#scalars&_smoothingWeight=0.97",
  width="100%", height="800px")


shutil.rmtree(
  logdir/'regularizers/Tiny', ignore_errors=True)

shutil.copytree(
  logdir/'sizes/Tiny', logdir/'regularizers/Tiny')


regularizer_histories = {} 
regularizer_histories['Tiny'] = size_histories['Tiny']


l2_model = Sequential([
  layers.Dense(
    1<<9, activation=activations.elu,
    kernel_regularizer=regularizers.l2(l2=0.001),
    input_shape=(FEATURES, ),
  ),
  layers.Dense(
    1<<9, activation=activations.elu,
    kernel_regularizer=regularizers.l2(l2=0.001),
  ),
  layers.Dense(
    1<<9, activation=activations.elu,
    kernel_regularizer=regularizers.l2(l2=0.001),
  ),
  layers.Dense(
    1<<9, activation=activations.elu,
    kernel_regularizer=regularizers.l2(l2=0.001),
  ),
  layers.Dense(1),
])

regularizer_histories['l2'] = compile_and_fit(
  l2_model, 'regularizers/l2')


plotter.plot(regularizer_histories)
plt.ylim([0.5, 0.7])


result = l2_model(features)
regularization_loss = tf.add_n(l2_model.losses)

import tensorflow_addons as tfa 


dropout_model = Sequential([
  layers.Dense(
    1<<9, activation=activations.elu,
    input_shape=(FEATURES,)),
  layers.Dropout(0.5),
  layers.Dense(1<<9, activation=activations.elu),
  layers.Dropout(0.5),
  layers.Dense(1<<9, activation=activations.elu),
  layers.Dropout(0.5),
  layers.Dense(1<<9, activation=activations.elu),
  layers.Dropout(0.5),
  layers.Dense(1),
])

regularizer_histories['dropout'] = compile_and_fit(
  dropout_model, 'regularizers/dropout')

plotter.plot(regularizer_histories)
plt.ylim([0.5, 0.7])

combined_model = tf.keras.Sequential([
  layers.Dense(
    512, kernel_regularizer=regularizers.l2(0.0001),
    activation='elu', input_shape=(FEATURES,)),
  layers.Dropout(0.5),
  layers.Dense(
    512, kernel_regularizer=regularizers.l2(0.0001),
    activation='elu'),
  layers.Dropout(0.5),
  layers.Dense(
    512, kernel_regularizer=regularizers.l2(0.0001),
    activation='elu'),
  layers.Dropout(0.5),
  layers.Dense(
    512, kernel_regularizer=regularizers.l2(0.0001),
    activation='elu'),
  layers.Dropout(0.5),
  layers.Dense(1)
])


regularizer_histories['combined'] = compile_and_fit(
  combined_model, 'regularizers/combined'
)

plotter.plot(regularizer_histories)
plt.ylim([0.5, 0.7])


display.IFrame(
  src="https://tensorboard.dev/experiment/fGInKDo8TXes1z7HQku9mw/#scalars&_smoothingWeight=0.97",
  width = "100%",
  height="800px")


