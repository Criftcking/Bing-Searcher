
##############################################################################
import requests

# Reemplaza con tu usuario de GitHub y el ID del Gist
usuario = "Criftcking"
gist_id = "36eeb7114e51f8b14c73eb9185c085e3"

# URL del Gist
url = f"https://api.github.com/gists/36eeb7114e51f8b14c73eb9185c085e3/comments"

# Realizar una solicitud GET a la API de GitHub
response = requests.get(url)

#print("Key: "+ response.text)

if response.status_code == 200:
    data = response.json()
    contenido = data[0]["body"]
    print(contenido)
else:
    print(f"Error al acceder al Gist. Código de estado: {response.status_code}")


###################################################################################################