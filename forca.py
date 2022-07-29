import random
from collections import Counter
  
algumasPalavras = '''caneca esfirra sino laranja gato basquete parque'''
  
algumasPalavras = algumasPalavras.split(' ')
# escolha aleatoria de palavra da lista
palavra = random.choice(algumasPalavras)         
  
if __name__ == '__main__':
    print('Adivinhe a palavra')

    for i in palavra:
        print('_', end = ' ')        
    print()

    jogando = True
    adivinhaLetra = ''                
    chances = len(palavra) + 2 #comprimento da palavra + 2 chances
    correto = 0
    estado = 0
    try:
        while (chances != 0) and estado == 0: # estado altera quando a palavra é adivinhada corretamente
            print()
            chances -= 1
  
            try:
                adivinhou = str(input('Digite uma letra: '))
            except:
                print('Digite apenas uma letra!')
                continue
  
            # validando chutes
            if not adivinhou.isalpha():
                print('Digite apenas uma letra')
                continue
            elif len(adivinhou) > 1:
                print('Digite apenas uma única letra')
                continue
            elif adivinhou in adivinhaLetra:
                print('Você já adivinhou essa palavra')
                continue

            # se a letra for adivinhada corretamente
            if adivinhou in palavra:
                k = palavra.count(adivinhou) # k armazena o numero de vezes que a letra adivinhada aparece na palavra
                for _ in range(k):    
                    adivinhaLetra += adivinhou
  
            # imprime a palavra
            for char in palavra:
                if char in adivinhaLetra and (Counter(adivinhaLetra) != Counter(palavra)):
                    print(char, end = ' ')
                    correto += 1
                elif (Counter(adivinhaLetra) == Counter(palavra)): # o jogo termina quando a palavra correta é adivinhada mesmo que ainda tenha chances
                    print("A palavra é: ", end=' ')
                    print(palavra)
                    estado = 1
                    print('Parabéns, você ganhou!')
                    break
                    break # para sair do loop while
                else:
                    print('_', end = ' ')
  
              
  
        # quando é usada todas as chances
        if chances <= 0 and (Counter(adivinhaLetra) != Counter(palavra)):
            print()
            print('Você perdeu. Tente novamente...')
            print('A palavra era {}'.format(palavra))
  
    except KeyboardInterrupt:
        print()
        print('Tente novamente.')
        exit()