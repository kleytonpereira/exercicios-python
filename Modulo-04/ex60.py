def eh_primo(primo):
    if primo == 2:
        return True
    elif primo == 3 or primo == 5 or primo == 7:
        return True
    elif primo % 2 == 0 or primo % 3 == 0 or primo % 5 == 0 or primo % 7 == 0:
        return False
    else:
        return True
    

assert eh_primo(2) == True, 'É Primo'
assert eh_primo(3) == True, 'É Primo'
assert eh_primo(13) == True, 'É Primo'
assert eh_primo(19) == True, 'É Primo'
assert eh_primo(9) == False, 'Não é Primo'
assert eh_primo(15) == False, 'Não é Primo'
