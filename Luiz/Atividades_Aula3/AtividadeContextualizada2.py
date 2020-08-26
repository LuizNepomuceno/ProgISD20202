# Vamos iniciar o trabalho com Confocal

print('Vamos iniciar os trabalhos com o Confocal, você já ligou a CPU, agora siga as regras')
nome = input('Digite seu nome: ')
print("Olá %s, Você precisa ligar o RCT" %(nome))



ligado1 = input("Digite Sim, se o RCT estiver ligado: ")
print(" %s, agora você precisa ligar o Painel de Interruptores" %(nome))
cor = input('Digite a cor do Laser que você vai usar: ')
print("A cor escolhida foi  %s. Lembre-se que os Interruptores, ligam o Laser e a cor deve ser escolhida igualmente pela chave certa, cuidado!" %(cor))

ligado2 = input("Digite Sim, se o Painel de Interruptores estiver ligado: ")
print(" %s, agora você precisa ligar o Joystick" %(nome))
    
ligado1 = 'RTC'
ligado2 = 'Interruptores'
ligado3 = 'Joystick'
print('Estão ligados os {0}, {1} e {2} Agora você tem que ligar o Painel  Argônio'.format(ligado1, ligado2, ligado3))

aviso1 = input('A Luz Verde do Argonio está ligada? ')
print('Quando a luz Verde acender no painel do Argônio. Aguarde aproximadamente 5 minuto. Gire o Dosímetro lentamente até a luz ficar Vemelha. E Pare!')


informe = input('Digite Ok quando ficar Vermelhor ou  Aguarde até a luz verde ficar Vermelha:' )
print('%s, Aguarde...' %(informe))

print('Agora o o Microscopio já pode ser Ligado')

nome2 = input('Digite o nome do Programa do Microscopio: ')
print("Inicializando o Microscopio %s" %(nome2))

print('Prepare sua lamina para colocar no Platina do Microscopio %s' %(nome2))
lam = input('Digite Ok se tudo estiver prondo: ')
print("Então tudo %s, Ajuste o foco, usando o Charriot, Parafuso Macro e Micrométrico" %(lam))

lam2 = input('Digite a Lente Objetiva que irá utilizar neste trabalho: ')
print("A lente Escolhida foi %s" %(lam2))

print('Veja se é a mesma lente que está no revólve do microscopio. Agora é só fazer a aquisição das imagens. Boa Sorte e bom trabalho')
print('Bora Trabalhar...')