# --> Directions
# Dada uma string s contendo os caracteres '(', ')', '{', '}', '[', ']'
# determine se o a string é valida.
# Uma string valida é considerada se:
# 1. Se um colchetes aberto é fechado por um do mesmo tipo;
# 2. Os colchetes abertos devem ser fechados na ordem correta;
# 3. Cada colchete aberto corresponde a um do mesmo tipo;

# --> Exemplo
# valid_parentheses('{}') --> True
# valid_parentheses('{]') --> False

def valid_parentheses(s):
  stack = [] # Pilha para armazenar os colchetes abertos
  pairs = {")": "(", "]": "[", "}": "{"} # Mapeamento dos colchetes fechados para os abertos

  for char in s:
    if char in pairs.values():
      # Se um colchete for aberto, adiciona o mesmo a pilha
      stack.append(char)
    elif char in pairs:
      # Se for encontrado um colchete fechado, verifica o topo da pilha
      # e o compara com o seu par no dicionario de colchetes
      if not stack or stack.pop() != pairs[char]:
        return False # Retorna String invalida  
    else:
      return False # Caso não encontre nada 'string vazia' retorna String Invalida
    
  return len(stack) == 0 # Se a stack estiver vazia sem nenhum colchete averto retorna True, se não retorna False
