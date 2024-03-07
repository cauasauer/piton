import jogos
secreta = "desculpa" 
letraAcert = ["_","_","_","_","_","_","_","_"]
tentativa = 7 
def jogar():
    while tentativa > 0 and  "_" in letraAcert:
        palpite = input('digite uma letra').lower()
        
        if palpite in secreta:
            index = 0
            for letra in secreta:
                if palpite == letra:
                    letraAcert [index] = letra
                index += 1 
        else:
            tentativa -= 1 
            print(f'voce tem {tentativa} tentativas restantes')
        print("_".join(letraAcert))
    if "_" not in letraAcert:
        print('parabens')
    else:
            print(f'voce perdeu, a palavra era {secreta}')
    jogos.escolJogo()

if(__name__=="__main__"):
    jogar()
