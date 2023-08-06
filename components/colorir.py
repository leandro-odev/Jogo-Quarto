import colorama

def colorir(var):

    colorama.init()
    
    if 'A' in var:
        #print(colorama.Fore.BLUE + var + colorama.Style.RESET_ALL)
        return colorama.Fore.LIGHTBLUE_EX + var + colorama.Style.RESET_ALL
    elif 'V' in var:
       #print(colorama.Fore.RED + var + colorama.Style.RESET_ALL)
       return colorama.Fore.RED + var + colorama.Style.RESET_ALL
    else:
        #print(' ')
        return '    '