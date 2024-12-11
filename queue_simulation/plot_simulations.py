import matplotlib.pyplot as plt
from simulation import Sistema
from constants import situacoes

# Simular e coletar métricas
lambda_chegada = 2
resultados = []

for situacao in situacoes:
    tempos_medios = []
    desvios_padroes = []
    for _ in range(32):
        sistema = Sistema(lambda_chegada, situacao["tempos_servico"], situacao["distrib_servico"])
        sistema.simular()
        tempo_medio, desvio_padrao = sistema.calcular_metricas()
        tempos_medios.append(tempo_medio)
        desvios_padroes.append(desvio_padrao)
    resultados.append((tempos_medios, desvios_padroes))

# Plotar gráficos comparativos
plt.figure(figsize=(14, 6))

# Gráfico de tempo médio
plt.subplot(1, 2, 1)
for i, (tempos_medios, _) in enumerate(resultados):
    plt.plot(range(1, 33), tempos_medios, label=f"Situação {i+1}: {situacoes[i]['distrib_servico'][0]}")
plt.title("Comparação de Tempo Médio")
plt.xlabel("Execução")
plt.ylabel("Tempo Médio (s)")
plt.legend()

# Gráfico de desvio padrão
plt.subplot(1, 2, 2)
for i, (_, desvios_padroes) in enumerate(resultados):
    plt.plot(range(1, 33), desvios_padroes, label=f"Situação {i+1}: {situacoes[i]['distrib_servico'][0]}")
plt.title("Comparação de Desvio Padrão")
plt.xlabel("Execução")
plt.ylabel("Desvio Padrão (s)")
plt.legend()

plt.tight_layout()
plt.show()
