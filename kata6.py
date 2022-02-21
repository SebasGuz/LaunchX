#Kata 6

#Ejercicio 1

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano"]
print('En el sistema solar son :', len(planetas), 'planetas')

planetas.append('Plutón')

print(planetas[-1], ' es el ultimo planeta en el sistema solar')


#Ejercicio 2

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno"]
nom_planeta = input(' Escribe el nombre de un planeta con la primera letra en mayúscula')
buscador_planeta = planetas.index(nom_planeta)
print(f' Estos son los planetas mas cercanos a {nom_planeta}')
print(planetas[0:buscador_planeta])



print(f' estos son los planetas mas alejados de {nom_planeta}')
print(planetas[buscador_planeta + 1:])
