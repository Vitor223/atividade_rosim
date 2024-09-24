import pandas as pd
import math
import re



# Carregar o arquivo de aeroportos
Aeroportos = r'aeroportos.xls'

voos = r'VRA_20240916110513.csv'

df = pd.read_excel(Aeroportos, skiprows=2)

print(df2.head())


# Função para calcular a distância entre dois pontos geográficos
def haversine(lat1, lon1, lat2, lon2):
    # Raio da Terra em km
    R = 6371.0
    
    # Converter de graus para radianos
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Diferença de coordenadas
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Fórmula de Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Distância
    distance = R * c
    return distance

def separar_dms(coordenada):
    # Expressão para extrair graus, minutos, segundos e direção
    padrao = r"(\d+)[°\s]+(\d+)['\s]+(\d+)[\"''\s]+([NSWE])"
    match = re.match(padrao, coordenada)

    if match:
        graus = int(match.group(1))
        minutos = int(match.group(2))
        segundos = int(match.group(3))
        direcao = match.group(4)

        if direcao in ['S', 'W']:
            graus = -graus

        return graus, minutos, segundos, direcao

    else:
        raise ValueError(f'Coordenada inválida: {coordenada}')    

# Função para converter coordenadas de graus, minutos e segundos para graus decimais
def dms_para_dd(graus, minutos, segundos, direcao):
    # Converter para graus decimais
    decimal = graus + (minutos / 60) + (segundos / 3600)
    
    # Ajustar o sinal para Sul e Oeste
    if direcao in ['S', 'W']:
        decimal = -decimal
    
    return decimal


# latitude = df[['LATITUDE']]

# for i in range(len(latitude)):
#     medida = separar_dms(latitude['LATITUDE'][i])
#     lat = dms_para_dd(medida[0], medida[1], medida[2], medida[3])


