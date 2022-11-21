# ST263: Tópicos Especiales en Telemática
Students: Pascual Gómez, pgomezl@eafit.edu.co

Professor: Edwin Montoya, emontoya@eafit.edu.co

## Lab 6: Wordcount en Apache Spark EN AWS EMR 6.3.1
En un cluster EMR se ejecutó el wordcount usando pyspark tomando datos desde S3, HDFS y también mediante el uso de JupyterHub Notebooks.

## 1. Wordcount en EMR con HDFS

### HDFS con datasets cargados:
<img width="514" alt="hdfs-data" src="https://user-images.githubusercontent.com/97640805/202962621-52018646-97f0-4c42-a98a-cfabef04e358.PNG">

### Locación del resultado del wordcount
<img width="495" alt="hdfs-result-location" src="https://user-images.githubusercontent.com/97640805/202962673-10d1f85b-e3c8-404d-9482-1059838e0f27.PNG">

### Resultado el wordcount
<img width="947" alt="hdfs-result-file" src="https://user-images.githubusercontent.com/97640805/202962679-aa05dec8-2acf-404f-9b92-19edd3924b53.PNG">

## 2. Wordcount en EMR con S3

### S3 con datasets cargados:
<img width="696" alt="s3-datasets-locations" src="https://user-images.githubusercontent.com/97640805/202963038-cfa7c30a-6108-42db-abf1-b61a1f9b14a3.PNG">

### Locación del resultado del wordcount
<img width="724" alt="s3-result-location" src="https://user-images.githubusercontent.com/97640805/202963061-47fcebb3-207b-4181-9342-1f34ab43d2eb.PNG">

### Resultado el wordcount
<img width="446" alt="s3-result" src="https://user-images.githubusercontent.com/97640805/202963127-a2060244-8b66-46ed-b2a1-b27f64a1a2d9.PNG">

## 3. Wordcount en JupyterHub Notebook

#### Dentro del notebook y usando los datos de S3 se ejecutó el wordcount en Jupyter:
<img width="935" alt="jupyter" src="https://user-images.githubusercontent.com/97640805/202964590-3ca4b0ec-6323-4583-9e56-cfa43fcca976.PNG">

## 4. Data_processing_using_PySpark.ipynb

#### Utilizando los datos del archivo sample_data.csv ubicado en S3 (s3://lab6.bucket.pgomezl/datasets/sample_data.csv) se siguieron los pasos:
<img width="693" alt="2-0" src="https://user-images.githubusercontent.com/97640805/202963455-704599fe-e154-4e59-b2d7-f164dd9f5f66.PNG">
<img width="710" alt="2-1" src="https://user-images.githubusercontent.com/97640805/202963463-42f8f0b1-f3a6-4d05-a40d-dad4b3b87330.PNG">
<img width="704" alt="2-2" src="https://user-images.githubusercontent.com/97640805/202963476-09c68ceb-6c5c-405f-b550-6e5d74747e6b.PNG">
<img width="690" alt="2-3" src="https://user-images.githubusercontent.com/97640805/202963488-9983bf14-481b-4352-96e5-d87e23df571f.PNG">



#### version README.md -> 1.0 (2022-noviembre)

