import csv # manejador de csv.

salida = "./hoteles.csv"  #Aqui se guarda el resultado del programa
entrada = "./Datafiniti_Hotel_Reviews.csv" #Establece el archivo con el que se trabajara

openF1 = open(salida, "w+") #ABRE EL ARCHIVO
openF2 = open(entrada, encoding="ISO-8859-1") #LEE EL ARCHIVO.

csvW = csv.writer(openF1); #Crea el archivo de escritura o lo abre si ya está hecho.
csvR = csv.reader(openF2, delimiter=',') #Abre el archivo de Lectura

csvW.writerow(["review","rating","architecture","environmental","general_food","personal_care_and_beauty","television","score_tag","agreement","confidence","objectivity","irony"]) #Estos headers escriben las columnas
#ScoreTag Positive or Negaitive .
#AGREEMENT Desagreement o Agremeent.
#Confidence % of confidence of the text.
#Objectivity boolean,
#Irony #boolean

next(csvR) #Se salta la primera linea que es la de los nombres de las columnas.
for row in csvR:

    review = row[0]
    rating = row[1]
    architecture = row[2]
    environmental = row[3]
    general_food = row[4]
    personal_care_and_beauty = row[5]
    television = row[6]
    data['txt'] = review
    response = requests.request("POST", url, headers=headers, data=data)
    jsonify = response.json()

    ##Review,Rating,architecture,environmental,general_food,personal_care_and_beauty,television

    score_tag = jsonify.get("score_tag")
    agreement = jsonify.get("agreement")
    confidence = jsonify.get("confidence")
    objectivity = jsonify.get("subjectivity")
    irony = jsonify.get("irony")

    csvW.writerow([review,rating,architecture,environmental,general_food,personal_care_and_beauty,television,score_tag, agreement, confidence, objectivity, irony])

    time.sleep(.60)

openF1.close()
openF2.close()