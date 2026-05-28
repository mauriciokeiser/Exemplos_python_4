# pratica_sensores.py
# Contexto real: Filtrar e processar leituras de sensores (valores válidos entre 0-100)

# Dados brutos de um sensor (alguns com erro: -1 ou >100)
leituras_brutas = [23, 45, -1, 67, 105, 34, 89, -1, 56, 78]

# 1. Filtre apenas leituras válidas (0 <= valor <= 100) usando list comprehension
# Sua solução aqui:
leituras_validas = [v for v in leituras_brutas if 0 <= v <= 100]
#leituras_validas = [v for v in leituras_brutas if v >= 0 <= 100] # OS DOIS ESTÃO CERTOS
print(f"Leituras Validas: {leituras_validas}")

# 2. Calcule a média das leituras válidas (use sum(leituras_validas) SOMA e len(leituras_validas) COMPRIMENTO - Quantos elementes possuem na lista)
# Sua solução aqui:

media = sum(leituras_validas) / len(leituras_validas)
print(f"Média: {media:.2f}")
#sum(leituras_validas)
#len(leituras_validas)

# 3. Classifique cada leitura válida como "Baixa" (<40), "Média" (40-70) ou "Alta" (>70)
# Use conditional expression dentro de uma comprehension
# Sua solução aqui:
classificacoes = [
"Baixa" if v < 40 else "Média" if v <= 70 else "Alta"
for v in leituras_validas
]


# 4. BÔNUS: Crie uma lista de tuplas (valor, classificação) apenas para leituras > 50
# Exemplo de saída: [(67, "Média"), (89, "Alta"), (56, "Média"), (78, "Alta")]
# Sua solução aqui:
resultado = [
    (v, "Média" if v <= 70 else "Alta")
    for v in leituras_validas if v > 50
]
print(resultado)