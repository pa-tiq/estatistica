import numpy as np
from scipy import stats

jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]
print("Valores: ", jogadores)
print("Média: ", np.mean(jogadores))
print("Mediana: ", np.median(jogadores))

quartis = np.quantile(jogadores, [0,0.25,0.5,0.75,1])
print("Quartis: ",quartis)

# ddof = graus de liberdade
desviopadrao = np.std(jogadores, ddof=1)
print("Desvio Padrão: ",desviopadrao)

# estatísticas detalhadas
print(stats.describe(jogadores))