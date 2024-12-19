# --> Directions
# Sam é um professor na HackerLand University, onde as notas dos alunos
# seguem regras de arredondamento:
# 1. Cada aluno recebe uma nota na faixa de 0 a 100;
# 2. Notas menores que 38 são consideradas reprovações e não são arredondadas;
# 3. Notas iguais ou maiores que 38 são arredondadas para o próximo múltiplo de 5
#    se a diferença entre a nota e o próximo múltiplo for menor que 3;
# 4. Caso a diferença seja maior ou igual a 3, a nota permanece a mesma.

# --> Exemplos
# grading_students([73, 67, 38, 33]) --> [75, 67, 40, 33]
# grading_students([84, 57, 33]) --> [85, 57, 33]
def grading_students(notes: list) -> list:
  arr_graded: list = []

  for grad in notes:
    if grad >= 38:
      multiple = grad + (5 - grad % 5)
      print(grad - multiple)
      if abs(grad - multiple) < 3:
        arr_graded.append(multiple)
      else:
        arr_graded.append(grad)
    else:
      arr_graded.append(grad)

  return arr_graded