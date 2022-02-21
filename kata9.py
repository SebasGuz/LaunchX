#kata 9 
# Ejercicio 1

def reporte(tanque_1, tanque_2, tanque_3):
    total_average = (tanque_1 + tanque_2 + tanque_3) / 3
    return f"""Reporte de Gasolina:
    Promedio de todos los tanques: {total_average}%
    Tanque 1: {tanque_1}%
    Tanque 2: {tanque_2}%
    Tanque 3: {tanque_3}% 
    """
print(reporte(60, 50, 70))

    
def promedio(values):
    total = sum(values)
    no_de_elementos= len(values)
    return total / no_de_elementos

promedio([20, 60, 85])

def reporte(tanque_1, tanque_2, tanque_3):
    
    return f"""Reporte de Gasolina:
    Promedio de todos los tanques: {promedio([tanque_1, tanque_2, tanque_3])}%
    Tanque 1: {tanque_1}%
    Tanque 2: {tanque_2}%
    Tanque 3: {tanque_3}% 

    """

print(reporte(40, 50, 100))


    
#Ejercicio 2

# Función con un informe preciso de la misión. 
# Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo
# y tanque interno
def reporte_mision(prelanzamiento,tiempo_vuelo, destino, tanque_externo, tanque_interno):
    return f"""
    Misión para {destino}
    Tiempo de viaje total: {prelanzamiento + tiempo_vuelo} minutos
    Gasolina restante: {tanque_externo + tanque_interno} galones
"""
print(reporte_mision(10, 20, "Marte", 40000, 50000))


def mission_report(destino, *minutos, **gasolina):
    return f"""
    Mission a {destino}
    Tiempo total de viaje: {sum(minutos)} minutos
    Gasolina restante: {sum(gasolina.values())}
    """

print(mission_report("Marte", 10, 10, 70, main=800000, external=100000))

def reporte_mision(destino, *minutos, **gasolina):
    reporte = f"""
    Mission to {destino}
    Total travel time: {sum(minutos)} minutes
    Total fuel left: {sum(gasolina.values())}
    """
    for tank_name, gallons in gasolina.items():
        reporte += f" tanque {tank_name} --> {gallons} gallones restantes\n"
    return reporte

print(reporte_mision("Jupiter", 10, 15, 70, principal=300000, externo=200000))