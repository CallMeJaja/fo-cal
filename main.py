import os,time
os.system('cls||clear')

def Core():
    
    core = int(input('\nInput Core Number => '))
    DiV = core / 12
    MoD = core % 12
    bulatAtas = round(DiV + 0.5)

    def findTube() :
        if bulatAtas == 1 or bulatAtas == 0:
            print('Biru')
        elif bulatAtas == 2:
            print('Orange')
        elif bulatAtas == 3:
            print('Hijau') 
        elif bulatAtas == 4:
            print('Cokelat')
        elif bulatAtas == 5:
            print('Abu-Abu')
        elif bulatAtas == 6:
            print('Putih')
        elif bulatAtas == 7:
            print('Merah')
        elif bulatAtas == 8:
            print('Hitam')
        elif bulatAtas == 9:
            print('Kuning')
        elif bulatAtas == 10:
            print('Violet')
        elif bulatAtas == 11:
            print('Pink')
        elif bulatAtas == 0 or bulatAtas == 12 or bulatAtas == 13:
            print('Toska')
        return bulatAtas

    def findCore() :
        if MoD == 1:
            print('Biru')
        elif MoD == 2:
            print('Orange')
        elif MoD == 3:
            print('Hijau') 
        elif MoD == 4:
            print('Cokelat')
        elif MoD == 5:
            print('Abu-Abu')
        elif MoD == 6:
            print('Putih')
        elif MoD == 7:
            print('Merah')
        elif MoD == 8:
            print('Hitam')
        elif MoD == 9:
            print('Kuning')
        elif MoD == 10:
            print('Violet')
        elif MoD == 11:
            print('Pink')
        elif MoD == 0 or MoD == 12:
            print('Toska')
        return MoD

    os.system('cls||clear')
    time.sleep(0.2)

    print('===== RESULT COLOR =====')
    print('Warna Tube dan Warna Core dari Core Ke-{} adalah \n'.format(core))
    print('Warna Tube :')
    findTube()
    print('Warna Core :')
    findCore()
    print('===========================')
    q = input('Ingin mencoba lagi ? (yes/no) => ')
    if q == "yes":
        Core()
    elif q == 'no':
        print('Thank You For Use The Tools')
        time.sleep(0.7)
        exit()
def Color():
    print('\n===== ALAT MENCARI CORE DARI WARNA =====')
    colorTube = input('masukan warna tube nya : ')
    colorCore = input('masukan warna core nya : ')

    def tube():
        global tube
        if colorTube == 'biru':
            tube = (1-1)*12
        elif colorTube == 'oren':
            tube = (2-1)*12
        elif colorTube == 'hijau':
            tube = (3-1)*12
        elif colorTube == 'coklat':
            tube = (4-1)*12
        elif colorTube == 'abu-abu':
            tube = (5-1)*12
        elif colorTube == 'putih':
            tube = (6-1)*12
        elif colorTube == 'merah':
            tube = (7-1)*12
        elif colorTube == 'hitam':
            tube = (8-1)*12
        elif colorTube == 'kuning':
            tube = (9-1)*12
        elif colorTube == 'violet':
            tube = (10-1)*12
        elif colorTube == 'pink':
            tube = (11-1)*12
        elif colorTube == 'toska':
            tube = (12-1)*12
        return tube

    def core():
        if colorCore == 'biru':
            core = 1 + tube()
        elif colorCore == 'oren':
            core = 2 + tube()
        elif colorCore == 'hijau':
            core = 3 + tube()
        elif colorCore == 'coklat':
            core = 4 + tube()
        elif colorCore == 'abu-abu':
            core = 5 + tube()
        elif colorCore == 'putih':
            core = 6 + tube()
        elif colorCore == 'merah':
            core = 7 + tube()
        elif colorCore == 'hitam':
            core = 8 + tube()
        elif colorCore == 'kuning':
            core = 9 + tube()
        elif colorCore == 'violet':
            core = 10 + tube()
        elif colorCore == 'pink':
            core = 11 + tube()
        elif colorCore == 'toska':
            core = 12 + tube()
        return core
    os.system('cls||clear')
    time.sleep(0.5)
    print('===== RESULT TOOLS =====')
    print('Core Ke => ',core())
    q = input('\nIngin Mencoba lagi ? (yes/no) => ')
    if q == 'yes':
        Color()
    elif q == 'no':
        time.sleep(0.2)
        print('Thank You For Use Tools')
        time.sleep(0.5)
        exit()

def About():
    os.system('cls||clear')
    time.sleep(0.5)
    print("""
======================[ About EN-GEN ]======================
                
                Name       : EN-GEN
                Version    : 1.0.0
                Date       : 2023-19-01: Purwakarta
                Python Ver : 3.x.x
                OS         : Windows

============================================================
""")
    time.sleep(0.5)
    exit()

def show_menu():

    print(("""
    ===========[ APLIKASI FIBER OPTIC ]==========
    
    \t\t█▀▀ █▄░█ ▄▄ █▀▀ █▀▀ █▄░█
    \t\t██▄ █░▀█ ░░ █▄█ ██▄ █░▀█
    
    =====[ Author : Reza Asriano Maulana ]=======
    =============================================
    """))
    print('[ 1 ] FIND BY CORE')
    print('[ 2 ] FIND BY COLOR')
    print('[ 3 ] About Tools')
    print('[ 4 ] EXIT')
    menu = int(input('CHOOSE OPTION => '))

    if menu == 1:
        Core()
    elif menu == 2:
        Color()
    elif menu == 3:
        About()
    elif menu == 4:
        exit()

if __name__ == "__main__":

    while(True):
        show_menu()