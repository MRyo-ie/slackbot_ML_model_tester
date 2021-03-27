import numpy as np
import os.path as osp
from PIL import Image
import random
import tensorflow as tf
from tensorflow import keras

bot_py_path = './botmodules/fashion_mnist/'
model_path = 'models/fashion_model/1/'

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


def predict_fashion(X):
    new_model = tf.keras.models.load_model(osp.join(bot_py_path, model_path))
    img_arr = np.array(Image.open(X))
    img_arr = np.expand_dims(img_arr, 0)
    pred_single = new_model.predict(img_arr)
    ans_id = np.argmax(pred_single[0])
    print("============================================\n", 
            f'img_arr.shape : {img_arr.shape}\n', 
            f'    ans_id    : {ans_id}\n', 
            f' pred_single  : {pred_single}\n', 
            f'    answer    : {class_names[ans_id]}\n', 
          "\n============================================")
    return f"A : {class_names[ans_id]}"


if __name__ == "__main__":
    ## テスト用データを保存する。
    fashion_mnist = keras.datasets.fashion_mnist
    _, (test_images, test_labels) = fashion_mnist.load_data()

    for i in range(10):
        img_i = random.randrange(len(test_labels))
        pil_image = Image.fromarray(test_images[img_i])
        ans_id = test_labels[img_i]
        pil_image.save(osp.join(bot_py_path, f"test_imgs/test{i}_{class_names[ans_id]}.png"))

# if __name__ == "__main__":
#     predict_fashion('./tmp.png')
