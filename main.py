from flask import Flask, render_template,url_for, request, jsonify
import base64
from io import BytesIO
import tensorflow as tf
from keras.preprocessing import image
import numpy as np
from PIL import Image
import time
# from tensorflow.keras.backend import set_session


app = Flask(__name__ , static_url_path='')
app.config.from_object(__name__)
# app.run(host= '0.0.0.0')
app.config["IMAGE_UPLOADS"] = "images"

# sess_config = tf.ConfigProto(
#     log_device_placement=False,
#     allow_soft_placement = True,
#     gpu_options = tf.GPUOptions(
#         per_process_gpu_memory_fraction=1
#     )
# )
# graph = tf.get_default_graph()
# sess = tf.Session(graph=graph, config=sess_config)

# tf_config = some_custom_config
# sess = tf.Session(config=tf_config)


# set_session(sess)
model = tf.keras.models.load_model('mnist2.h5')
model.summary()


def save(data):
    data = data[22:]
    im = Image.open(BytesIO(base64.b64decode(data)))
    im2 = im.resize((28,28))
    im2.save('static/images/image.png', 'PNG')
    im.save('static/images/display.png', 'PNG')

    

def new_guess():
    img = Image.open('static/images/image.png').convert("L")
    img = np.resize(img, (28,28,1))
    im2arr = np.array(img)
    im2arr = im2arr.reshape(1,28,28,1)
    global model
    # global sess
    # global graph
    # with graph.as_default():
        # set_session(sess)    
    pred = model.predict_classes(im2arr)
    print('hogyaa')
    print(pred[0])
    return pred[0]







@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    start_time = time.time()
#    result = guess()
    result = new_guess()

    run_time =  time.time() - start_time
    return render_template("result.html" , result = result , time = run_time)

# @app.route('/getmethod/<jsdata>')
# def get_javascript_data(jsdata):
#     for _ in range(10): print('hii')
#     print('mil gaya')
#     # return render_template('index.html')
#     return jsdata


@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    jsdata = request.form['javascript_data']
    print('mil gaya')

    # print(jsdata)
    save(jsdata)
    # print(guess())
    return jsdata


if __name__ == '__main__':
    app.run(debug = True)