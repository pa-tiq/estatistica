import pandas as pd
import numpy as np

base = pd.read_csv('dados/iris.csv')
print(base)
print('(linhas,colunas): ',base.shape)
# nossa base de dados tem 150 linhas e 5 colunas

# Criar amostragem aleatória do conjunto de dados

# Primeiro, definir a seed para que o resultado seja igual, apesar de ser aleatório
np.random.seed(2345)
# 150 elementos, de valor 0 ou 1, com reposição, probabilidade de ser 0 é 70% e ser 1 é 30%
gerador_de_amostra = np.random.choice(a=[0,1], size=150, replace=True, p=[0.7,0.3])
print('linhas do gerador de amostra: ',len(gerador_de_amostra)) # esse gerador de amostra tem o mesmo tamanho que a base de dados
print('quantidade de 1 no gerador de amostra: ',len(gerador_de_amostra[gerador_de_amostra == 1])) # 49 elementos
print('quantidade de 0 no gerador de amostra: ',len(gerador_de_amostra[gerador_de_amostra == 0])) # 101 elementos
# com o gerador de amostra irei gerar a amostra, escolhendo aleatoriamente 49 ou 101 
# elementos dentro do espaço amostral de 150 elementos

amostra = base.loc[gerador_de_amostra == 0]
print(amostra)

