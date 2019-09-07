def titulo(msg):
    print('-=' * 25)
    print(str(msg).center(50, ' '))
    print('-=' * 25)


def calcArea(altura, largura):
    area = altura * largura
    print(f'A Area Total de um terreno de {altura:.1f}mt x {largura:.1f}mt é de {area:.1f}mt')


titulo('Area de Terreno')

alt = float(input('Informe a Altura em metros: '))
larg = float(input('Informe a Largura em metros: '))

calcArea(alt, larg)
