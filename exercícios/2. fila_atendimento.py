# pratica_fila.py
# Contexto real: Sistema simples de fila de atendimento (primeiro a entrar, primeiro a sair)

fila_atendimento = []

# 1. Simule a chegada de 5 clientes (nomes) na fila
# Use append() para adicionar ao final
clientes = ["Ana", "Bruno", "Carla", "Daniel", "Elena"]
# Sua solução aqui:
# Copie os clientes para a fila_atendimento em ordem de chegada:
for cliente in clientes:
    fila_atendimento.append(cliente)

print(f"Fila: {fila_atendimento}")

# 2. Atenda os 2 primeiros clientes (remova do início da fila)
# Dica: pop(0) remove o primeiro elemento
# Sua solução aqui:
#for cliente in clientes:
 #   dois_primeiros = fila_atendimento.pop(0)
fila_atendimento.pop(0)
fila_atendimento.pop(0)


print(f"Fila: {fila_atendimento}")
# 3. Um cliente prioritário chegou! Insira "Fernanda" na frente da fila
# Use insert() para adicionar na posição 0
# Sua solução aqui:
fila_atendimento.insert(0, "Fernanda")

print(f"Fila: {fila_atendimento}")
# 4. Exiba a fila atual com numeração (use enumerate() )
# Exemplo de saída esperada:
# 1. Fernanda
# 2. Carla
# 3. Daniel
# 4. Elena
# Sua solução aqui:
for pos, nome in enumerate(fila_atendimento, start=1):
    print(f"{pos}. {nome}")


# 5. BÔNUS: Verifique se "Ana" ainda está na fila (operador in)
# Sua solução aqui:

if "Ana" in fila_atendimento:
    print("Ana esta na fila")
else:
    print("Ana NÃO esta na fila")

#if fila_atendimento.count("Ana") == 0: # DOIS ESTÃO CERTOS
#    print("Ana não esta na fila")
#else:
#    print("Ana esta na fila")

