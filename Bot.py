from flask import Flask
import json
import requests

TOKEN = "751988420:AAHrzn7RXWxVQQNha0tQUzyouE5lUcPde1g" #Cambialo por tu token
URL = "https://api.telegram.org/bot" + TOKEN + "/"
app = Flask(__name__)

def update(offset):
    #Llamar al metodo getUpdates del bot, utilizando un offset
    respuesta = requests.get(URL + "getUpdates" + "?offset=" + str(offset))
    #Telegram devolvera todos los mensajes con id IGUAL o SUPERIOR al offset
 
 
    #Decodificar la respuesta recibida a formato UTF8
    mensajes_js = respuesta.content.decode("utf8")
 
    #Convertir el string de JSON a un diccionario de Python
    mensajes_diccionario = json.loads(mensajes_js)
 
    #Devolver este diccionario
    return mensajes_diccionario
 
 
def leer_mensaje(mensaje):
 
    #Extraer el texto, nombre de la persona e id del último mensaje recibido
    texto = mensaje["message"]["text"]
    persona = mensaje["message"]["from"]["first_name"]
    id_chat = mensaje["message"]["chat"]["id"]
 
    #Calcular el identificador unico del mensaje para calcular el offset
    id_update = mensaje["update_id"]
 
    #Devolver las dos id, el nombre y el texto del mensaje
    return id_chat, persona, texto, id_update
 
def enviar_mensaje(idchat, texto):
    #Llamar el metodo sendMessage del bot, passando el texto y la id del chat
    requests.get(URL + "sendMessage?text=" + texto + "&chat_id=" + str(idchat))
 
 
 
#Variable para almacenar la ID del ultimo mensaje procesado
ultima_id = 0




@app.route('/')
    while(True):
    mensajes_diccionario = update(ultima_id)
    for i in mensajes_diccionario["result"]:
 
        #Llamar a la funcion "leer_mensaje()"
        idchat, nombre, texto, id_update = leer_mensaje(i)
 
        #Si la ID del mensaje es mayor que el ultimo, se guarda la ID + 1
        if id_update > (ultima_id-1):
            ultima_id = id_update + 1
 
        #Generar una respuesta a partir de la informacion del mensaje
        if "Hola" in texto:
            texto_respuesta = "Hola, " + nombre + "!"
        elif "Adios" in texto:
            texto_respuesta = "Hasta pronto!"
        else:
            texto_respuesta = "Has escrito: \"" + texto + "\""
 
        #Enviar la respuesta
        enviar_mensaje(idchat, texto_respuesta)
 
    #Vaciar el diccionario
    mensajes_diccionario = []
    
if __name__ == '__main__':
    app.run