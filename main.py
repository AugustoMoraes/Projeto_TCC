import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Criar o gráfico
plt.plot(x, y)

# Adicionar rótulos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Meu Gráfico')

# Exibir o gráfico
plt.show()
