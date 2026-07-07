#DEFENSA DE MI PERFIL ANTE ATAQUE DE FUERZA BRUTA.
#LIMITAR LOS INTENTOS DE LOGUEARSE.
#BLOQUEO DE CUENTA.
import time

print('Sistema de seguridad.')
password_correcto="admin1234" # es despues del logueo. Esta contrasena es la que se guarda en la base de datos.
intentos=3

while intentos >0:
    intento= input(f'Te quedan {intentos} intentos - Ingrese password: ')
    if intento==password_correcto:
        print('Acceso Correcto.')
        break
    else:('Password que ingreso es incorrecto.')
    intentos= intentos - 1 #le resto unos de los intentos.

if intentos ==0:
    print("\n Cuenta esta bloqueada.")


