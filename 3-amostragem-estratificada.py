import pandas as pd
from sklearn.model_selection import train_test_split

# Amostra estratificada: população está dividida em estratos.
# A amostra precisa ser representativa de todos os estratos proporcionalmente.

iris = pd.read_csv("dados/iris.csv")
print("\nIris População:")
print(iris["class"].value_counts())
# existem 3 classes, e cada classe tem 50 elementos

# iloc[:,0:4] = 3 primeiras colunas, os atributos
# iloc[:,4] = 4ª coluna, as classes
# test_size = vamos selecionar 50% da base de dados
# stratify = a amostra será estratificada com base na classe
x, _, y, _ = train_test_split(
    iris.iloc[:, 0:4], iris.iloc[:, 4], test_size=0.5, stratify=iris.iloc[:, 4]
)
print("\nIris Amostra:")
print(y.value_counts(),"\n")
# 3 classes, e cada classe com 25 elementos
# amostras geradas de outras formas provavelmente ficarão desbalanceadas,
# ou seja, haverão mais elementos de uma classe e menos de outra

##############################################################

infert = pd.read_csv("dados/infert.csv")
print("\Infert População:")
print(infert["education"].value_counts())
# estratificado por educação, existem 3 classes desbalanceadas, com 
# 120, 116 e 12 elementos.# vou estratificar proporcionalmente cada classe.

# iloc[:,2:9] = colunas de atributos
# iloc[:,1] = 1º coluna, education
# test_size = vamos selecionar 40% da base de dados, então o test_size é 0.6
# stratify = a amostra será estratificada com base na coluna education
x1, _, y1, _ = train_test_split(
    infert.iloc[:, 2:9], infert.iloc[:,1], test_size=0.6, stratify=infert.iloc[:,1]
)
print("\nInfert Amostra:")
print(y1.value_counts(),"\n")
# cada estrato teve a mesma chance de aparecer na amostra
# 3 classes de 48, 46 e 5 amostras