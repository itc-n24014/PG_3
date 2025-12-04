print('雨は降っていますか？')
tenki = input()
if tenki == 'yes': # 雨が降っている
    print('傘を持っていますか？')
    kasa = input()
    if kasa == 'yes': # 傘を持っている
        print('外出する')
    else: # 傘がない
        print('しばらく待つ…')
        print('まだ降っている？')
        mada = input()
        if mada == 'yes': # まだ降っている
            print('諦めよう')
        else: # 雨がやんだ
            print('外出する')
else: # 雨が降っていない
    print('外出する')