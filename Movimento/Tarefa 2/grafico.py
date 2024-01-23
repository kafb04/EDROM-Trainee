import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros do braço robótico
l1 = 10  # Distância entre a base e a junta do cotovelo (10 cm)
l2 = 5   # Distância entre a junta do cotovelo e o ponto vermelho (5 cm)

# Função para calcular as coordenadas do ponto vermelho (cinemática direta)
def calcular_coordenadas(theta1, theta2):
    x = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    y = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)
    return x, y

# Função para calcular os ângulos das juntas (cinemática inversa)
def calcular_angulos(x, y):
    D = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
    theta2 = np.arccos(D)
    theta1 = np.arctan2(y, x) - np.arctan2(l2 * np.sin(theta2), l1 + l2 * np.cos(theta2))
    return theta1, theta2

# Função para animação
def animar(i):
    global theta1, theta2

    # Movimento 5 cm para cima
    nova_y = calcular_coordenadas(theta1, theta2)[1] + 0.05  # Ajuste pequeno para visualização
    theta1, theta2 = calcular_angulos(x, nova_y)

    # Atualizar gráfico
    ponto_vermelho.set_data(*calcular_coordenadas(theta1, theta2))
    linha_braço.set_data([0, l1 * np.cos(theta1), l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)],
                        [0, l1 * np.sin(theta1), l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)])

    return ponto_vermelho, linha_braço

# Configurações iniciais
theta1, theta2 = np.radians(45), np.radians(45)  # Ângulos iniciais
x, y = calcular_coordenadas(theta1, theta2)

# Configurar gráfico
fig, ax = plt.subplots()
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)

# Desenhar o braço robótico
linha_braço, = ax.plot([0, l1 * np.cos(theta1), l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)],
                       [0, l1 * np.sin(theta1), l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)], 'o-')

# Desenhar o ponto vermelho
ponto_vermelho, = ax.plot(*calcular_coordenadas(theta1, theta2), 'ro')

# Criar animação
ani = FuncAnimation(fig, animar, frames=100, interval=100, blit=True)

plt.show()
