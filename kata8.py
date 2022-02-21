#Kata 8 
# Ejercicio 1

planet = {
    'name': 'Marte',
    'number': 2
}
planet.get('name')
print(planet['name'])
planet.get('number')
print(planet['number'])
# o se puede escribir así

print(f'{planet["name"]} tiene {planet["number"]} lunas')

planet['circunferencia (km)'] = {
    'polar': 6752 ,
    'equatorial': 6792
}
print(f'El planeta {planet["name"]} tiene una circunferencia polar de {planet["circunferencia (km)"]["polar"]} Km y equatorial de {planet["circunferencia (km)"]["equatorial"]} km')

#Ejercicio 2

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
lunas = planet_moons.values()
planets = len(planet_moons.keys())
total_lunas = 0
for luna in planet_moons.values():
    total_lunas = total_lunas + luna

print(f' el total de lunas es de {total_lunas}')

promedio = total_lunas / planets
print(f'{promedio:0.04f}')