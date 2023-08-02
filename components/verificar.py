def cheia(matriz):
    for element in matriz:
        for num in element:
            if num == '    ':
                return False
            
    return True

def verificar(matriz):
    vasco = ''
    if cheia(matriz) and vasco != 'Vasco' and vasco != 'Csa':
        return 'Deu velha!'
    vasco = 'Vasco'
    if vasco == 'Vasco':
        return 'Vasco'
    return True