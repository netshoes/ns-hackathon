# [START app]
import json
import logging
import os
import io
import cv2
import base64
import datetime
import webcolors
import itertools
import numpy as np

from PIL import Image
from flask import Flask, request
from flask_cors import CORS
from collections import Counter
from keras.models import load_model
from keras.preprocessing import image
from sklearn.cluster import KMeans
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath("hackathon-07-cecd0cd0bd94.json")

app = Flask(__name__)
CORS(app)

def init():
    global DIC_COLORS
    global MODEL
    MODEL = load_model('model.h5')
    MODEL._make_predict_function()
    DIC_COLORS = {'black': 'Preto',
        'dimgray': 'Preto',
        'dimgrey': 'Preto/ Cinza',
        'gray': 'Cinza/Branco',
        'grey': 'Cinza',
        'darkgray': 'Preto / Cinza',
        'darkgrey': 'Cinza',
        'silver': 'Cinza',
        'lightgray': 'Cinza / Branco',
        'lightgrey': 'Cinza / Branco',
        'gainsboro': 'Cinza / Branco',
        'whitesmoke': 'Branco',
        'white': 'Branco',
        'snow': 'Branco',
        'rosybrown': 'Vermelho',
        'lightcoral': 'Vermelho',
        'indianred': 'Vermelho',
        'brown': 'Vermelho',
        'firebrick': 'Vermelho',
        'maroon': 'Vermelho',
        'darkred': 'Vermelho',
        'red': 'Vermelho',
        'mistyrose': 'Vermelho',
        'salmon': 'Vermelho',
        'tomato': 'Vermelho',
        'darksalmon': 'Vermelho',
        'coral': 'Vermelho',
        'orangered': 'Vermelho',
        'lightsalmon': 'Vermelho',
        'sienna': 'Vermelho',
        'seashell': 'Branco',
        'chocolate': 'Vermelho',
        'saddlebrown': 'Vermelho',
        'sandybrown': 'Vermelho',
        'peachpuff': 'Branco',
        'peru': 'Vermelho',
        'linen': 'Branco',
        'bisque': 'Branco',
        'darkorange': 'Laranja',
        'burlywood': 'Vermelho',
        'antiquewhite': 'Branco',
        'tan': 'Cinza',
        'navajowhite': 'Branco',
        'blanchedalmond': 'Branco',
        'papayawhip': 'Branco',
        'moccasin': 'Branco',
        'orange': 'Laranja',
        'wheat': 'Branco',
        'oldlace': 'Branco',
        'floralwhite': 'Branco',
        'darkgoldenrod': 'Marrom',
        'goldenrod': 'Marrom',
        'cornsilk': 'Branco',
        'gold': 'Dourado',
        'lemonchiffon': 'Branco',
        'khaki': 'Bege',
        'palegoldenrod': 'Branco/Amarelo',
        'darkkhaki': 'Verde',
        'ivory': 'Branco',
        'beige': 'Branco',
        'lightyellow': 'Branco',
        'lightgoldenrodyellow': 'Branco',
        'olive': 'Verde',
        'yellow': 'Amarelo',
        'olivedrab': 'Verde',
        'yellowgreen': 'Verde',
        'darkolivegreen': 'Verde',
        'greenyellow': 'Verde',
        'chartreuse': 'Verde',
        'lawngreen': 'Verde',
        'honeydew': 'Branco',
        'darkseagreen': 'Verde',
        'palegreen': 'Verde',
        'lightgreen': 'Verde',
        'forestgreen': 'Verde',
        'limegreen': 'Verde',
        'darkgreen': 'Verde',
        'green': 'Verde',
        'lime': 'Verde',
        'seagreen': 'Verde',
        'mediumseagreen': 'Verde',
        'springgreen': 'Verde',
        'mintcream': 'Branco',
        'mediumspringgreen': 'Verde',
        'mediumaquamarine': 'Azul',
        'aquamarine': 'Azul',
        'turquoise': 'Azul',
        'lightseagreen': 'Azul',
        'mediumturquoise': 'Azul',
        'azure': 'Branco',
        'lightcyan': 'Branco',
        'paleturquoise': 'Azul',
        'darkslategray': 'Azul',
        'darkslategrey': 'Preto',
        'teal': 'Azul',
        'darkcyan': 'Azul',
        'aqua': 'Azul',
        'cyan': 'Azul',
        'darkturquoise': 'Azul',
        'cadetblue': 'Azul',
        'powderblue': 'Azul',
        'lightblue': 'Azul',
        'deepskyblue': 'Azul',
        'skyblue': 'Azul',
        'lightskyblue': 'Azul',
        'steelblue': 'Azul',
        'aliceblue': 'Branco',
        'dodgerblue': 'Azul',
        'lightslategray': 'Cinza/Azul',
        'lightslategrey': 'Cinza/Azul',
        'slategray': 'Cinza',
        'slategrey': 'Cinza',
        'lightsteelblue': 'Cinza',
        'cornflowerblue': 'Azul',
        'royalblue': 'Azul',
        'ghostwhite': 'Branco',
        'lavender': 'Branco',
        'midnightblue': 'Preto / Azul',
        'navy': 'Azul',
        'darkblue': 'Azul',
        'mediumblue': 'Azul',
        'blue': 'Azul',
        'slateblue': 'Azul',
        'darkslateblue': 'Azul',
        'mediumslateblue': 'Azul',
        'mediumpurple': 'Roxo',
        'blueviolet': 'Azul',
        'indigo': 'Roxo',
        'darkorchid': 'Roxo',
        'darkviolet': 'Roxo',
        'mediumorchid': 'Roxo',
        'thistle': 'Vermelho',
        'plum': 'Vermelho',
        'violet': 'Vermelho',
        'purple': 'Vermelho',
        'darkmagenta': 'Vermelho',
        'fuchsia': 'Vermelho',
        'magenta': 'Vermelho',
        'orchid': 'Vermelho',
        'mediumvioletred': 'Vermelho',
        'deeppink': 'Vermelho',
        'hotpink': 'Vermelho',
        'lavenderblush': 'Vermelho',
        'palevioletred': 'Vermelho',
        'crimson': 'Vermelho',
        'pink': 'Rosa',
        'lightpink': 'Vermelho'}

