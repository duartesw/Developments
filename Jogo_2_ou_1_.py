import os
playagain = 'S'

def f_dois_ou_um(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Por favor, insira apenas números (1 ou 2)")
            continue

        if value <= 0 or value >2:
            print("O numero precisa estar entre 1 e 2")
            continue
        else:
            break
    return value

def f_vencedor(j1,j2,j3):
  if j1==j2 and j1==j3:
    result = 'Houve Empate'
  elif (j1==j2 and j1!=j3):
    result = 'Jogador 3 Ganhou'
  elif (j1==j3 and j1!=j2):
    result = 'Jogador 2 Ganhou'
  elif  (j2==j3 and j3!=j1):
    result = 'Jogador 1 Ganhou'
  print('')
  print(result)
  print('')
  return result

while playagain == 'S' :
  print('')
  player1 = f_dois_ou_um("Jogador 1, escolha um numero entre 1 e 2: ")
  player2 = f_dois_ou_um("Jogador 2, escolha um numero entre 1 e 2: ")
  player3 = f_dois_ou_um("Jogador 3, escolha um numero entre 1 e 2: ")

  f_vencedor(player1,player2,player3)

  playagain = input('Jogar Novamente? (Digite S para Sim e N para Nao): ').upper()
  
  os.system('cls' if os.name == 'nt' else 'clear')
  print('')