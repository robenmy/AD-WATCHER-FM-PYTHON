from pymongo import MongoClient
client = MongoClient('localhost', 27017)
#create new database



#create new database
db = client['client-base']
courses = db.course  # colleccion creada


def regisuser(userid,nombre, apellido, empresa, correo, contrasena):
  registro_user = {
  'TableName': 'regUser',
  '_id':   userid,
  'Nombre': nombre,
  'Apellido': apellido,
  'Empresa': empresa,
  'Correo': correo,
  'Contrasena': contrasena
  }
  result = courses.insert_one(registro_user)
  print(result)
  

def regfingerprint(userid_foraneo, anuncio, frecuencia, estacion,horario_array,arrayFin):
  finger ={
  'TableName': 'regfingerprint',
  'UserID_foraneo': userid_foraneo,
  'AudioName': anuncio,
  'Frecuencia': frecuencia,
  'Estacion' : estacion,
  'Horario' : horario_array,
  'Fingerprint': arrayFin
  }
  result = courses.insert_one(finger)
  print(result)


def clientsummary(userid, frecuencia, estacion, adName, date, hora):
    summary = {
    'TableName': 'clientsummary',
    'UserID': userid,
 	'Frecuencia': frecuencia,
 	'Estacion': estacion,
 	'Anuncio': adName,
 	'Fecha': date,
 	'Hora': hora
 	}
    result = courses.insert_one(summary)
    print(result)

def anuncio_horario(hora, minutos, am_pm):
  horario = {
    'Hora': hora,
    'Minutos': minutos,
    'am_pm' : am_pm
  }

  return horario


def busquedaFing(hora, minutos,amPM):

    busquedaResult = courses.find({"Horario": {
    "$elemMatch": {
      "Hora": hora,
      "Minutos": minutos,
      "am_pm": amPM
    }

  }})
    a =[0,0,0,0]
    b=[]
    for i in busquedaResult:

      a[0] = i['UserID_foraneo']
      a[1] = i['AudioName']
      a[2] = i['Frecuencia']
      a[3] = i['Estacion']
      b = list(i['Fingerprint'])

    return a,b



horarios =[]
horarios.append(anuncio_horario('5','4','am'))
horarios.append(anuncio_horario('5','40','pm'))

#regisuser('Robenmy', 'Robenmy','Cepeda', 'Pucmm', 'robenmy@hotmail.com', '1234567')
regfingerprint("Jesus","Tauro Turbo","La calle", "98.3",horarios,"83838383")
#r= courses.find({"_id":"Robenmy","Contrasena":"1234567"})
'''
#if r is not None:
b = []
for a in r:

  print(a)
  b.append(a["_id"])
  b.append(a["Correo"])

if b is not None:
  print(b[1])
else:
  print("no existe")

'''


#a,b =busquedaFing('5', '40','pm')
#print(a)
#print(b)







 
  

