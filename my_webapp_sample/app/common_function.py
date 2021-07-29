import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

def load_and_prep_image(filename, img_shape=224):
    img = tf.io.read_file(filename)
    img = tf.image.decode_image(img)
    img = tf.image.resize(img, size=[img_shape, img_shape])
    img = img/255.
    return img

import pathlib
import numpy as np

data_dir = pathlib.Path("10_food_classes_10_percent/train")
class_names = np.array(['chicken_curry', 'chicken_wings', 'fried_rice', 'grilled_salmon', 'hamburger', 'ice_cream', 'pizza', 'ramen', 'steak', 'sushi'])

def pred_and_plot(model, filename, class_names=class_names):
    img = load_and_prep_image(filename)
    
    pred = model.predict(tf.expand_dims(img, axis=0))
    
    if len(pred[0]) > 1:
        pred_class = class_names[tf.argmax(pred[0])]
    else:
        pred_class = class_names[int(tf.round(pred[0]))]
    
    plt.imshow(img)
    plt.title(f"Prediction: {pred_class}")
    plt.axis(False);
    print(filename.replace("uploads", "result"))
    plt.savefig(filename.replace("uploads", "result"), dpi=300)