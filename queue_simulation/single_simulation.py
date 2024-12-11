from simulation import Sistema
from constants import situacoes

# Simular e coletar métricas
lambda_chegada = 2
for i, situacao in enumerate(situacoes, 1):
    sistema = Sistema(lambda_chegada, situacao["tempos_servico"], situacao["distrib_servico"])
    sistema.simular()
    tempo_medio, desvio_padrao = sistema.calcular_metricas()
    print(f"Situação {i}:")
    print(f"  Tempo médio no sistema: {tempo_medio:.4f}s")
    print(f"  Desvio padrão: {desvio_padrao:.4f}s\n")
