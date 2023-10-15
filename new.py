import requests
import os

os.system("cls")


def buscar_links(query, api_key, cx, cantidad=10):
    enlaces = []
    start = 1

    while len(enlaces) < cantidad:
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}&start={start}"
        
        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                items = data.get('items', [])
                if not items:
                    break  # No hay más resultados disponibles

                for resultado in items:
                    enlaces.append(resultado['link'])
                start += 10  # Avanza a la siguiente página de resultados
            else:
                print("Error al realizar la solicitud a la API")
                break
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            break

    return enlaces[:cantidad]

if __name__ == "__main__":
    archivo_entrada = "dorks.txt"
    archivo_salida = "Results.txt"
    cantidad = int(input("Ingrese la cantidad de enlaces que desea obtener por consulta '5-20': "))
    api_key = "AIzaSyBmF6zNty-LrwAq98R4-OKAwGpkzkfOFb4"  # Reemplaza con tu clave de API de Google
    cx = "81052c80034ed4cb7"  # Reemplaza con el ID de tu motor de búsqueda personalizado

    try:
        with open(archivo_entrada, 'r') as file:
            lineas = file.readlines()
            with open(archivo_salida, 'w') as output_file:
                contador_total = 0  # Inicializa el contador total de enlaces

                for linea in lineas:
                    consulta = linea.strip()  # Elimina espacios en blanco y saltos de línea
                    enlaces = buscar_links(consulta, api_key, cx, cantidad)
                    contador_total += len(enlaces)  # Actualiza el contador total

                    if enlaces:
                        for enlace in enlaces:
                            os.system(f"title Contador: {contador_total}")
                            print(enlace)
                            output_file.write(enlace + '\n')
                            
                            

        print(f"Se han encontrado un total de {contador_total} enlaces y se han guardado en el archivo: {archivo_salida}")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {archivo_entrada}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
