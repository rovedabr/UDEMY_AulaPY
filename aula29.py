"""
CONSTANTES - Em maíusculas e não mudam de valor ao longo do código
Muitas condições dentro do If => ruim 
Complexidade de código => ruim
"""

speed = 65 #*velocidade do carro
place_car = 90 #*local onde o carro está na estrada

RADAR_1 = 60
PLACE_1 = 100
RADAR_RANGE = 1

# if speed > RADAR_1:
#     print("A velocidade do carro foi superior ao permitido")

# if place_car >= (PLACE_1 - RADAR_RANGE) and \
#    place_car <= (PLACE_1 + RADAR_RANGE):
#     print("O Carro foi multado no radar 1")

#*============ Refatorando =============

speedOverRadar1 = speed > RADAR_1
speedUnderRadar1 = speed <= RADAR_1

fined_car = place_car >= (PLACE_1 - RADAR_RANGE) and place_car <= (PLACE_1 + RADAR_RANGE)
print(fined_car)

if speedOverRadar1:
    print("O carro passou da velocidade do radar 1")

if speedUnderRadar1:
    print("O carro não passou da velocidade do radar 1")

if fined_car:
    print("O carro foi multado pelo radar 1")