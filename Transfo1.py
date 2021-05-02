import os
from math import sqrt


values = dict(S=False, U1=False, I1=False,
              MT=False, U2=False, I2=False)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def rappelle():
    print('Version BETA\n'
          'Rappelle:\n'
          '    S: Puissance apparent, VA: Volt Ampère\n'
          '    U: Tension, V: Volt\n'
          '    I: intensiter ou courant, A: Ampère\n'
          '    En monophasé:\n'
          '        S = U . I = 240 * 0.5 = 120VA\n'
          '        U = S / I = 120 / 0.5 = 240V\n'
          '        I = S / U = 120 / 240 = 0.5A\n'
          '    En triphasé\n'
          '        S = U . I * √(3) = 240 * 10 * √(3) = 4156.92VA\n'
          '        U = S / ( I * √(3) ) = 4156.92 / ( 10 * √(3) ) = 240V\n'
          '        I = S / ( U * √(3) ) = 4156.92 / ( 240 * √(3) ) = 10A')

    _input('ASEPC', author=True)


def menu():
    values.update(S=False, U1=False, I1=False,
                  MT=False, U2=False, I2=False)

    print('Version BETA\n'
          'm: Menu          e: EXIT         c: Clear        r: Rappelle\n'
          '1: S (VA)        2: U1 (V)       3: I1 (A)\n'
          '4: tri,mono      5: U2 (V)       6: I2 (A)')
    entre = input('Entrer les numéro des unités connu: ')

    if 'e' in entre:
        exit(0)
    elif 'm' in entre:
        main()
    elif 'c' in entre:
        clear()
        main()
    elif 'r' in entre:
        rappelle()
    elif '0' in entre or '1' in entre or '2' in entre or '3' in entre or '4' in entre or '5' in entre or '6' in entre:
        pass
    else:
        print(f'La valeur {entre} n\'est pas valid seulement de 0 a 6 et non solment de 7 a 9')
        print('Vous devez saisir la nombres celui a cote unités, par exemple. I1 et U1 valent "23 ou 32".')
        print('ou S, U1, U2 est "125 ou 521 ou 512".')

        _input('ASEPC', author=True)

        main()
    return entre


def _input(arg, author=False) -> float:
    if arg == "ASEPC" and author is True:
        input('Appuyer sur entrer pour Continuer...')
        return True

    if author is True:
        entre = input(arg)
    else:
        entre = input(f'Entre la valeur du {arg}: ')

    if 'e' == entre:
        exit(0)
    elif 'm' in entre:
        main()
    elif 'c' in entre:
        clear()
        main()
    elif 'r' in entre:
        rappelle()

    try:
        return float(entre)
    except ValueError:
        print(f'La valeur "{entre}" n\'est pas valide :(')
        if author is True:
            return _input(arg, author=True)
        else:
            return _input(arg)


# noinspection PyTypeChecker
def main():
    _menu = menu()

    def mono_tri():
        if values['MT'] == 1 or values['MT'] == 3:
            pass
        else:
            # noinspection PyTypeChecker
            values['MT'] = _input('Pour le monophasé entrer le numéro 1 si c\'est pour triphasé entrer le numéro 3: ',
                                  author=True)
            mono_tri()

    val1 = {'1': 'S', '2': 'U1', '3': 'I1', '4': 'MT', '5': 'U2', '6': 'I2'}
    val2 = {'1': 'VA', '2': 'V', '3': 'A', '4': 'MT', '5': 'V', '6': 'A'}
    list_entered = []
    for i in val1:
        if i == '4':
            pass
        elif i in _menu:
            values[val1[i]] = _input(val1[i])
            list_entered.append(f'{val1[i]}={values[val1[i]]}{val2[i]}')
    del _menu
    mono_tri()

    # noinspection PyTypeChecker
    def _math():
        if values['MT'] == 1:
            if values['S'] and values['I1'] and not values['U1']:
                values['U1'] = values['S'] / values['I1']
                print(f"U1=S/I1={values['S']}/{values['I1']}={values['U1']}V")

            if values['S'] and values['U1'] and not values['I1']:
                values['I1'] = values['S'] / values['U1']
                print(f"I1=S/U1={values['S']}/{values['U1']}={values['I1']}A")

            if values['I1'] and values['U1'] and not values['S']:
                values['S'] = values['U1'] * values['I1']
                print(f"S=U1*I1={values['U1']}*{values['I1']}={values['S']}VA")

            if values['S'] and values['I2'] and not values['U2']:
                values['U2'] = values['S'] / values['I2']
                print(f"U2=S/I2={values['S']}/{values['I2']}={values['U2']}V")

            if values['S'] and values['U2'] and not values['I2']:
                values['I2'] = values['S'] / values['U2']
                print(f"I2=S/U2={values['S']}/{values['U2']}={values['I2']}A")

            if values['I2'] and values['U2'] and not values['S']:
                values['S'] = values['U2'] * values['I2']
                print(f"S=U2*I2={values['U2']}*{values['I2']}={values['S']}VA")

        else:
            if values['S'] and values['I1'] and not values['U1']:
                values['U1'] = values['S'] / (values['I1'] * sqrt(3))
                print(f"U1=S/(I1*√(3))={values['S']}/({values['I1']}*√(3))={values['U1']}V")

            if values['S'] and values['U1'] and not values['I1']:
                values['I1'] = values['S'] / (values['U1'] * sqrt(3))
                print(f"I1=S/(U1*√(3))={values['S']}/({values['U1']}*√(3))={values['I1']}A")

            if values['I1'] and values['U1'] and not values['S']:
                values['S'] = values['U1'] * values['I1'] * sqrt(3)
                print(f"S=U1*I1*√(3)={values['U1']}*{values['I1']}*√(3)={values['S']}VA")

            if values['S'] and values['I2'] and not values['U2']:
                values['U2'] = values['S'] / (values['I2'] * sqrt(3))
                print(f"U2=S/(I2*√(3))={values['S']}/({values['I2']}*√(3))={values['U2']}V")

            if values['S'] and values['U2'] and not values['I2']:
                values['I2'] = values['S'] / (values['U2'] * sqrt(3))
                print(f"I2=S/(U2*√(3))={values['S']}/({values['U2']}*√(3))={values['I2']}A")

            if values['I2'] and values['U2'] and not values['S']:
                values['S'] = values['U2'] * values['I2'] * sqrt(3)
                print(f"S=U2*I2*√(3)={values['U2']}*{values['I2']}*√(3)={values['S']}VA")

    for i in list_entered:
        print(i)
    _math()
    _math()

    _input('ASEPC', author=True)

    main()


if __name__ == '__main__':
    clear()
    rappelle()
    clear()
    main()
    _input('ASEPC', author=True)
