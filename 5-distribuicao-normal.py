from scipy.stats import norm

# valores normalmente distribuídos com média = 8 e desvio padrão = 2

# probabilidade de escolher um valor menor que 6
print(norm.cdf(6, 8, 2))

# probabilidade de escolher um valor maior que 6
print(norm.sf(6, 8, 2))
print(1 - norm.cdf(6, 8, 2))

# probabilidade de escolher um valor menor que 6 ou maior que 10
print(norm.sf(10, 8, 2) + norm.cdf(6, 8, 2))

# probabilidade de escolher um valor menor que 10 e maior que 8
print(norm.cdf(10, 8, 2) - norm.cdf(8, 8, 2))