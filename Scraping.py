import re
import requests

def obtener_tecnologias(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            tecnologias = []

            # Expresiones regulares para buscar patrones de tecnologías
            patrones = {
                "Python": r"Python/[0-9]+\.[0-9]+",
                "Django": r"Django/[0-9]+\.[0-9]+",
                # Agrega más patrones según las tecnologías que estés buscando
            }

            for tecnologia, patron in patrones.items():
                version = re.search(patron, content)
                if version:
                    tecnologias.append((tecnologia, version.group()))

            return tecnologias
        else:
            print("No se pudo obtener el contenido de la página")
    except requests.RequestException as e:
        print("Error durante la solicitud:", e)

if __name__ == "__main__":
    sitio_web = input("Ingresa la URL del sitio web: ")

    tecnologias_encontradas = obtener_tecnologias(sitio_web)
    if tecnologias_encontradas:
        print("Tecnologías encontradas:")
        for tecnologia, version in tecnologias_encontradas:
            print(f"{tecnologia}: {version}")
    else:
        print("No se encontraron tecnologías.")
