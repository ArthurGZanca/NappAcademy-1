lista_frases = ['Eu gosto de batatas', 'Eu estava andando de moto']
lista_frases += ['Ele estava comendo no restaurante']
lista_frases += ['O cachorro está passeando pelo parque']

# Escreva seu código aqui:
gerundio = ['ando', 'endo', 'indo']
for p in lista_frases:
    palavras = p.split(' ')
    for g in gerundio:
        for palavra in palavras:
            if g in palavra:
                print(palavra)
