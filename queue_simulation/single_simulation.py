from simulation import Sistema
from constants import situacoes

# Simular e coletar métricas
lambda_chegada = 2
for i, situacao in enumerate(situacoes, 1):
    sistema = Sistema(lambda_chegada, situacao["tempos_servico"], situacao["distrib_servico"])
    sistema.simular()
    tempo_medio, desvio_padrao, tempo_minimo, tempo_maximo = sistema.calcular_metricas()
    print(f"Situação {i}:")
    print(f"  Tempo médio no sistema: {tempo_medio:.4f}s")
    print(f"  Desvio padrão: {desvio_padrao:.4f}s")
    print(f"  Tempo mínimo no sistema: {tempo_minimo:.4f}s")
    print(f"  Tempo máximo no sistema: {tempo_maximo:.4f}s\n")
