entrada = input("Por favor, ingrese los nombres de los archivos junto con sus respectivas extensiones, en el siguiente formato: 'nombredearchivo.extension', y separelos por espacios (solo se admiten las extensiones: .gif .jpg .jpeg .png .pdf .txt .zip): ")
archivos = entrada.split()
extensiones = ['jpg', 'jpeg', 'pdf', 'txt', 'png', 'zip', 'gif']
tipos_mime = ['image/jpeg', 'image/jpeg', 'application/pdf', 'text/plain', 'image/png', 'application/zip', 'image/gif']
extensiones_archivos = [archivo.lower().split('.')[-1] for archivo in archivos]
tipos_mime_archivos = []
for extension in extensiones_archivos:
    if extension in extensiones:
        indice = extensiones.index(extension)
        tipo_mime = tipos_mime[indice]
        tipos_mime_archivos.append(tipo_mime)
    else:
        tipos_mime_archivos.append('application/octet-stream')
for archivo, tipo_mime in zip(archivos, tipos_mime_archivos):
    print(f"Nombre Archivo: {archivo} - Salida Esperada: {tipo_mime}")