from nis import cat
from numpy import average


#EJERCICIO 1

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate e"""

#Añade el código
partes_textos=text.split('.')
partes_textos

#Define las palabras pista: average, temperature y distance suenan bien
pal_claves=['average','temperature','distance']


#Ciclo for para recorrer la cadena
for sentence in pal_claves:
    for pal_clave in pal_claves:
        if pal_clave in sentence:
            print(sentence)
            break

#Ciclo para cambiar C a Celsius
for sentence in partes_textos:
    for pal_clave in pal_claves:
        if pal_clave in pal_claves:
            print(sentence.replace(" C", "Celsius"))
            break

#EJERCICIO 2

# Datos con los que vas a trabajar
name="Luna"
gravity=0.00612 #in kms
planet= "Tierra"


#Creamos el titulo
titulo="La gravedad de la ",planet," y la ", name

#Creamos la plantilla
datos = f"""{'-'*80} 
Nombre del planeta: {planet} 
Gravedad en {name}: {gravity * 1000} m/s2 
"""
# Unión de ambas cadenas
template = f"""{titulo.title()} 
{datos} 
""" 
print(datos)
# Nuevos datos muestra
planet = 'Marte '
gravedad  = 0.00143
name = 'Ganímedes'
# Comprobamos la plantilla
print(datos)
new_template = """
Datos de Gravedad sobre: {name}

Nombre del planeta: {planet}
Gravedad en {name}: {gravity} m/s2
"""
print(new_template.format(nombre=name, planeta=planet, gravedad=gravedad))
# Pista: print(nueva_plantilla.format(variables))
print(new_template.format(nombre=name, planeta=planet, gravedad=gravedad*1000))