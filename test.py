import tensorflow as tf
from keras.preprocessing import image
import numpy as np
from PIL import Image



model = tf.keras.models.load_model('mnist2.h5')
model.summary()
 
# img = image.load_img('data/33.png')
def guess():
    img = Image.open('static/images/image.png').convert("L")
    img = np.resize(img, (28,28,1))
    im2arr = np.array(img)
    im2arr = im2arr.reshape(1,28,28,1)
    y_pred = model.predict_classes(im2arr)
    print(y_pred)

guess()