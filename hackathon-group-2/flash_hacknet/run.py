import io
import os

# Imports the Google Cloud client library
# [START vision_python_migration_import]
import json
from google.cloud import vision
from google.cloud.vision import types
from flask import Flask, request, jsonify
import pandas as pd
import json
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

def map_string_to_number(string):
    n = 0
    try:
        n = n + int(string)
        return n
    except:
        if string is None :
            return 0
        for l in range(len(str(string))):
            n = n + 2**l+int(ord(string[l]))
        return n/(2**l+len(str(string)))


# In[427]:


import math
def cosine_similarity(v1,v2):
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)


# In[265]:


def to_lower(df):
    for i in ["cor","departamento","tipoProduto","valorGenero","tamanho","marca","nome"]:
        df[i] = df[i].str.lower()

def map_df_to_numbers(df, exception = "_id"):
    for column in df.columns:
        if column == exception:
            continue
        for line in range(len(df[column])):
            df[column][line] = map_string_to_number(df[column][line])
            
def normalize(df, exception = "id"):
    for column in df.columns:
        if column == exception:
            continue
        df[column] = df[column]/(max(df[column]))


# In[268]:


def apply_weights(df,column,perc,baseline = 0):
    df[column] = baseline+df[column]*perc


# In[476]:


def distance(centroids,df):
    l = []
    size = len(df)
    for i in range(size):
        l += [cosine_similarity(centroids[df["prediction"]][i],df[["cor","departamento","tipoProduto","valorGenero","tamanho","marca","nome"]].loc[i].tolist())]
    return df.assign(distance = l) 

@app.route('/sellerProducts', methods=['POST','GET'])
def hello_world():

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key.json"
    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    all_data = request.get_json()
    list_shoes = []

    for data in all_data['data']:

        #return jsonify(data)
        client = vision.ImageAnnotatorClient()
        # prepara um objeto para receber uma imagem e passa a devida url
        image = vision.types.Image()
        image.source.image_uri = data['imagem1']

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        #only the heaviest label
        if len(labels) >0:
            for x in range(5):
                if labels[x].description == 'Shoe':
                    list_shoes.append(data)
                    #return jsonify('resultado:', labels[x].description)
            #return jsonify('resultado:', labels[0].description)
        #else:
            #return jsonify('resultado:', '')

        #daqui pra frente list_shoes soh tem dado de shoes


    df_train = pd.read_json("dados.json",encoding="utf-8")


# In[389]:


    df_X = pd.DataFrame(columns=["cor","departamento","tipoProduto","valorGenero","tamanho","marca","nome"])
    for row in df_train["sku"]:
        row_string = str(row).replace("\"","").replace("None","\"none\"").replace("\'","\"").replace("\\n","").replace("\\xa0","").replace("\\r","").replace("\\x96","").replace("\\x8","").replace("\\x1c","").replace("\\x1d","")
        k = json.loads(row_string)
        cor = None
        depto = None
        tipo = None
        genero =None
        tamanho = None
        marca = None
        nome = None
        
        nome = k["name"]
        depto = k["product"]["department"]["name"]
        tipo = k["product"]["productType"]["name"]
        genero = k["product"]["gender"]
        marca = k["product"]["brand"]["name"]
        
        for config in k["configurations"]:
            if config["type"] == "color":
                cor = config["name"]
            if config["type"] == "size":    
                tamanho = config["name"]
        
        df_X.loc[len(df_X)] = [cor,depto,tipo,genero,tamanho,marca,nome]


    # In[390]:


    to_lower(df_X)

    map_df_to_numbers(df_X)

    normalize(df_X)

    apply_weights(df_X,"valorGenero",0.1)
    apply_weights(df_X,"marca",0.3,0.5)
    apply_weights(df_X,"tipoProduto",0.8,1)
    apply_weights(df_X,"departamento",0.3,0.7)
    apply_weights(df_X,"nome",0.2)
    apply_weights(df_X,"tamanho",0.1)
    apply_weights(df_X,"cor",0.1)


    # In[391]:


    # Leitura de dados do marketplace
    df_init = pd.DataFrame.from_dict(list_shoes)

    
    # In[498]:


    df_test = df_init[["cor","departamento","tipoProduto","valorGenero","tamanho","marca","nome","id"]]


    # In[499]:


    df_test = df_test.fillna(value="0")
    to_lower(df_test)
    map_df_to_numbers(df_test)

    normalize(df_test)

    apply_weights(df_test,"valorGenero",0.1)
    apply_weights(df_test,"marca",0.3,0.5)
    apply_weights(df_test,"tipoProduto",0.8,1)
    apply_weights(df_test,"departamento",0.3,0.7)
    apply_weights(df_test,"nome",0.2)
    apply_weights(df_test,"tamanho",0.1)
    apply_weights(df_test,"cor",0.1)


    # In[500]:


    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters= 3).fit(df_X)


    # In[501]:


    df_test["prediction"] = kmeans.predict(df_test[["cor","departamento","tipoProduto","valorGenero","tamanho","marca","nome"]])
    df_test = distance(kmeans.cluster_centers_,df_test)


    # In[502]:


    df_final = pd.merge(df_init,df_test,left_on="id",right_on="id")
    df_final = df_final[["tipoProduto_x","departamento_x","valorGenero_x","tamanho_x","marca_x","cor_x","nome_x","distance","id","prediction"]]


    # In[532]:
    print(df_final)


    l = []
    json_data = {}
    for pred in df_test["prediction"].unique():
        json_data_i = {}
        json_data_i["cluster"] = pred
        k1 = []
        for item in df_test[df_test["prediction"] == pred].iterrows():
            json_data_i_i = {}
            json_data_i_i["product_id"] = str(item[1]["id"])
            json_data_i_i["distance"] = str(item[1]["distance"])
            k1.append(json_data_i_i)
        json_data_i["products"] = k1
        l.append(json_data_i)
    json_data["response"] = l
    json_response = json.dumps(json_data)
    print(json_response)
    return jsonify(json_response)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5001)
