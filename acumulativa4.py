import json
import oracledb

# datos={'nombre':'Ricardo'}        #diccionario json
# # print ("\n")
# # print(datos)

# # print ("\n")
# # print(json.dumps(datos,indent=4))     #se utiliza dumbs para tratar un diccionario como un objeto json

# # datos='{  "nombre":"Ricardo"  }'
# # print (datos)
# # print(json.loads(datos))                #si el diccionario esta como un string se utiliza loads para transformarlo a json


# with open ("nombre.json","w") as archivo: #w de write para guardar datos en json
#     json.dump(datos, archivo)

with open("nombre.json", "r") as archivos:          #r de read para leer los datos de json
    datos=json.load(archivos)
    print(datos)