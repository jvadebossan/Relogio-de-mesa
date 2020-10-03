#\n
import os
import datetime
from time import sleep as wait
import keyboard

def despertador():
    clear = lambda: os.system('cls')
    clear()
    print('##############################################')
    print('#                DESPERTADOR                 #')
    print('##############################################')
    print('# [R] relógio [C] cronometro [D] despertador #')
    print('# OBS: APERTE [ESPAÇO] DESLIGAR O DESPERTADOR#')
    print('##############################################')
    print('Exemplo: 13:57')
    horario_despertar = input('digite o horário: ')
    clear = lambda: os.system('cls')
    clear()

    print('##############################################')
    print('#    DESPERTADOR (definido para {})       #'.format(horario_despertar))
    print('##############################################')
    print('# [R] relógio [C] cronometro [D] despertador #')
    print('# OBS: APERTE [ESPAÇO] DESLIGAR O DESPERTADOR#')
    print('##############################################')

    func_despertador = True
    while func_despertador == True:
        hr1 = datetime.datetime.now()
        hr = hr1.strftime("%H:%M")
        if horario_despertar == hr:
            print('plin plin plin plin, deu o horário')
            print('O despertador será reiniciado em 5 segundos...')
            wait(5)
            func_despertador = False
            return despertador()
        
        elif keyboard.is_pressed('space'):
            clear = lambda: os.system('cls')
            clear()
            print('reiniciando despertador')
            wait(3)
            func_despertador = False
            return despertador()

        elif keyboard.is_pressed('c'):
            clear = lambda: os.system('cls')
            clear()
            print('indo para o cronometro')
            wait(3)
            func_despertador = False
            cronometro()

        elif keyboard.is_pressed('r'):
            clear = lambda: os.system('cls')
            clear()
            print('indo para o relogio') 
            wait(3)
            func_despertador = False
            relogio()   

def cronometro():
    clear = lambda: os.system('cls')
    clear()
    print('##############################################')
    print('#                CRONOMETRO                  #')
    print('##############################################')
    print('# [R] relógio [C] cronometro [D] despertador #')
    print('# OBS: APERTE [ESPAÇO] PARA INICIAR E PAUSAR #')
    print('##############################################')
    cronometro_func = True
    numeros_cronometro = 0
    while cronometro_func == True:
        if keyboard.is_pressed('space'):
            while cronometro_func == True:
                clear = lambda: os.system('cls')
                clear()
                print('##############################################')
                print('#                CRONOMETRO                  #')
                print('##############################################')
                print('# [R] relógio [C] cronometro [D] despertador #')
                print('# OBS: APERTE [ESPAÇO] PARA INICIAR E PAUSAR #')
                print('##############################################')
                numeros_cronometro += 1
                print('{} segundos'.format(numeros_cronometro))
                wait(1)
                if keyboard.is_pressed('space'):
                    cronometro_func = False
                    clear = lambda: os.system('cls')
                    clear()
                    print('##############################################')
                    print('#            CRONOMETRO (pausado)            #')
                    print('##############################################')
                    print('# [R] relógio [C] cronometro [D] despertador #')
                    print('# OBS: APERTE "C" PARA REINICIAR O CRONOMETRO#')
                    print('##############################################')
                    cronometro_func2 = True
                    while cronometro_func2 == True:
                        if keyboard.is_pressed('c'):
                            print('reiniciando cronometro')
                            wait(3)
                            return cronometro()
                        elif keyboard.is_pressed('D'):
                            cronometro_func2 = False
                            clear = lambda: os.system('cls')
                            clear()
                            print('indo para o despertador')
                            wait(3)
                            despertador()

                        elif keyboard.is_pressed('R'):
                            cronometro_func2 = False
                            clear = lambda: os.system('cls')
                            clear()
                            print('indo para o relogio')
                            wait(3)
                            relogio()

        elif keyboard.is_pressed('D'):
            clear = lambda: os.system('cls')
            clear()
            print('indo para o despertador') 
            cronometro_func2 = False
            despertador()
            
        elif keyboard.is_pressed('R'):
            clear = lambda: os.system('cls')
            clear()
            print('indo para o relogio') 
            wait(3)
            relogio()   



def relogio():
    relogio_func = True
    while relogio_func == True:
        hr1 = datetime.datetime.now()
        hr = hr1.strftime("%H:%M")
        print('##############################################')
        print('#                 RELÓGIO                   #')
        print('##############################################')
        print('# [R] relógio [C] cronometro [D] despertador #')
        print('#        OBS: APERTE E SEGURE A TECLA        #')
        print('##############################################')
        print('\n')
        print('agora são: ' + hr)
        wait(1)
        clear = lambda: os.system('cls')
        clear()
        if keyboard.is_pressed('c'):
            relogio_func = False
            print('indo para o cronometro')
            wait(3)
            cronometro()

        if keyboard.is_pressed('d'):
            relogio_func = False
            print('indo para o despertador')
            wait(3)
            despertador()
            
        

relogio()