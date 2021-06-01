import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import seaborn as sns 
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf 
from tensorflow.keras import (
  layers, activations, losses, optimizers, metrics,
)
from tensorflow.keras.layers.experimental import preprocessing 
from tensorflow.keras.models import Sequential 
print(tf.__version__)

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
column_names = [
  'MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight',
  'Acceleration', 'Model Year', 'Origin']

raw_dataset = pd.read_csv(
  url, names=column_names, 
  na_values='?', comment='\t',
  sep=' ', skipinitialspace=True,
)

dataset = raw_dataset.copy() 
print(dataset.tail())



print(dataset.isna().sum())

dataset.dropna(inplace=True)

print(dataset.isna().sum())

dataset['Origin'] = dataset['Origin'].map(
  {1: 'USA', 2: 'Europe', 3: 'Japan'})

dataset = pd.get_dummies(dataset, prefix='', prefix_sep='')
print(dataset.tail())

from sklearn.model_selection import train_test_split 
train_dataset, test_dataset \
  = train_test_split(dataset, train_size=0.8, random_state=0)

sns.pairplot(
  train_dataset[
    ['MPG', 'Cylinders', 'Displacement', 'Weight']],
  diag_kind='kde',  
)

print(train_dataset.describe().transpose())


train_features, test_features \
  = train_dataset.copy(), test_dataset.copy() 

train_labels, test_labels \
  = train_features.pop('MPG'), test_features.pop('MPG')


print(train_dataset.describe().transpose()[['mean', 'std']])

normalizer = preprocessing.Normalization() 
normalizer.adapt(train_features.values)
print(normalizer.mean.numpy())

first = train_features[:1].values
with np.printoptions(precision=3, suppress=True):
  print('First example: ', first)
  print()
  print('Normalized: ', normalizer(first).numpy())


horsepower = train_features['Horsepower'].values 
horsepower_normalizer = preprocessing.Normalization(
  input_shape=(1, ),
)
horsepower_normalizer.adapt(horsepower)
horsepower_model = Sequential([
  horsepower_normalizer, 
  layers.Dense(units=1),
])

horsepower_model.summary() 

print(horsepower_model.predict(horsepower[:10]))


horsepower_model.compile(
  optimizer=tf.optimizers.Adam(learning_rate=1e-3),
  loss=losses.MeanAbsoluteError(),
)

history = horsepower_model.fit(
  train_features['Horsepower'], train_labels, 
  epochs=100, 
  verbose=2, 
  validation_split=0.2,
)

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch 
print(hist.tail())


def plot_loss(history):
  hist = history.history
  plt.plot(hist['loss'], label='loss')
  plt.plot(hist['val_loss'], label='val_loss')
  plt.ylim([0, 10])
  plt.xlabel('Epoch')
  plt.ylabel('Error [MPG]')
  plt.legend() 
  plt.grid(True)

plot_loss(history)


test_results = {}

test_results['horsepower_model'] = horsepower_model.evaluate(
  test_features['Horsepower'], test_labels, verbose=0,
)

x = tf.linspace(0.0, 250, 251)
y = horsepower_model.predict(x)

def plot_horsepower(x, y):
  plt.scatter(
    train_features['Horsepower'], train_labels, label='Data')
  plt.plot(x, y, color='k', label='Predictions')
  plt.xlabel('Horsepower')
  plt.ylabel('MPG')
  plt.legend() 

plot_horsepower(x, y)


linear_model = Sequential([
  normalizer, 
  layers.Dense(units=1),
])

linear_model.predict(train_features[:10])

print(linear_model.layers[1].kernel)


linear_model.compile(
  loss=losses.MeanAbsoluteError(),
  optimizer=optimizers.Adam(learning_rate=0.01)
)


history = linear_model.fit(
  train_features, train_labels, 
  epochs=100,
  verbose=0,
  validation_split=0.2,
)

plot_loss(history)

test_results['linear_model'] = linear_model.evaluate(
  test_features, test_labels, verbose=0,
)



def build_and_compile(norm):
  model = Sequential([
    norm, 
    layers.Dense(64, activation=activations.relu),
    layers.Dense(64, activation=activations.relu),
    layers.Dense(1)
  ])
  model.compile(
    loss=losses.MeanAbsoluteError(),
    optimizer=optimizers.Adam(learning_rate=1e-4))
  return model 



dnn_horsepower_model = build_and_compile(horsepower_normalizer)
dnn_horsepower_model.summary() 

history = dnn_horsepower_model.fit(
  train_features['Horsepower'], train_labels, 
  validation_split=0.2, 
  verbose=2, epochs=100,
)

plot_loss(history)

x = tf.linspace(0.0, 250, 251)
y = dnn_horsepower_model.predict(x)

plot_horsepower(x, y)

test_results['dnn_horsepower_model'] \
  = dnn_horsepower_model.evaluate(
    test_features['Horsepower'], test_labels, 
    verbose=0,
  )



dnn_model = build_and_compile(normalizer)
dnn_model.summary()

hisotry = dnn_model.fit(
  train_features, train_labels, 
  validation_split=0.2, 
  verbose=0, epochs=100,
)

plot_loss(history)

test_results['dnn_Model'] = dnn_model.evaluate(
  test_features, test_labels, verbose=0,
)

print(
  pd.DataFrame(
    test_results, index=['Mean  absolute error [MPG]']).T
)


test_predictions = dnn_model.predict(test_features).flatten() 

a = plt.axes(aspect='equal')
plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values [MPG]')
plt.ylabel('Predictions [MPG]')
lims = [0, 50]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims, lims)

error = test_predictions - test_labels 
plt.hist(error, bins=25)
plt.xlabel('Prediction Error [MPG]')
_ = plt.ylabel('Count')

dnn_model.save(f'/root/dnn_model')

model = tf.keras.models.load_model('/root/dnn_model')
test_results['reloaded'] = model.evaluate(
  test_features, test_labels, verbose=0,
)

print(
  pd.DataFrame(
    test_results, index=['Mean absolute error [MPG]']).T
)


load_model tteiuhanashiwoshiteiruwakenanndayo





