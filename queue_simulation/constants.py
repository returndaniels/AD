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

