import requests
from bs4 import BeautifulSoup
import os
import concurrent.futures
import colorama
from colorama import Fore, Style

#Inicializa colorama
colorama.init()


# Función para contar y mostrar el número de líneas en el archivo
def contar_lineas():
    with open('totalurls.txt', 'r') as archivo:
        lineas = archivo.readlines()
        numero_de_lineas = len(lineas)
        return numero_de_lineas
        
        
def contar_y_guardar_urls_con_interrogacion():
    urls_con_interrogacion = set()  # Usamos un conjunto para evitar duplicados
    
    # Leer las URLs existentes en 'Results.txt' y agregarlas al conjunto
    with open('Results.txt', 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            urls_con_interrogacion.add(linea.strip())  # Usamos strip para eliminar saltos de línea

    # Obtener nuevas URLs con signo de interrogación y agregarlas al conjunto
    with open('totalurls.txt', 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if '?' in linea:
                urls_con_interrogacion.add(linea.strip())

    # Escribir las URLs únicas en 'Results.txt'
    with open('Results.txt', 'w') as archivo:
        for url in urls_con_interrogacion:
            archivo.write(url + '\n')

    return len(urls_con_interrogacion)





with open("dorks.txt", 'r') as archivo:
    lineas = archivo.readlines()
cantidad_lineas = len(lineas)




# Función para procesar una dork y extraer las URLs
def process_dork(dork):
    
    
    headers = {
        "Host": "www.bing.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "TE": "trailers"
    }

    
    url = f'https://www.bing.com/search?q={dork}&qs=n&form=QBRE&sp=-1&lq=0&pq={dork}'

    try:
        
        # Realizar la solicitud HTTP
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Parsear el contenido HTML de la respuesta
            soup = BeautifulSoup(response.text, 'html.parser')

            # Encontrar todos los elementos 'a' con la clase 'tilk'
            links = soup.find_all('a', class_='tilk')

            # Extraer las URLs de los elementos encontrados
            urls = []
            longitud = 0
            for link in links:
                
                href = link.get('href')
                R = requests.get(url=href)
                ur = R.text
        
                inicio = ur.find('var u = "') + 1
                fin = ur.find('";', inicio)
                valor = ur[inicio:fin]
                valore = valor[8:]
                token = valore
                urls.append(token)
                
                with open("dorks.txt", 'r') as archivo:
                    lineas = archivo.readlines()
                cantidad_lineas = len(lineas)

                
                
                longitud += 1
                os.system(f"title URLS Count:{contar_lineas()}-{contar_y_guardar_urls_con_interrogacion()} Dorks:{cantidad_lineas} ")
                print(token)
                
                
            
                
                with open('totalurls.txt', 'a') as archivo:
                    archivo.write(token + '\n')



            return urls

        else:
            print(f'Error al hacer la solicitud HTTP para la dork "{dork}". Código de estado: {response.status_code}')
            return []

    except Exception as e:
        print(f'Error al procesar la dork "{dork}": {str(e)}')
        return []

if __name__ == "__main__":
    os.system("cls")
    
        # Función para verificar la clave de activación
    def verificar_clave():

        # URL del Gist
        url = f"https://api.github.com/gists/36eeb7114e51f8b14c73eb9185c085e3/comments"

        # Realizar una solicitud GET a la API de GitHub
        response = requests.get(url)

        #print(response.text)

        if response.status_code == 200:
            data = response.json()
            contenido = data[1]["body"]
            print(contenido)

        else:
            print(f"Error al acceder al Gist. Código de estado: {response.status_code}")

        
        
        clave_correcta = contenido  # Reemplaza con tu clave real
        
        try:
            with open("clave_activacion.txt", "r") as archivo:
                clave_guardada = archivo.read().strip()
            if clave_guardada == clave_correcta:
                print("¡Clave de activación válida! El programa está activado.")
                return True
            else:
                
                return False
        except FileNotFoundError:
            return False

    # Función para solicitar y guardar la clave de activación
    def ingresar_clave():
        

        # URL del Gist
        url = f"https://api.github.com/gists/36eeb7114e51f8b14c73eb9185c085e3/comments"

        # Realizar una solicitud GET a la API de GitHub
        response = requests.get(url)

        #print(response.text)

        if response.status_code == 200:
            data = response.json()
            contenido = data[1]["body"]
            
        else:
            print(f"Error al acceder al Gist. Código de estado: {response.status_code}")
            
        clave_correcta = contenido  # Reemplaza con tu clave real
        
        clave_activacion = input(Fore.LIGHTYELLOW_EX+"Por favor, ingrese la (KEY de activación): "+Fore.RESET)
        
        if clave_activacion == clave_correcta:
            print("¡Clave de activación válida! El programa está activado.")
            with open("clave_activacion.txt", "w") as archivo:
                archivo.write(clave_activacion)
            return True
        else:
            print("Clave de activación incorrecta. El programa se cerrará.")
            return False

    if __name__ == "__main__":
        os.system("cls")
        print("Iniciando programa...")
        
        if verificar_clave():
            # Aquí colocarías el código principal del programa
            print("¡Bienvenido al programa activado!")
            os.system("cls")
            
            print(Fore.LIGHTMAGENTA_EX+"""
Nota: Coloca tus dorks en 'dorks.txt' o crea un archivo  
        ____  _                                         _     
        |  _ \(_)                                       | |    
        | |_) |_ _ __   __ _     ___  ___  __ _ _ __ ___| |__  
        |  _ <| | '_ \ / _` |   / __|/ _ \/ _` | '__/ __| '_ \ 
        | |_) | | | | | (_| |   \__ \  __/ (_| | | | (__| | | |
        |____/|_|_| |_|\__, |   |___/\___|\__,_|_|  \___|_| |_|
                        __/ |                           
                        |___/ BTC WALLET: 13MEq6AABjuzHZEprcRWDckS1PijxYNrPN 
                                By @GhostHat_Real | @Criftcking_Real
   
          """+Fore.RESET)
    
            print("Escribe la Cantidad de Bots (5-100)")
            treads = int(input("-------> "))
            print("Iniciando...")
            # Leer las dorks desde un archivo de texto
            with open('dorks.txt', 'r') as file:
                dorks = file.read().splitlines()

            # Usar concurrent.futures para procesar las dorks en paralelo
            with concurrent.futures.ThreadPoolExecutor(max_workers=treads) as executor:
                print("Iniciando contador de líneas...")
                results = list(executor.map(process_dork, dorks))
            
            
            
            
            
            
        else:
            # Si no se pudo verificar la clave, solicitarla al usuario
            if ingresar_clave():
                # Aquí colocarías el código principal del programa
                print("¡Bienvenido al programa activado!")
                os.system("cls")
                print(Fore.LIGHTMAGENTA_EX+"""
Nota: Coloca tus dorks en 'dorks.txt' o crea un archivo  
        ____  _                                         _     
        |  _ \(_)                                       | |    
        | |_) |_ _ __   __ _     ___  ___  __ _ _ __ ___| |__  
        |  _ <| | '_ \ / _` |   / __|/ _ \/ _` | '__/ __| '_ \ 
        | |_) | | | | | (_| |   \__ \  __/ (_| | | | (__| | | |
        |____/|_|_| |_|\__, |   |___/\___|\__,_|_|  \___|_| |_|
                        __/ |                           
                        |___/ BTC WALLET: 13MEq6AABjuzHZEprcRWDckS1PijxYNrPN 
                                By @GhostHat_Real | @Criftcking_Real
   
          """+Fore.RESET)
    
                print("Escribe la Cantidad de Bots (5-100)")
                treads = int(input("-------> "))
                print("Iniciando...")
                # Leer las dorks desde un archivo de texto
                with open('dorks.txt', 'r') as file:
                    dorks = file.read().splitlines()

                # Usar concurrent.futures para procesar las dorks en paralelo
                with concurrent.futures.ThreadPoolExecutor(max_workers=treads) as executor:
                    print("Iniciando contador de líneas...")
                    results = list(executor.map(process_dork, dorks))
                    
        