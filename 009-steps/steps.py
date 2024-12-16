# --> Directions
# Escreve uma função que receba um inteiro positivo N.
# A função deve dar console log de um uma escada
# com o tamanho do inteiro N para sua base e a string
# printada deve ter o N do degrau e o restante em espaços vazios

# --> Exemplo
# steps(5) -->
# '#    '
# '##   '
# '###  '
# '#### '
# '#####'
  
def steps(n):
  if n <= 0: return []
  steps = []
  for i in range(0, n):
    string = "#"*(i+1) + " " * (n - i - 1)
    steps.append(string)
  return steps

print(steps(4))