@app.route('/', methods=['GET'])
def index():
    return str("TESTE"), 200


@app.route('/predict', methods=['POST'])
def predict():
    images = request.get_json(force=True)
    client_google = vision.ImageAnnotatorClient()
    
    results = []
    
    try:
        for image_ in images:   
            categoria = image_['categoria']
            marca     = image_['marca']
            cor       = image_['cor']

            tenis = ['Shoe', 'Sneakers', 'Footwear']
            camiseta = ['T-shirt']

            if categoria == 'Camiseta':
                labels = camiseta
            elif categoria == 'Tênis':
                labels = tenis

            image_object = preprocess_image(image_['image'])
            image_google = types.Image(content=base64.b64decode(image_['image']))

            # Label Detection
            response = client_google.label_detection(image=image_google)

            categoria_certa = False
            for label in response.label_annotations:
                if len(set(labels).intersection(set([label.description]))) > 0:
                    categoria_certa = True

            # Object detection
            response = client_google.object_localization(image=image_google)
            croped_image = crop_image(response, image_object, labels)

            # Save image
            name_date = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
            path_image_object_boxed = 'output_' + name_date + '.jpg'
            croped_image.save(path_image_object_boxed)

            # Predict Brand
            brand = predict_brand(image_object)

            # Detect color
            color = detect_color(croped_image)
            result_array = {
                image_['name']: {
                    'categoria' : categoria_certa,
                    'marca' : brand,
                    'cor': color,
                    'path_image': path_image_object_boxed
                }
            }
            results.append(result_array)

        results = {'results' : results}

    except Exception as e:
        results = {'error': str(e)}

    return json.dumps(results), 200

def predict_brand(image_object):
    tensor = img_to_tensor(image_object, (100,100))
    #   print(tensor.shape)
    predicao = MODEL.predict(tensor)
    brand_id = np.argmax(predicao)

    if brand_id == 0:
        brand = 'Adidas'
    elif brand_id == 1:
        brand = 'New Balance'
    elif brand_id == 2:
        brand = 'Olympikus'

    return brand


def img_to_tensor(img_object, size):
    img_object = img_object.resize(size, Image.ANTIALIAS)
    img_array = image.img_to_array(img_object)
    return np.expand_dims(img_array, axis=0).astype('float32')

def detect_color(img_object):

    img_object = img_object.resize((50, 50), Image.ANTIALIAS)
    img_array  = image.img_to_array(img_object)

    img_array_cropped = mov_win( img_array, (15,15) )

    lista, cor_final = acha_cor(img_array_cropped)

    return cor_final

