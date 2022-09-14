# adivinhação de palavras
# claudio imai
# 14/09/2022
# ver1.1
import random

nome = input("Qual o seu nome? ")
print("Boa sorte ! ", nome)
while True:
    palavras = ["laranja", "melancia", "melao", "banana", "uva", "framboesa", "amora", "maca", "graviola", "abacate",
                "goiaba", "kiwi", "tangerina", "frutadoconde", "acerola", "pitanga", "morango", "ponkan", "limao", "pera",
                "carro", "caminhao", "caminhonete", "bicicleta", "moto", "barco", "canoa", "navio", "aviao", "skate",
                "patinete", "monociclo", "triciclo", "caravela", "trator", "helicoptero", "jangada", "onibus", "trem",
                "metro",
                "pudim", "saladadefruta", "bolo", "brigadeiro", "torta", "mousse", "quindin", "docedeleite", "pave",
                "gelatina", "sonho", "sorvete", "flan", "bemcasado", "bombom", "chocolate", "trufa", "alfajores", "pavlova",
                "pedemoleque",
                "abobora", "abobrinha", "alcachofra", "aspargos", "beterraba", "cenoura", "cogumelo", "ervilha", "inhame",
                "pepino", "pimentao", "rabanete", "tomate", "fava", "batatadoce", "beringela", "chuchu", "batata", "cebola",
                "mandioca",
                "cachorro", "gato", "leao", "vaca", "pato", "cavalo", "marreco", "tigre", "panda", "urso", "coelho",
                "capivara", "camondongo", "camelo", "ornitorrinco", "bode", "cabrito", "carneiro", "pavao", "camaleao"]
    palavra = random.choice(palavras)

    print("Adivinhe as letras")
    letras = ''
    chances = 12
    dica = input("\n Se você precisa de uma dica aperte a")
    if dica == "a":
        if palavra in palavras [0:20]:
            print("\n\nVocê pode usar para fazer suco ou até mesmo fazer uma salada, caso não tenha descoberto ainda, é a fruta  \n\n")
        if palavra in palavras [20:40]:
            print("\n\nte leva mais rapido que andar... se ainda n descobriu ...é um meio de transporte \n\n")
        if palavra in palavras [40:60]:
            print("\n\n É gostoso e doce , vem depois da refeição ...um... não sabe ainda? é a sobremesa\n\n")
        if palavra in palavras [60:80]:
            print(
                "\n\ne bom e geralmente tem na sopa.... se não sabe... tem q se alimentar melhor... sao legumes \n\n")
        if palavra in palavras [80:100]:
            print("\n\nÉ um ser vivo, mas não é o homem... é um animal\n\n")

    else:
        print("\n\n	Que coragem, parabéns e boa sorte?\n\n")

    while chances > 0:
        failed = 0
        for char in palavra:
            if char in letras:
                print(char)
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("Você ganhou!!!")
            print("A palavra é: ", palavra)
            break

        letra = input("digite uma letra:")
        letras += letra

        if letra not in palavra:
            chances -= 1
            print("Errado")
            print("Você tem", +chances, 'mais tentativas')

            if chances == 0:
                print("Você perdeu!!!")
    continuar = input("aperte s para sair")
    if continuar == "s":
        break
