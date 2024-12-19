# --> Directions  
# Dada uma string contendo apenas os caracteres 'A' e 'B', determine o número mínimo de remoções 
# necessárias para que não existam caracteres iguais adjacentes na string.  

# --> Exemplo  
# alternating_characters("AABAAB") --> 2  
# alternating_characters("AAAAAB") --> 4
# alternating_characters("BBBBBBBBBB") --> 9
# alternating_characters("") --> 0

def alternating_characters(s: str):
  deletions = 0
  for index in range(len(s) - 1):
    if s[index] == s[index+1]:
      deletions += 1
  return deletions