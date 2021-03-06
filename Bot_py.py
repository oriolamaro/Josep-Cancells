{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Bot.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPMcCHf231hvMSHpMy6gHpG",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/oriolamaro/Josep-Cancells/blob/master/Bot_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "M7Qt3vubMfg7",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OfAv0lWuNRJB",
        "colab_type": "text"
      },
      "source": [
        "import json\n",
        "import requests\n",
        " \n",
        "#Variables para el Token y la URL del chatbot\n",
        "TOKEN = \"931350528:AAHBZuwFTpc3K9WCsseM9klsdQ_0hPvLsjs\" #Cambialo por tu token\n",
        "URL = \"https://api.telegram.org/bot\" + TOKEN + \"/\"\n",
        " \n",
        " \n",
        " \n",
        "def update(offset):\n",
        "    respuesta = requests.get(URL + \"getUpdates\" + \"?offset=\" + str(offset))\n",
        "    #Telegram devolvera todos los mensajes con id IGUAL o SUPERIOR al offset\n",
        " \n",
        " \n",
        "    #Decodificar la respuesta recibida a formato UTF8\n",
        "    mensajes_js = respuesta.content.decode(\"utf8\")\n",
        " \n",
        "    #Convertir el string de JSON a un diccionario de Python\n",
        "    mensajes_diccionario = json.loads(mensajes_js)\n",
        " \n",
        "    #Devolver este diccionario\n",
        "    return mensajes_diccionario\n",
        " \n",
        " \n",
        "def leer_mensaje(mensaje):\n",
        " \n",
        "    texto = mensaje[\"message\"][\"text\"]\n",
        "    persona = mensaje[\"message\"][\"from\"][\"first_name\"]\n",
        "    id_chat = mensaje[\"message\"][\"chat\"][\"id\"]\n",
        "    id_update = mensaje[\"update_id\"]\n",
        " \n",
        "    return id_chat, persona, texto, id_update\n",
        " \n",
        "def enviar_mensaje(idchat, texto):\n",
        "    requests.get(URL + \"sendMessage?text=\" + texto + \"&chat_id=\" + str(idchat))\n",
        " \n",
        " \n",
        " \n",
        "#Variable para almacenar la ID del ultimo mensaje procesado\n",
        "ultima_id = 0\n",
        " \n",
        "while(True):\n",
        "    mensajes_diccionario = update(ultima_id)\n",
        "    for i in mensajes_diccionario[\"result\"]:\n",
        " \n",
        "        idchat, nombre, texto, id_update = leer_mensaje(i)\n",
        " \n",
        "        \n",
        "        if id_update > (ultima_id-1):\n",
        "            ultima_id = id_update + 1\n",
        " \n",
        "        if \"Hola\" in texto:\n",
        "            texto_respuesta = \"Hola, \" + nombre + \"!\"\n",
        "        elif \"Adios\" in texto:\n",
        "            texto_respuesta = \"Hasta pronto!\"\n",
        "        else:\n",
        "            texto_respuesta = \"Has escrito: \\\"\" + texto + \"\\\"\"\n",
        " \n",
        "        #Enviar la respuesta\n",
        "        enviar_mensaje(idchat, texto_respuesta)\n",
        " \n",
        "    #Vaciar el diccionario\n",
        "    mensajes_diccionario = []"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TSpAaDZ6Mgno",
        "colab_type": "code",
        "outputId": "f59735cb-c806-4384-9065-a2e9cde74b22",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 488
        }
      },
      "source": [
        "import json\n",
        "import requests\n",
        " \n",
        "#Variables para el Token y la URL del chatbot\n",
        "TOKEN = \"931350528:AAHBZuwFTpc3K9WCsseM9klsdQ_0hPvLsjs\" #Cambialo por tu token\n",
        "URL = \"https://api.telegram.org/bot\" + TOKEN + \"/\"\n",
        " \n",
        " \n",
        " \n",
        "def update(offset):\n",
        "    #Llamar al metodo getUpdates del bot, utilizando un offset\n",
        "    respuesta = requests.get(URL + \"getUpdates\" + \"?offset=\" + str(offset))\n",
        "    #Telegram devolvera todos los mensajes con id IGUAL o SUPERIOR al offset\n",
        " \n",
        " \n",
        "    #Decodificar la respuesta recibida a formato UTF8\n",
        "    mensajes_js = respuesta.content.decode(\"utf8\")\n",
        " \n",
        "    #Convertir el string de JSON a un diccionario de Python\n",
        "    mensajes_diccionario = json.loads(mensajes_js)\n",
        " \n",
        "    #Devolver este diccionario\n",
        "    return mensajes_diccionario\n",
        " \n",
        " \n",
        "def leer_mensaje(mensaje):\n",
        " \n",
        "    #Extraer el texto, nombre de la persona e id del último mensaje recibido\n",
        "    texto = mensaje[\"message\"][\"text\"]\n",
        "    persona = mensaje[\"message\"][\"from\"][\"first_name\"]\n",
        "    id_chat = mensaje[\"message\"][\"chat\"][\"id\"]\n",
        " \n",
        "    #Calcular el identificador unico del mensaje para calcular el offset\n",
        "    id_update = mensaje[\"update_id\"]\n",
        " \n",
        "    #Devolver las dos id, el nombre y el texto del mensaje\n",
        "    return id_chat, persona, texto, id_update\n",
        " \n",
        "def enviar_mensaje(idchat, texto):\n",
        "    #Llamar el metodo sendMessage del bot, passando el texto y la id del chat\n",
        "    requests.get(URL + \"sendMessage?text=\" + texto + \"&chat_id=\" + str(idchat))\n",
        " \n",
        " \n",
        " \n",
        "#Variable para almacenar la ID del ultimo mensaje procesado\n",
        "ultima_id = 0\n",
        " \n",
        "while(True):\n",
        "    mensajes_diccionario = update(ultima_id)\n",
        "    for i in mensajes_diccionario[\"result\"]:\n",
        " \n",
        "        #Llamar a la funcion \"leer_mensaje()\"\n",
        "        idchat, nombre, texto, id_update = leer_mensaje(i)\n",
        " \n",
        "        #Si la ID del mensaje es mayor que el ultimo, se guarda la ID + 1\n",
        "        if id_update > (ultima_id-1):\n",
        "            ultima_id = id_update + 1\n",
        " \n",
        "        #Generar una respuesta a partir de la informacion del mensaje\n",
        "        if \"Hola\" in texto:\n",
        "            texto_respuesta = \"Hola, \" + nombre + \"!\"\n",
        "        elif \"Adios\" in texto:\n",
        "            texto_respuesta = \"Hasta pronto!\"\n",
        "        else:\n",
        "            texto_respuesta = \"Has escrito: \\\"\" + texto + \"\\\"\"\n",
        " \n",
        "        #Enviar la respuesta\n",
        "        enviar_mensaje(idchat, texto_respuesta)\n",
        " \n",
        "    #Vaciar el diccionario\n",
        "    mensajes_diccionario = []"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36m_make_request\u001b[0;34m(self, conn, method, url, timeout, chunked, **httplib_request_kw)\u001b[0m\n\u001b[1;32m    376\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m  \u001b[0;31m# Python 2.7, use buffering of HTTP responses\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 377\u001b[0;31m                 \u001b[0mhttplib_response\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgetresponse\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbuffering\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    378\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[0;34m:\u001b[0m  \u001b[0;31m# Python 3\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: getresponse() got an unexpected keyword argument 'buffering'",
            "\nDuring handling of the above exception, another exception occurred:\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-1040c0a9d2e9>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     47\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     48\u001b[0m \u001b[0;32mwhile\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 49\u001b[0;31m     \u001b[0mmensajes_diccionario\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0multima_id\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     50\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mmensajes_diccionario\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"result\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     51\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-1-1040c0a9d2e9>\u001b[0m in \u001b[0;36mupdate\u001b[0;34m(offset)\u001b[0m\n\u001b[1;32m     10\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moffset\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m     \u001b[0;31m#Llamar al metodo getUpdates del bot, utilizando un offset\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 12\u001b[0;31m     \u001b[0mrespuesta\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mrequests\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mURL\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;34m\"getUpdates\"\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;34m\"?offset=\"\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moffset\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     13\u001b[0m     \u001b[0;31m#Telegram devolvera todos los mensajes con id IGUAL o SUPERIOR al offset\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/requests/api.py\u001b[0m in \u001b[0;36mget\u001b[0;34m(url, params, **kwargs)\u001b[0m\n\u001b[1;32m     74\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     75\u001b[0m     \u001b[0mkwargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msetdefault\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'allow_redirects'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 76\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0mrequest\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'get'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mparams\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     77\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     78\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/requests/api.py\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(method, url, **kwargs)\u001b[0m\n\u001b[1;32m     59\u001b[0m     \u001b[0;31m# cases, and look like a memory leak in others.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     60\u001b[0m     \u001b[0;32mwith\u001b[0m \u001b[0msessions\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mSession\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0msession\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 61\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0msession\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     62\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     63\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/requests/sessions.py\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)\u001b[0m\n\u001b[1;32m    528\u001b[0m         }\n\u001b[1;32m    529\u001b[0m         \u001b[0msend_kwargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msettings\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 530\u001b[0;31m         \u001b[0mresp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprep\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0msend_kwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    531\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    532\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mresp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/requests/sessions.py\u001b[0m in \u001b[0;36msend\u001b[0;34m(self, request, **kwargs)\u001b[0m\n\u001b[1;32m    641\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    642\u001b[0m         \u001b[0;31m# Send the request\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 643\u001b[0;31m         \u001b[0mr\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0madapter\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrequest\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    644\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    645\u001b[0m         \u001b[0;31m# Total elapsed time of the request (approximately)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/requests/adapters.py\u001b[0m in \u001b[0;36msend\u001b[0;34m(self, request, stream, timeout, verify, cert, proxies)\u001b[0m\n\u001b[1;32m    447\u001b[0m                     \u001b[0mdecode_content\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    448\u001b[0m                     \u001b[0mretries\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmax_retries\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 449\u001b[0;31m                     \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    450\u001b[0m                 )\n\u001b[1;32m    451\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[1;32m    598\u001b[0m                                                   \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtimeout_obj\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    599\u001b[0m                                                   \u001b[0mbody\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mbody\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 600\u001b[0;31m                                                   chunked=chunked)\n\u001b[0m\u001b[1;32m    601\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    602\u001b[0m             \u001b[0;31m# If we're going to release the connection in ``finally:``, then\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36m_make_request\u001b[0;34m(self, conn, method, url, timeout, chunked, **httplib_request_kw)\u001b[0m\n\u001b[1;32m    378\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[0;34m:\u001b[0m  \u001b[0;31m# Python 3\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    379\u001b[0m                 \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 380\u001b[0;31m                     \u001b[0mhttplib_response\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgetresponse\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    381\u001b[0m                 \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    382\u001b[0m                     \u001b[0;31m# Remove the TypeError from the exception chain in Python 3;\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.6/http/client.py\u001b[0m in \u001b[0;36mgetresponse\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m   1354\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1355\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1356\u001b[0;31m                 \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbegin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1357\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mConnectionError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1358\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclose\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.6/http/client.py\u001b[0m in \u001b[0;36mbegin\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    305\u001b[0m         \u001b[0;31m# read until we get a non-100 response\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    306\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 307\u001b[0;31m             \u001b[0mversion\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstatus\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreason\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_read_status\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    308\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mstatus\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0mCONTINUE\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    309\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.6/http/client.py\u001b[0m in \u001b[0;36m_read_status\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    266\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    267\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_read_status\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 268\u001b[0;31m         \u001b[0mline\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreadline\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m_MAXLINE\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"iso-8859-1\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    269\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mline\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0m_MAXLINE\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    270\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mLineTooLong\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"status line\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.6/socket.py\u001b[0m in \u001b[0;36mreadinto\u001b[0;34m(self, b)\u001b[0m\n\u001b[1;32m    584\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    585\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 586\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_sock\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrecv_into\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mb\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    587\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    588\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_timeout_occurred\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.6/ssl.py\u001b[0m in \u001b[0;36mrecv_into\u001b[0;34m(self, buffer, nbytes, flags)\u001b[0m\n\u001b[1;32m   1010\u001b[0m                   \u001b[0;34m\"non-zero flags not allowed in calls to recv_into() on %s\"\u001b[0m \u001b[0;34m%\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1011\u001b[0m                   self.__class__)\n\u001b[0;32m-> 1012\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnbytes\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbuffer\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1013\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1014\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrecv_into\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbuffer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnbytes\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mflags\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.6/ssl.py\u001b[0m in \u001b[0;36mread\u001b[0;34m(self, len, buffer)\u001b[0m\n\u001b[1;32m    872\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Read on closed or unwrapped SSL socket.\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    873\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 874\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_sslobj\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbuffer\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    875\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mSSLError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    876\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0mSSL_ERROR_EOF\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msuppress_ragged_eofs\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.6/ssl.py\u001b[0m in \u001b[0;36mread\u001b[0;34m(self, len, buffer)\u001b[0m\n\u001b[1;32m    629\u001b[0m         \"\"\"\n\u001b[1;32m    630\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mbuffer\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 631\u001b[0;31m             \u001b[0mv\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_sslobj\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbuffer\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    632\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    633\u001b[0m             \u001b[0mv\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_sslobj\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sYhJKLsdG24Q",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import json\n",
        "import requests\n",
        " \n",
        "#Variables para el Token y la URL del chatbot\n",
        "TOKEN = \"1194187317:AAH76qSWKaRc3LYzNoIsvP6b5zxEqzroYgM\" #Cambialo por tu token\n",
        "URL = \"https://api.telegram.org/bot\" + TOKEN + \"/\"\n",
        " \n",
        " \n",
        " \n",
        "def update(offset):\n",
        "    #Llamar al metodo getUpdates del bot, utilizando un offset\n",
        "    respuesta = requests.get(URL + \"getUpdates\" + \"?offset=\" + str(offset))\n",
        "    #Telegram devolvera todos los mensajes con id IGUAL o SUPERIOR al offset\n",
        " \n",
        " \n",
        "    #Decodificar la respuesta recibida a formato UTF8\n",
        "    mensajes_js = respuesta.content.decode(\"utf8\")\n",
        " \n",
        "    #Convertir el string de JSON a un diccionario de Python\n",
        "    mensajes_diccionario = json.loads(mensajes_js)\n",
        " \n",
        "    #Devolver este diccionario\n",
        "    return mensajes_diccionario\n",
        " \n",
        " \n",
        "def leer_mensaje(mensaje):\n",
        " \n",
        "    #Extraer el texto, nombre de la persona e id del último mensaje recibido\n",
        "    texto = mensaje[\"message\"][\"text\"]\n",
        "    persona = mensaje[\"message\"][\"from\"][\"first_name\"]\n",
        "    id_chat = mensaje[\"message\"][\"chat\"][\"id\"]\n",
        " \n",
        "    #Calcular el identificador unico del mensaje para calcular el offset\n",
        "    id_update = mensaje[\"update_id\"]\n",
        " \n",
        "    #Devolver las dos id, el nombre y el texto del mensaje\n",
        "    return id_chat, persona, texto, id_update\n",
        " \n",
        "def enviar_mensaje(idchat, texto):\n",
        "    #Llamar el metodo sendMessage del bot, passando el texto y la id del chat\n",
        "    requests.get(URL + \"sendMessage?text=\" + texto + \"&chat_id=\" + str(idchat))\n",
        " \n",
        " \n",
        " \n",
        "#Variable para almacenar la ID del ultimo mensaje procesado\n",
        "ultima_id = 0\n",
        " \n",
        "while(True):\n",
        "    mensajes_diccionario = update(ultima_id)\n",
        "    for i in mensajes_diccionario[\"result\"]:\n",
        " \n",
        "        #Llamar a la funcion \"leer_mensaje()\"\n",
        "        idchat, nombre, texto, id_update = leer_mensaje(i)\n",
        " \n",
        "        #Si la ID del mensaje es mayor que el ultimo, se guarda la ID + 1\n",
        "        if id_update > (ultima_id-1):\n",
        "            ultima_id = id_update + 1\n",
        " \n",
        "        #Generar una respuesta a partir de la informacion del mensaje\n",
        "        if \"Hola\" in texto:\n",
        "            texto_respuesta = \"Hola, \" + nombre + \"!\" + \"  Veig que ja saps com parlar amb mi.  Necessites res?\"\n",
        "        elif \"hola\" in texto:\n",
        "            texto_respuesta = \"Hola, \" + nombre + \"!\" + \"  Veig que ja saps com parlar amb mi.  Necessites res?\"\n",
        "        elif \"Adéu\" in texto:\n",
        "            texto_respuesta = \"Fins després!\"\n",
        "        elif \"Adeu\" in texto:\n",
        "            texto_respuesta = \"Fins després!\"\n",
        "        elif \"he anat\" in texto:\n",
        "            texto_respuesta = \"A on?\"\n",
        "        elif \"Ribes\" in texto:\n",
        "            texto_respuesta = \"Molt bé!  Espero que t'agradés, a mi, m'agrada molt.  Ara et recomano que vagis a la casella I7\"\n",
        "        elif \"ribes\" in texto:\n",
        "            texto_respuesta = \"Molt bé!  Espero que t'agradés, a mi, m'agrada molt.  Ara et recomano que vagis a la casella I7\"\n",
        "        elif \"Dòrria\" in texto:\n",
        "            texto_respuesta = \"Ja comences a controlar eh?!  Ara vés tres caselles a la dreta des d'on ets!\"\n",
        "        elif \"Dorria\" in texto:\n",
        "            texto_respuesta = \"Ja comences a controlar eh?!  Ara vés tres caselles a la dreta des d'on ets!\" \n",
        "        elif \"dòrria\" in texto:\n",
        "            texto_respuesta = \"Ja comences a controlar eh?!  Ara vés tres caselles a la dreta des d'on ets!\"\n",
        "        elif \"dorria\" in texto:\n",
        "            texto_respuesta = \"Ja comences a controlar eh?!  Ara vés tres caselles a la dreta des d'on ets!\"\n",
        "        elif \"Pardines\" in texto:\n",
        "            texto_respuesta = \"Potser voltaràs per tota la vall de Ribes...  Però ara vés dos caselles més a la dreta\"\n",
        "        elif \"pardines\" in texto:\n",
        "            texto_respuesta = \"Potser voltaràs per tota la vall de Ribes...  Però ara vés dos caselles més a la dreta\"\n",
        "        elif \"Planoles\" in texto:\n",
        "            texto_respuesta = \"Molt bé!  Ara vés una casella cap abaix!\"\n",
        "        elif \"planoles\" in texto:\n",
        "            texto_respuesta = \"Molt bé!  Ara vés una casella cap abaix!\"\n",
        "        elif \"Nevà\" in texto:\n",
        "            texto_respuesta = \"Si et desplaces tres caselles cap a l'esquerra, arribaràs al poble on és el cofre!!!\"\n",
        "        elif \"Neva\" in texto:\n",
        "            texto_respuesta = \"Si et desplaces tres caselles cap a l'esquerra, arribaràs al poble on és el cofre!!!\"\n",
        "        elif \"nevà\" in texto:\n",
        "            texto_respuesta = \"Si et desplaces tres caselles cap a l'esquerra, arribaràs al poble on és el cofre!!!\"\n",
        "        elif \"neva\" in texto:\n",
        "            texto_respuesta = \"Si et desplaces tres caselles cap a l'esquerra, arribaràs al poble on és el cofre!!!\"\n",
        "        elif \"quina església\" in texto:\n",
        "            texto_respuesta = \"Tu no busques l'església, tu busques un número!  I el que necessites és el 7!\"\n",
        "        elif \"quina esglesia\" in texto:\n",
        "            texto_respuesta = \"Tu no busques l'església, tu busques un número!  I el que necessites és el 7!\"\n",
        "        elif \"ni bous ni nines\" in texto:\n",
        "            texto_respuesta = \"En els temps que vivim, si hi juguen fins els 10 ja és molt, per tant el número que necessites és el 10!\"\n",
        "        elif \"sou cobra\" in texto:\n",
        "            texto_respuesta = \"El cònsol de pardines cobra dues dobles, però dues dobles poden ser 2X2, així doncs, el número que necessites ara, és el 4!\"\n",
        "        elif \"pagaràs\" in texto:\n",
        "            texto_respuesta = \"Pagaré amb monedes, es clar!  Però has de saber que la paraula MONEDES té 7 lletres, per tant necessites el 7!\"\n",
        "        elif \"pagaras\" in texto:\n",
        "            texto_respuesta = \"Pagaré amb monedes, es clar!  Però has de saber que la paraula MONEDES té 7 lletres, per tant necessites el 7!\"\n",
        "        elif \"càtar amagat\" in texto:\n",
        "            texto_respuesta = \"El càtar amagat es deia Hug no?  Doncs Hug té tres lletres així que el número que necessites ara és el 3!\"\n",
        "        elif \"catar amagat\" in texto:\n",
        "            texto_respuesta = \"El càtar amagat es deia Hug no?  Doncs Hug té tres lletres així que el número que necessites ara és el 3!\"\n",
        "        elif \"Toses\" in texto:\n",
        "            texto_respuesta = \"El gentilici dels habitants de Toses és Tosans, però això potser no t'ajudarà gaire!\"\n",
        "        elif \"toses\" in texto:\n",
        "            texto_respuesta = \"El gentilici dels habitants de Toses és Tosans, però això potser no t'ajudarà gaire!\"\n",
        "        elif \"Campelles\" in texto:\n",
        "            texto_respuesta = \"No confondre amb campanes!\"\n",
        "        elif \"campelles\" in texto:\n",
        "            texto_respuesta = \"No confondre amb campanes!\"\n",
        "        elif \"Queralbs\" in texto:\n",
        "            texto_respuesta = \"Sabies que la Vall de Núria és terme municipal de Queralbs?\"\n",
        "        elif \"queralbs\" in texto:\n",
        "            texto_respuesta = \"Sabies que la Vall de Núria és terme municipal de Queralbs?\"\n",
        "        elif \"Toro\" in texto:\n",
        "            texto_respuesta = \"No confondre amb bou!\"\n",
        "        elif \"toro\" in texto:\n",
        "            texto_respuesta = \"No confondre amb bou!\"\n",
        "        elif \"Bou\" in texto:\n",
        "            texto_respuesta = \"El bou té dues banyes. I tú, quantes en tens?\"\n",
        "        elif \"bou\" in texto:\n",
        "            texto_respuesta = \"El bou té dues banyes. I tú, quantes en tens?\"\n",
        "        elif \"Nina\" in texto:\n",
        "            texto_respuesta = \"Tú ets més de Nancy o de Barbie?\"\n",
        "        elif \"nina\" in texto:\n",
        "            texto_respuesta = \"Tú ets més de Nancy o de Barbie?\"\n",
        "        elif \"Nancy\" in texto:\n",
        "            texto_respuesta = \"A mi sempre m'ha agradat més la Barbie\"\n",
        "        elif \"nancy\" in texto:\n",
        "            texto_respuesta = \"A mi sempre m'ha agradat més la Barbie\"\n",
        "        elif \"Barbie\" in texto:\n",
        "            texto_respuesta = \"A mi sempre m'ha agradat més la Barbie\"\n",
        "        elif \"barbie\" in texto:\n",
        "            texto_respuesta = \"A mi sempre m'ha agradat més la Barbie\"\n",
        "        elif \"Sí\" in texto:\n",
        "            texto_respuesta = \"Sí, què?\"\n",
        "        elif \"Si\" in texto:\n",
        "            texto_respuesta = \"Sí, què?\"\n",
        "        elif \"sí\" in texto:\n",
        "            texto_respuesta = \"Sí, què?\"\n",
        "        elif \"si\" in texto:\n",
        "            texto_respuesta = \"Sí, què?\"\n",
        "        elif \"Núria\" in texto:\n",
        "            texto_respuesta = \"❄⛄🌨\"\n",
        "        elif \"Nuria\" in texto:\n",
        "            texto_respuesta = \"❄⛄🌨\"\n",
        "        elif \"núria\" in texto:\n",
        "            texto_respuesta = \"❄⛄🌨\"\n",
        "        elif \"nuria\" in texto:\n",
        "            texto_respuesta = \"❄⛄🌨\"\n",
        "        elif \"Cafè\" in texto:\n",
        "            texto_respuesta = \"☕☕☕ hahaha!  Has caigut a la trampa!\"\n",
        "        elif \"Cafe\" in texto:\n",
        "            texto_respuesta = \"☕☕☕ hahaha!  Has caigut a la trampa!\"\n",
        "        elif \"cafè\" in texto:\n",
        "            texto_respuesta = \"☕☕☕ hahaha!  Has caigut a la trampa!\"\n",
        "        elif \"cafe\" in texto:\n",
        "            texto_respuesta = \"☕☕☕ hahaha!  Has caigut a la trampa!\"\n",
        "        elif \"/start\" in texto:\n",
        "            texto_respuesta = \"Hola, \" + nombre + \"!\" + \"  Veig que ja saps com parlar amb mi!\"\n",
        "        else:\n",
        "            texto_respuesta = \"Ups no t'he entès!\"\n",
        " \n",
        "        #Enviar la respuesta\n",
        "        enviar_mensaje(idchat, texto_respuesta)\n",
        " \n",
        "    #Vaciar el diccionario\n",
        "    mensajes_diccionario = []"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}