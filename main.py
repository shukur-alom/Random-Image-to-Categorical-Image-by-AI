from keras.applications import nasnet
import os,shutil
import numpy as np
from keras.preprocessing.image import load_img,img_to_array

model = nasnet.NASNetLarge(weights="NASNet-large.h5")

for j in os.listdir('random image'):
    img_path_in = f'random image/{j}'
    img_2 = img_to_array(load_img(img_path_in,target_size=(331,331,3)))
    img_2 = nasnet.preprocess_input(np.expand_dims(img_2, axis=0))
    result = nasnet.decode_predictions(model.predict(img_2), top=5)
    for i in result[0]:
        print(i)
        if i[2] >= 0.50:
            name = i[1]
            if name in os.listdir('designe image'): shutil.copy(img_path_in,f"designe image/{name}")
            else: 
                os.mkdir(f"designe image/{name}")
                shutil.copy(img_path_in,f"designe image/{name}")