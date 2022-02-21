
# Añadir el código necesario para crear una  variable que guarde la velocidad del asteroide
# Escribe una expresión de prueba para calcular si necesita una advertencia
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false

# Un asteroide se acerca y viaja a una velocidad de 49 km/s

from ast import ExtSlice
from sympy import principal_branch


astpel=49
adver=input("Dime que velocidad tiene el asteroide: ")

if adver > 25:
    print("¡Advertencia!, un asteroide viene en camino")
else:
    print("Hay un asteroide, pero no representa ningún problema, tranquilo")

""" Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, 
a veces produce un rayo de luz que se puede ver desde la Tierra. Escribe la lógica condicional que usa declaraciones
if, else, y elif para alertar a las personas de todo el mundo que deben buscar un asteroide en el cielo. 
¡Hay uno que se dirige a la tierra ahora a una velocidad de 19 km/s! """      

# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False

ast= 19
luz=input("Dime la velocidad a la que va el asteroide")

if luz >= 20:
    print("¡Cuidado!, un asteroide entro en la atmosfera de la tierra, deberia verse una luz en cielo ")
else:
    print("Entro un asteroide en la orbita, pero no lo podras ver :() ")

# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.

tam_ast=input("Un nuevo asteroide se aproxima hacia la tierra, ingresa el temaño que tiene en metros: ")
vel_ast=input("Ahora ingresa la velocidad a la que va el asteroide en km: ")


if tam_ast > 25 and vel_ast < 25:
        print("El asteroide es muy grande , y representa un gran peligro, ¡Busca refugio!")
elif vel_ast >= 20:
        print("El asteroide entro a la atmosfera de la tierra, podras ver una luz en el cielo, si se aproxima a ti ¡Corre! :(") 
elif vel_ast<20:
        print("El asteroide entro en la atmosfera de la tierra, pero no lo podras ver aproximarse, ¡Suerte en que no caiga en tu trayectoria!")


