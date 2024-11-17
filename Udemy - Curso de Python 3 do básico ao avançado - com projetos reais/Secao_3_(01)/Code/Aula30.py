velocidade = 61 # velocidade atual do carro.
local_carro = 100 # local em que o carro está na estrada.

RADAR_1 = 60 # VELICIDADE MÁXIMA DO RADAR 1.
LOCAL_1 = 100 # LOCAL ONDE O  radar 1 está.
RADAR_RANGE = 1 # A distância onde o radar pega.

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carrou_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carrou_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print(f"A velocidade do carro PASSOU DO RADAR 1 COM {velocidade}km!")

if carrou_passou_radar_1:
    print('Carro passou no radar 1.')

# Multar se ele está entre 99 and 101.
if carro_multado_radar_1:
    print("Carro multado em radar 1.")