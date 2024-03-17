import pandas as pd
import numpy as np
from math import ceil

# Amostra SIstemática: É escolhido um elemento aleatório, 
# e a partir daí, a cada N elementos um novo elemento é escolhido.

populacao = 150
amostra = 15
k = ceil(populacao/amostra)
# k=10. Quero 15 elementos na amostra, então preciso tirar 1 elemento
# de cada 10 da população.

# defino um valor aleatório r (1<r<k+1) para inicializar a amostra
r = np.random.randint(low=1,high=k+1,size=1)[0]

acumulador = r
sorteados = []
for i in range(amostra):
    sorteados.append(acumulador)
    acumulador += k
print('Elementos sorteados: ',sorteados)
print('Tamanho do array de elementos sorteados: ',len(sorteados))

base = pd.read_csv('dados/iris.csv')
amostra = base.loc[sorteados]
print(amostra)

