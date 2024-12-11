# Relatório de Simulação de Rede de Filas

Autor: Daniel de Sousa da Silva
DRE: 118064962

## Objetivo

Simular uma rede aberta de filas composta por três servidores (S1, S2 e S3) em três situações distintas, analisando o **tempo médio no sistema** e o **desvio padrão do tempo no sistema** após descartar os primeiros 10.000 jobs (fase de _warm-up_) e observar os próximos 10.000 jobs.

## Configurações das Situações Simuladas

1. **Situação 1**: Tempos de serviço determinísticos:

   - S1: 0.4s
   - S2: 0.6s
   - S3: 0.95s

2. **Situação 2**: Tempos de serviço uniformemente distribuídos:

   - S1: Intervalo (0.1s, 0.7s)
   - S2: Intervalo (0.1s, 1.1s)
   - S3: Intervalo (0.1s, 1.8s)

3. **Situação 3**: Tempos de serviço exponencialmente distribuídos:
   - S1: Média 0.4s
   - S2: Média 0.6s
   - S3: Média 0.95s

### Parâmetros Comuns

- Taxa de chegada: $\lambda = 2$ jobs por segundo.
- Cada situação foi simulada 32 vezes para garantir resultados consistentes.

## Resultados Observados

### Situação 1

- **Tempo médio no sistema**: 1.2494s
- **Desvio padrão**: 0.2564s
- **Tempo mínimo no sistema**: 1.0000s
- **Tempo máximo no sistema**: 4.0000s

### Situação 2

- **Tempo médio no sistema**: 1.2468s
- **Desvio padrão**: 0.5113s
- **Tempo mínimo no sistema**: 0.2151s
- **Tempo máximo no sistema**: 5.1222s

### Situação 3

- **Tempo médio no sistema**: 1.2359s
- **Desvio padrão**: 0.9634s
- **Tempo mínimo no sistema**: 0.0106s
- **Tempo máximo no sistema**: 7.8842s

## Análise dos Resultados

1. **Tempos Médios**:

   - O tempo médio no sistema é bem próximo, independente da situação.

2. **Desvio Padrão**:
   - A situação 1 apresenta o menor desvio padrão (0.2564s), o que é esperado pois os tempos de serviço são deterministicos .
   - Já na situação 3, com tempos exponenciais, o desvio padrão foi maior (0.9634s), possivelmente devido à maior variabilidade dos tempos de serviço.
   - A situação 2, com tempos uniformes, também apresentou um desvio padrão relativamente alto (0.5113s), mas ainda inferior à situação 3.

## Análise Gráfica

![Gráficos de simulações](assets/plot_simulations.png)

Os gráficos revelam que o desvio padrão se mantém relativamente estável ao longo das 32 simulações nos três cenários avaliados. Em relação ao **tempo médio no sistema**, observa-se que a **situação 3** apresenta maior variabilidade, conforme indicado pelo gráfico do desvio padrão, enquanto a **situação 1** demonstra maior estabilidade nos resultados.

## Conclusão

Esses resultados confirmam que a escolha da distribuição dos tempos de serviço deve levar em conta os objetivos do sistema: enquanto tempos determinísticos garantem maior previsibilidade, distribuições com maior variabilidade podem ser mais adaptáveis em cenários dinâmicos. A análise contribui para a compreensão do impacto da variabilidade em sistemas de filas, destacando a importância de alinhar a configuração dos servidores com os requisitos de desempenho esperados.
