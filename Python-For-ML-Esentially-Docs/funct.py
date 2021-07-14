def e_potentielle(masse, hauteur, g=9.41, e_limite = 40.43):
    E = masse * hauteur * g
    if(E>=e_limite):
        return True
    else:
        return False

    res = e_potentielle(masse=20, hauteur=0.42)
    print(res)