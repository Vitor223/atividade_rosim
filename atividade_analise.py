import pandas as pd
import math



# Carregar o arquivo de aeroportos
arquivo = r'C:\Users\vitor\Downloads\atividade_rosim\aeroportos.xls'

df = pd.read_excel(arquivo, skiprows=2)



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


# Função para converter coordenadas de graus, minutos e segundos para graus decimais
def dms_para_dd(graus, minutos, segundos, direcao):
    # Converter para graus decimais
    decimal = graus + (minutos / 60) + (segundos / 3600)
    
    # Ajustar o sinal para Sul e Oeste
    if direcao in ['S', 'W']:
        decimal = -decimal
    
    return decimal

i = 1

for i in range(len(df)):
    # Obter as coordenadas dos aeroportos
    lat1 = dms_para_dd(df['Latitude'][i], df['Latitude.1'][i], df['Latitude.2'][i], df['Latitude.3'][i])
    lon1 = dms_para_dd(df['Longitude'][i], df['Longitude.1'][i], df['Longitude.2'][i], df['Longitude.3'][i])
    
    # Calcular a distância entre os aeroportos
    for j in range(i+1, len(df)):
        lat2 = dms_para_dd(df['Latitude'][j], df['Latitude.1'][j], df['Latitude.2'][j], df['Latitude.3'][j])
        lon2 = dms_para_dd(df['Longitude'][j], df['Longitude.1'][j], df['Longitude.2'][j], df['Longitude.3'][j])
        
        distance = haversine(lat1, lon1, lat2, lon2)
        
        print(f'Distância entre {df["Aeroporto"][i]} e {df["Aeroporto"][j]}: {distance:.2f} km')
        
    i += 1

