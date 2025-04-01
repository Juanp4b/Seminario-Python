# Copie el texto del Zen de Python en una variable e imprima todas las líneas cuya segunda
# palabra comience con una vocal (A, E, I, O, U, a, e, i, o, u).

def splitFilter(text,filtro):
    splitLines = text.split('\n')
    # list = []
    # for line in splitLines:
    #     splitWords = line.split()
    #     if splitWords > 0:
    #         word = splitWords[1]
    #         if word[0] in filtro:
    #             list.append(line)
    
    list = [line for line in splitLines if len(line.split()) > 0 and line.split()[1][0] in filtro]
    return list