import numpy as np
import matplotlib.pyplot as plt

#Aqui trabalhamos com numpy, para uma matemática mais precisa, e matplotlib, para plotar gráficos


# valores importantes para a onda
A= 1  # altura da onda
amplitude = A
frequencia = 2*np.pi # frequência angular, nosso periodo é 1, na questão 5.61

#frequencia=1 # frequência angular da 5.62, o nosso periodo é T=2*pi
 
fase = 0   # deslocamento horizontal, não tem
# começa com K=0, logo a0, é o nosso y inicia
y = 2*A/np.pi 
# quantidade de iterações, ondas vão se somar
N = 5
# eixo x do gráfico
t = np.linspace(0, N, N*1000) # entre 0 e N, teremos N*100 pontos cada um com um valor,quantos mais pontos melhor a defição.

# LOOP PRINCIPAL
for k in range(1, N + 1): 
    #temos uma onda retificada
    y += amplitude *4*np.pi* np.cos(k*t*frequencia)/((np.pi)**2  -(k*frequencia)**2) #5.61
    #y += (4(-1)**k)*np.cos(k*frequencia*t)/k**2   #5.62
# gráfico final
plt.plot(t, y)
questão= "5.61"
plt.title(f"Onda questão {questão}")
plt.xlabel("t")
plt.ylabel("x(t)")

plt.grid(True)

plt.show()