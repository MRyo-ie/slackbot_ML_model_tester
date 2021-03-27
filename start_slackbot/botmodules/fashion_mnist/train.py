import json
import os

import tensorflow as tf
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
train_images = train_images / 255.0

# d = {'signature_name': 'serving_default',
#      'inputs': [test_images[0].tolist()]}

# with open('./test_data.json', mode='w') as f:
#     f.write(json.dumps(d))

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28), name='inputs'),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

model_path = './models/fashion_model/'
os.makedirs(model_path, exist_ok=True)
tf.saved_model.save(model, os.path.join(model_path, '1'))

