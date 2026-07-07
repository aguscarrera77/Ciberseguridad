#ransomware: es un archivo que contiene material infectado con un malware y me produce problemas en mi sistema operativo y una gran falla de seguridad. Se manda a traves de archivos que por ej a simple viste la extension es correcta pero en realidad tiene un pequeno cambio que no es de simple deteccion.
#Por ejemplo pdf... pfd / doble extension ..... .pdf.exe 
import time
archivos_recibidos=['foto_vacaciones.jpg','informe_mensual.pdf','premio_ganado.pdf.exe']
#recorro con un for.
for archivo in archivos_recibidos:
    print(f'Analizando archivos: {archivo}')
    time.sleep(1)

    if archivo.endswith('.exe'):
        print(f"WARNING: el archivo {archivo} contiene un ejecutable oculto.BLOQUEADO POR SEGURIDAD.")
    elif archivo.endswith('.pdf') or archivo.endswith(".jpg"):
        print(f'ARCHIVO SEGURO. EL archivo {archivo} puede ser abierto.')
    else: print(f"Advertencia la extension {archivo} desconocida.El archivo es enviado a cuarentena.")

