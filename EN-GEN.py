#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os,time

input('kamu masih jomblo? [y/n] : ')
time.sleep(0.5)
os.system('cls||clear')
global menu 
menu = 0

def Core(): 
    core = 0
    while True:
        try:
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
        except ValueError:
            print('Input tidak valid. Gunakan angka')
            continue
        else:
            time.sleep(0.2)
            print('\n===== RESULT COLOR =====')
            print('Warna Tube dan Warna Core dari Core Ke-{} adalah \n'.format(core))
            print('Warna Tube :')
            findTube()
            print('Warna Core :')
            findCore()
            print('===========================')
           
         
        q = input('Ingin mencoba lagi ? (yes/no) => ')
        if q == "yes":
            Core()
        elif q == "no":
            return Menu()
            break
            
        
def Menu():
    menu = 0
    while True:
        try:
            time.sleep(0.5)
            menu = int(input('\nPILIH MENU [0. BACK TO MENU] => '))
            if menu == 1 :
                Core()
            elif menu == 2 :
                Color()
            elif menu == 3 :
                About()
            elif menu == 4 :
                exit()
            elif menu == 0 :
                show_menu()
            else:
                print('\n{} TIDAK ADA DI MENU. PILIH MENU 1 SAMPAI 4'.format(menu))
                return Menu()
        except ValueError:
            print('Pilihan anda tidak valid. Gunakan angka')
            print('Pilih menu antara 1 sampai 4')
            continue
        else:
            print('\n{} TIDAK ADA DI MENU. PILIH MENU 1 SAMPAI 4'.format(menu))
            print('Pilih menu antara 1 sampai 4')
            return Menu()
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
    time.sleep(0.5)
    print('\n===== RESULT TOOLS =====')
    print('Core Ke => ',Core())
    q = input('\nIngin Mencoba lagi ? (yes/no) => ')
    if q == 'yes':
        Color()
    elif q == 'no':
        return Menu()
def About():
    time.sleep(0.5)
    print("""
==========================================[ ABOUT EN-GEN ]=================================================
                
                                    Name       : EN-GEN
                                    Version    : 1.0.0
                                    Date       : 2023-19-01: Purwakarta
                                    Python Ver : 3.x
                                    OS         : Windows
                                    Author     : Reza Asriano Maulana
                                    Instagram  : rzaezaae
                                    Github     : CallMeJaja

===========================================================================================================
──────────────────────────────── Donate for support me to upgrade this APP ────────────────────────────────
──────────────────────────────── DANA : 085872792870 | OVO : 081217427056  ────────────────────────────────
===========================================================================================================
""")
    time.sleep(0.5)
    menu = int(input('PILIH MENU [0. BACK TO MENU] => '))
    if menu == 1:
        Core()
    elif menu == 2:
        Color()
    elif menu == 3:
        About()
    elif menu == 4:
        time.sleep(0.5)
        print("""
===========================================================================================================      
=============================[ Terimakasih telah menggunakan aplikasi ini :) ]=============================      
===========================================================================================================    
        """)
        time.sleep(0.5)
        exit()
    elif menu == 0:
        show_menu()
    else:
        print('\n{} TIDAK ADA DI MENU. PILIH MENU 1 SAMPAI 4'.format(menu))
        return Menu()

def show_menu():
    print(("""
====================================[ APILKASI FIBER OPTIK ]====================================
────────────────────────────────────────────────────────────────────────────────────────────────                        

                        _______  __    _        _______  _______  __    _ 
                        |       ||  |  | |      |       ||       ||  |  | |
                        |    ___||   |_| | ____ |    ___||    ___||   |_| |
                        |   |___ |       ||____||   | __ |   |___ |       |
                        |    ___||  _    |      |   ||  ||    ___||  _    |
                        |   |___ | | |   |      |   |_| ||   |___ | | |   |
                        |_______||_|  |__|      |_______||_______||_|  |__|

──────────────────────────────────────────────────────────────────────────────── version 1.0 ──
============================================================================== author : jaja ==
    """))
    print('MENU :\n')
    print('[ 1 ] FIND BY CORE')
    print('[ 2 ] FIND BY COLOR')
    print('[ 3 ] ABOUT TOOLS')
    print('[ 4 ] EXIT')
    menu = 0
    while True:
        try:
            menu = int(input('\nPILIH MENU => '))
            if menu == 1:
                Core()
            elif menu == 2:
                Color()
            elif menu == 3:
                About()
            elif menu == 4:
                time.sleep(0.5)
                print("""
===========================================================================================================      
=============================[ Terimakasih telah menggunakan aplikasi ini :) ]=============================      
===========================================================================================================    
                """)
                time.sleep(1)
                exit()
        except ValueError:
            print('Pilihan anda tidak valid. Gunakan angka')
            print('Pilihan anda tidak valid. Pilih menu antara 1 sampai 4')
            continue
        else:
            print('{} TIDAK ADA DI MENU. PILIH MENU ANTARA 1 SAMPAI 4'.format(menu))
            print('Pilihan anda tidak valid. Pilih menu antara 1 sampai 4')
if __name__ == "__main__":
    while(True):
        show_menu()
