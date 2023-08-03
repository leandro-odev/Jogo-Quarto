def cheia(matriz):
    for element in matriz:
        for num in element:
            if num == '    ':
                return False
            
    return True

def verificar(matriz):
    horizontal = 0
    while horizontal < 4:
        if 'A' in (matriz[horizontal][0], matriz[horizontal][1], matriz[horizontal][2], matriz[horizontal][3]):
            return 'A'
        if 'V' in (matriz[horizontal][0], matriz[horizontal][1], matriz[horizontal][2], matriz[horizontal][3]):
            return 'V'
        horizontal += 1
    
    vertical = 0
    while vertical < 4:
        if 'A' in (matriz[0][vertical], matriz[1][vertical], matriz[2][vertical], matriz[3][vertical]):
            return 'A'
        if 'V' in (matriz[0][vertical], matriz[1][vertical], matriz[2][vertical], matriz[3][vertical]):
            return 'V'
        vertical += 1
    
    if 'A' in (matriz[0][0], matriz[1][1], matriz[2][2], matriz[3][3]):
        return 'A'
    if 'V' in (matriz[0][0], matriz[1][1], matriz[2][2], matriz[3][3]):
        return 'V'

