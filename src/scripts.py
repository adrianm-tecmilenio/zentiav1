def get_palabras_from_linea(linea):
    palabras = linea.split(",")
    palabras = [palabra.strip() for palabra in palabras if palabra.strip()]
    palabras = [palabra.strip('"') for palabra in palabras if palabra.strip('"')]
    return palabras


def get_palabras_clave_unicas():
    nombre_archivo = "./src/skilling/skilling_products_with_keywords.csv"
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()

        palabras_clave_unicas = []

        for linea in lineas:
            # Saltar la cabecera
            if linea.startswith("Titulo,"):
                continue
            partes = linea.strip().split(",")
            # Unir los campos que están entre comillas (por si hay comas en los precios o palabras clave)
            campos = []
            campo_actual = ""
            dentro_de_comillas = False
            for parte in partes:
                if parte.startswith('"') and not parte.endswith('"'):
                    dentro_de_comillas = True
                    campo_actual = parte
                elif dentro_de_comillas:
                    campo_actual += "," + parte
                    if parte.endswith('"'):
                        dentro_de_comillas = False
                        campos.append(campo_actual)
                        campo_actual = ""
                else:
                    campos.append(parte)
            if dentro_de_comillas:
                campos.append(campo_actual)
            # El campo de palabras clave es el último
            if len(campos) >= 5:
                palabras_clave = campos[-1]
                palabras = get_palabras_from_linea(palabras_clave)
                for palabra in palabras:
                    if palabra not in palabras_clave_unicas:
                        palabras_clave_unicas.append(palabra)
        
        return sorted(palabras_clave_unicas)

# if __name__ == "__main__":
#     get_palabras_clave_unicas()