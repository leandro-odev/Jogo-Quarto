def cheia(matriz):
    for element in matriz:
        for num in element:
            if num == '    ':
                return False
            
    return True

def verificar(matriz):

    #Azul ou vermelha
    horizontal = 0
    while horizontal < 4:
        if 'A' in matriz[horizontal][0] and 'A' in matriz[horizontal][1] and 'A' in matriz[horizontal][2] and 'A' in matriz[horizontal][3]:
            return 'A'
        if 'V' in matriz[horizontal][0] and 'V' in matriz[horizontal][1] and 'V' in matriz[horizontal][2] and 'V' in matriz[horizontal][3]:
            return 'V'
        horizontal += 1
    
    vertical = 0
    while vertical < 4:
        if 'A' in matriz[0][vertical] and 'A' in matriz[1][vertical] and 'A' in matriz[2][vertical] and 'A' in matriz[3][vertical]:
            return 'A'
        if 'V' in matriz[0][vertical] and 'V' in matriz[1][vertical] and 'V' in  matriz[2][vertical] and 'V' in matriz[3][vertical]:
            return 'V'
        vertical += 1
    
    if 'A' in matriz[0][0] and 'A' in matriz[1][1] and 'A' in matriz[2][2] and 'A' in matriz[3][3]:
        return 'A'
    if 'V' in matriz[0][0] and 'V' in matriz[1][1] and 'V' in matriz[2][2] and 'V' in matriz[3][3]:
        return 'V'
    
    #Quadrado ou redondo
    horizontal = 0
    while horizontal < 4:
        if 'Q' in matriz[horizontal][0] and 'Q' in matriz[horizontal][1] and 'Q' in matriz[horizontal][2] and 'Q' in matriz[horizontal][3]:
            return 'Q'
        if 'R' in matriz[horizontal][0] and 'R' in matriz[horizontal][1] and 'R' in matriz[horizontal][2] and 'R' in matriz[horizontal][3]:
            return 'R'
        horizontal += 1
    
    vertical = 0
    while vertical < 4:
        if 'Q' in matriz[0][vertical] and 'Q' in matriz[1][vertical] and 'Q' in matriz[2][vertical] and 'Q' in matriz[3][vertical]:
            return 'Q'
        if 'R' in matriz[0][vertical] and 'R' in matriz[1][vertical] and 'R' in  matriz[2][vertical] and 'R' in matriz[3][vertical]:
            return 'R'
        vertical += 1
    
    if 'Q' in matriz[0][0] and 'Q' in matriz[1][1] and 'Q' in matriz[2][2] and 'Q' in matriz[3][3]:
        return 'Q'
    if 'R' in matriz[0][0] and 'R' in matriz[1][1] and 'R' in matriz[2][2] and 'R' in matriz[3][3]:
        return 'R'

    #Grande ou pequena
    horizontal = 0
    while horizontal < 4:
        if 'G' in matriz[horizontal][0] and 'G' in matriz[horizontal][1] and 'G' in matriz[horizontal][2] and 'G' in matriz[horizontal][3]:
            return 'G'
        if 'P' in matriz[horizontal][0] and 'P' in matriz[horizontal][1] and 'P' in matriz[horizontal][2] and 'P' in matriz[horizontal][3]:
            return 'P'
        horizontal += 1
    
    vertical = 0
    while vertical < 4:
        if 'G' in matriz[0][vertical] and 'G' in matriz[1][vertical] and 'G' in matriz[2][vertical] and 'G' in matriz[3][vertical]:
            return 'G'
        if 'P' in matriz[0][vertical] and 'P' in matriz[1][vertical] and 'P' in  matriz[2][vertical] and 'P' in matriz[3][vertical]:
            return 'P'
        vertical += 1
    
    if 'G' in matriz[0][0] and 'G' in matriz[1][1] and 'G' in matriz[2][2] and 'G' in matriz[3][3]:
        return 'G'
    if 'P' in matriz[0][0] and 'P' in matriz[1][1] and 'P' in matriz[2][2] and 'P' in matriz[3][3]:
        return 'P'

    #Furada ou não furada
    horizontal = 0
    while horizontal < 4:
        if 'F' in matriz[horizontal][0] and 'F' in matriz[horizontal][1] and 'F' in matriz[horizontal][2] and 'F' in matriz[horizontal][3]:
            return 'F'
        if 'N' in matriz[horizontal][0] and 'N' in matriz[horizontal][1] and 'N' in matriz[horizontal][2] and 'N' in matriz[horizontal][3]:
            return 'N'
        horizontal += 1
    
    vertical = 0
    while vertical < 4:
        if 'F' in matriz[0][vertical] and 'F' in matriz[1][vertical] and 'F' in matriz[2][vertical] and 'F' in matriz[3][vertical]:
            return 'F'
        if 'N' in matriz[0][vertical] and 'N' in matriz[1][vertical] and 'N' in  matriz[2][vertical] and 'N' in matriz[3][vertical]:
            return 'N'
        vertical += 1
    
    if 'F' in matriz[0][0] and 'F' in matriz[1][1] and 'F' in matriz[2][2] and 'F' in matriz[3][3]:
        return 'F'
    if 'N' in matriz[0][0] and 'N' in matriz[1][1] and 'N' in matriz[2][2] and 'N' in matriz[3][3]:
        return 'N'

    if cheia(matriz):
        return 'Deu velha!'
    return True