def mov_win(im, window_size = (15,15)):
    variance = 10000000
    for col in range(15):
        for lin in range(15):
            im_ = im[10+col:(10+window_size[1])+col, 10+lin:(10+window_size[0])+lin]
            vari = im_var(im_)

            if vari < variance:
                variance = vari
                win_ = im_
    return win_

def im_var(img):
    r,g,b = cv2.split(img)
    r= list(itertools.chain(*r))
    g= list(itertools.chain(*g))
    b= list(itertools.chain(*b))
    
    x = np.vstack([r,g,b])
    cov_ = np.cov(x)
    
    return cov_[0][0]+cov_[1][1]+cov_[2][2] + cov_[0][1] + cov_[0][2]+cov_[1][2]

def acha_cor(win):
    cor_ = []
    for i in [1,2,3,4,5]:
        cor, cor_mais_clara, bar = clustered_color(win,i)
        requested_colour = (cor[0], cor[1], cor[2])
        closest_name = get_colour_name(requested_colour)
        cor_.append(DIC_COLORS[closest_name])

    a = Counter(cor_)
    return cor_, max(a, key=a.get)

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def clustered_color(img, num_clusters):

    image = img.reshape(img.shape[0]*img.shape[1],3)
    clt = KMeans(n_clusters = num_clusters)
    clt.fit(image)

    hist = centroid_histogram(clt)
    bar  =  plot_colors(hist, clt.cluster_centers_)
    return bar

def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins = numLabels)

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist

def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
    # of each of the colors
    bar = np.zeros((50, 300, 3), dtype = "uint8")
    startX = 0
    maior_porcentagem = 0
    cor = [0,0,0]
    menor_diferenca = 255*3
    cor_mais_clara = [0,0,0]
    # loop over the percentage of each cluster and the color of
    # each cluster
    for (percent, color) in zip(hist, centroids):
        diferenca = (255*3)-(color[0]+color[0]+color[0])
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            cor_mais_clara = color

        if maior_porcentagem < percent:
            maior_porcentagem = percent
            cor = color
        
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
            color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return cor, cor_mais_clara, bar

def get_colour_name(requested_colour):
    try:
        closest_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return closest_name

def crop_image(response, image_object, labels):
    boxes = []
    i = 0
    max_area = -1
    max_i = -1
    object_detected_bool = False

    for object_detected in response.localized_object_annotations:
        if object_detected.name in labels:
            
            boxes.append(
                {
                    'x1':object_detected.bounding_poly.normalized_vertices[0].x,
                    'y1':object_detected.bounding_poly.normalized_vertices[0].y,
                    'x3':object_detected.bounding_poly.normalized_vertices[2].x,
                    'y3':object_detected.bounding_poly.normalized_vertices[2].y
                }
            )
            area = (boxes[i]['x3'] - boxes[i]['x1']) * (boxes[i]['y3'] - boxes[i]['y1'])
            if area > max_area:
                max_area = area
                max_i = i
                object_detected_bool = True

            i = i+1

    if object_detected_bool:
        image_pil = image_object
        width, height = image_pil.size

        x1 = int(boxes[max_i]['x1']*width)
        y1 = int(boxes[max_i]['y1']*height)
        x2 = int(boxes[max_i]['x3']*width)
        y2 = int(boxes[max_i]['y3']*height)

        img_array = np.array(image.img_to_array(image_pil))
        image_object_cropped = image.array_to_img(img_array[y1:y2,x1:x2])

    else:
        image_object_cropped = image_object
    
    return image_object_cropped


@app.errorhandler(500) 
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500
'''
def crop_car(image_object):
    img_array = np.array(image.img_to_array(image_object))
    with graph.as_default():
        crop_sucessful, image_object_detected, y1, y2, x1, x2 = MODEL_YOLO.detect_biggest_car(image_object)

    image_object_cropped = image.array_to_img(img_array[y1:y2,x1:x2])
    return crop_sucessful, image_object_cropped, image_object_detected
'''
def model_predict(image_object, image_name):
    medio_grave = 0
    result = { 
    }

    return result, medio_grave

def preprocess_image(img64encoded):
    image_bytes = base64.b64decode(img64encoded)
    image_object = Image.open(io.BytesIO(image_bytes))
    return image_object

if __name__ == '__main__':
    init()
    port = int(os.environ.get('PORT', 5001))
    app.run(host='127.0.0.1', port=port, debug=True)
# [END app]
