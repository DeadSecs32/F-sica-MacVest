''' Cabeçalho 

####    Autor: Gabriel Tomé Silveira    ####
####    contato: silveira.tomeg@usp.br  ####
####    github: @DeadSecs32             ####
####    data: 11/03/2021                ####
####    Marrie Currie Vestibulares      ####
####    Título: Escalas Termométricas   ####

Liscença: Copyright (c) 2021 Gabriel Tomé Silveira

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.

'''

################# Funções principais do programa #######################

def Celsius_F():
    Tc = float(input('valor em °C: '))
    Tf = Tc * 9/5 +32
    print(f'A temperatura de {Tc}°C em °F é: {round(Tf,2)}°F') 

def F_Celsius():
    Tf = float(input('Sua temperatura em °F: '))
    Tc = (Tf - 32) * (5/9) 
    print(f'A temperatura de {Tf}°F em °C é: {round(Tc,2)}°C') 

def Celsius_Kelvin():
    K = float(input('Temperatura em Kelvin: '))
    Tc = K + 273
    print(f'A temperatura de {K}K em °C é de: {round(Tc,2)}') 

def Kelvin_Celsius():
    Tc = float(input('Temperatura em °C: ')) 
    K  = Tc - 273
    print(f'A temperatura  de {Tc}°C em Kelvin é de: {round(K,2)}') 

def Kelvin_F():
    K = float(input(' Temperatura em Kelvin: '))
    Tf = (K - 273.15 ) * (9/5) + 32 
    print(f'A temperatura de {K}K em °F é de: {round(Tf,2)}°F')

def F_Kelvin():
    Tf = float(input('Temperatura em °F: '))
    K = (Tf - 32) * (5/9) + 273.15 
    print(f'A temperatura de {Tf}°F em K é de: {round(K,2)}K') 

#########################################################################

################# Função Principal do programa ##########################

def main():
    print()
    print(' Título: Escalas Termométricas \n Escola: Marrie Currie Vestibulares \n Criador: Gabriel Tomé Silveira \n licença: MIT\n')
    print('---------------------------------------------------------\n')
    print('Vamos começar!')
    print()
    print('Qual escala termométrica você quer converter: \n [1].  °C --> °F \n [2].  °F --> °C \n [3].  °C -->  K \n [4].   K --> °C \n [5].   K --> °F \n [6].  °F -->  K \n [7].   Não quero realizar nem uma operação \n')
    Escalas = int(input('Escolha entre o número de 1 a 7: '))

    if Escalas == 1:
        Celsius_F()
    if Escalas == 2:
        F_Celsius()
    if Escalas == 3:
        Celsius_Kelvin()
    if Escalas == 4:
        Kelvin_Celsius()
    if Escalas == 5:
        Kelvin_F()
    if Escalas == 6:
        F_Kelvin()
    if Escalas == 7: 
        print('Até mais meu amigo...')
        
    continua = input('Você quer continuar no programa?(S/N):\n ')

    while continua == 'S':
        print('Qual escala termométrica você quer converter: \n [1].  °C --> °F \n [2].  °F --> °C \n [3].  °C -->  K \n [4].   K --> °C \n [5].   K --> °F \n [6].  °F -->  K \n [7].   Não quero realizar nem uma operação \n')

        Escalas = int(input('Escolha entre o número de 1 a 7: '))

        if Escalas == 1:
            Celsius_F()
        if Escalas == 2:
            F_Celsius()
        if Escalas == 3:
            Celsius_Kelvin()
        if Escalas == 4:
            Kelvin_Celsius()
        if Escalas == 5:
            Kelvin_F()
        if Escalas == 6:
            F_Kelvin()
        if Escalas == 7:
            print('Estou finalizando')
            break
##########################################################################

################## Importando a Função ###################################
 
main()
