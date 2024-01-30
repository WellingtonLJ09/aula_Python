velocidade = 59 #velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 #local onde está o radar 1
RADAR_RANGE = 1 # a distãncia onde o radar pega

#if velocidade > RADAR_1:
#    print('Velocidade carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print('carro multado em radar 1')