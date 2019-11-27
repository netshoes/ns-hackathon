# Net Sage

The Marketplace solution that increases the matching rate through the use of Machine Learning, specifically, by classifying values based on their similarities.

## Getting Started

The general idea of the algorithm is to enrich a unsupervised learning model
with data from fields that go beyond the minimum required to generate
a SKU.

For this we include natural language processing elements, extracting the characteristics of the texts,
categorical with TF-IDF and bi-grams, where the minimum frequency
token is .1 and the maximum .2 to extract the characteristics
that can give context and highlight relationships
that the evaluator potentially uses to classify
the products entered by the seller.

The model improves its accuracy over time and a
higher number of SKUs are registered.

It is important to note that the results produced by our endeavours may be reproduced.

## k-nearest neighbors algorithm(kNN)

The general idea of the algorithm is to find k nearest tagged exemples 
of the not classified one, and using the tags of the nearest
exemples, it's taken a decision related of the class of the
untagged example.

We used the kNN due to the nature of the our database.
The simplicity of the algorithm allows the huge database to be
efficiently train the model.
The nature of the database, which has a variable number of possible
matches, prevents that other clustering algorithm, like K-means, to be used
efficiently, while kNN allows the matches number to be more dinamic,
working well even with low matches cases.
Another reason is that business rules does change with the time, so the use 
of a simple to understand algorithm ease the updates and maintenance in a 
future stage.

Here is the [thesis source](http://www.teses.usp.br/teses/disponiveis/55/55134/tde-19052009-135128/pt-br.php)

## Demo

A web interface was created to that an sku may be build live from the desired input. The mid layer is a Node.js express app, which receives the input, formats it and passes it to the matching API, thus re-transmitting back the correspondant matched values.

Here is the [Netstage Demo](https://netstagepixelados.herokuapp.com/) and the Heroku [dashboard](https://dashboard.heroku.com/apps/netstagepixelados/deploy/github)

## Built With

* [Git](https://github.com) - Used as Code Repository
* [Jupyter](https://jupyter.org/) - Used for data science and model traning
* [cuML](https://github.com/rapidsai/cuml) - RAPIDS Machine Learning Library
* [cuDF](https://github.com/rapidsai/cudf) - GPU DataFrame Library
* [NodeJS](https://nodejs.org/en/) - Backend Framework
* [BigQuery](https://cloud.google.com/bigquery/) - Used as a cload data warehouse where it stores the database used
* [AI Platform](https://cloud.google.com/ai-platform/?hl=pt-br) - Used as AI Platform’s integrated tool chain that helps building and running machine learning applications.
* [Heroku](https://www.heroku.com/) - Used as a cload application platform for the demo

## Notebooks

* POC (Final API)
* Training with the least representative sku's 
* Training with the most representative sku's

## Authors

 * Alexandre Faria
 * Erick Yano
 * Felipe Santos de Brito
 * Gabriel Menossi Suriano
 * Lucas Moura de Carvalho 

