import numpy as np

# Funções auxiliares para geração de tempos

def exponencial(media):
    return np.random.exponential(media)

def uniforme(inicio, fim):
    return np.random.uniform(inicio, fim)

def deterministico(valor):
    return valor

# Classe para simular o sistema

class Sistema:
    def __init__(self, lambda_chegada, tempos_servico, distrib_servico, num_jobs=20000, warmup=10000):
        self.lambda_chegada = lambda_chegada
        self.tempos_servico = tempos_servico
        self.distrib_servico = distrib_servico
        self.num_jobs = num_jobs
        self.warmup = warmup
        self.chegadas = []
        self.tempos_no_sistema = []

    def gerar_tempo_servico(self, servidor):
        """Gera o tempo de serviço de acordo com a distribuição especificada."""
        if self.distrib_servico[servidor] == 'deterministico':
            return deterministico(self.tempos_servico[servidor])
        elif self.distrib_servico[servidor] == 'uniforme':
            return uniforme(*self.tempos_servico[servidor])
        elif self.distrib_servico[servidor] == 'exponencial':
            return exponencial(self.tempos_servico[servidor])

    def simular(self):
        """Executa a simulação do sistema."""
        # Inicialização
        fila_S1, fila_S2, fila_S3 = [], [], []
        tempo_atual = 0

        # Gerar as chegadas do processo de Poisson
        for _ in range(self.num_jobs):
            tempo_atual += exponencial(1 / self.lambda_chegada)
            self.chegadas.append(tempo_atual)

        # Inicialização de servidores
        servindo_S1 = servindo_S2 = servindo_S3 = None
        fim_servico_S1 = fim_servico_S2 = fim_servico_S3 = 0

        # Processar jobs
        for chegada in self.chegadas:
            # Atualizar estado dos servidores
            if servindo_S1 and chegada >= fim_servico_S1:
                if np.random.rand() < 0.5:
                    fila_S2.append(servindo_S1)
                else:
                    fila_S3.append(servindo_S1)
                servindo_S1 = None

            if servindo_S2 and chegada >= fim_servico_S2:
                if np.random.rand() < 0.2:
                    fila_S2.append(servindo_S2)
                else:
                    self.tempos_no_sistema.append(chegada - servindo_S2)
                servindo_S2 = None

            if servindo_S3 and chegada >= fim_servico_S3:
                self.tempos_no_sistema.append(chegada - servindo_S3)
                servindo_S3 = None

            # Adicionar jobs às filas
            fila_S1.append(chegada)

            # Servir jobs
            if not servindo_S1 and fila_S1:
                servindo_S1 = fila_S1.pop(0)
                fim_servico_S1 = chegada + self.gerar_tempo_servico(0)

            if not servindo_S2 and fila_S2:
                servindo_S2 = fila_S2.pop(0)
                fim_servico_S2 = chegada + self.gerar_tempo_servico(1)

            if not servindo_S3 and fila_S3:
                servindo_S3 = fila_S3.pop(0)
                fim_servico_S3 = chegada + self.gerar_tempo_servico(2)

        # Descartar warm-up
        self.tempos_no_sistema = self.tempos_no_sistema[self.warmup:]

    def calcular_metricas(self):
        """Calcula as métricas pedidas."""
        tempo_medio = np.mean(self.tempos_no_sistema)
        desvio_padrao = np.std(self.tempos_no_sistema)
        return tempo_medio, desvio_padrao

# Configurações para cada situação

situacoes = [
    # Situação 1: tempos determinísticos
    {
        "tempos_servico": [0.4, 0.6, 0.95],
        "distrib_servico": ["deterministico", "deterministico", "deterministico"]
    },
    # Situação 2: tempos uniformes
    {
        "tempos_servico": [(0.1, 0.7), (0.1, 1.1), (0.1, 1.8)],
        "distrib_servico": ["uniforme", "uniforme", "uniforme"]
    },
    # Situação 3: tempos exponenciais
    {
        "tempos_servico": [0.4, 0.6, 0.95],
        "distrib_servico": ["exponencial", "exponencial", "exponencial"]
    }
]

# Simular e coletar métricas

lambda_chegada = 2
for i, situacao in enumerate(situacoes, 1):
    sistema = Sistema(lambda_chegada, situacao["tempos_servico"], situacao["distrib_servico"])
    sistema.simular()
    tempo_medio, desvio_padrao = sistema.calcular_metricas()
    print(f"Situação {i}:")
    print(f"  Tempo médio no sistema: {tempo_medio:.4f}s")
    print(f"  Desvio padrão: {desvio_padrao:.4f}s\n")
