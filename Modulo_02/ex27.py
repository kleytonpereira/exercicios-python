for primo in range(2, 100):
    if primo == 2:
        print(f'{primo}')
    elif primo == 3 or primo == 5 or primo == 7:
        print(f'{primo}')
    elif primo % 2 == 0 or primo % 3 == 0 or primo % 5 == 0 or primo % 7 == 0:
        continue
    else:
        print(f'{primo}')
