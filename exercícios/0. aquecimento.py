# aquecimento.py - Execute e complete os comentários

# 1. Qual a diferença entre = e == ?
x = 5
print(5 == x)  # Retorna: __True___ (tipo: _Booleano____)

# 2. O que este código imprime?
nota = 8
situacao = "Aprovado" if nota >= 7 else "Reprovado"
print(situacao)  # _APROVADO____

# 3. Complete o loop para imprimir apenas números pares de 0 a 10:
for n in range(11):
    if n%2 == 0:  # ou not n%2: ou  if n%2 == 0:
        print(n)