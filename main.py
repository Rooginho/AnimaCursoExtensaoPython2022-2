# Meu primeiro projeto Python!
#
# Print () = comando de saida
print("Alo mundo!")

# Quando quiser guardar uma STRING (frase)
nome = "Roger da Costa"
# Qunado quiser guardar um numero inteiro 
idade = 23

# Exibir o nome na tela (que esta dentro da variavel nome)
print(nome)

#Quando quiser exibir a frase "minha idade é" completando com a variavel da idade
#Print("minha idade é"+idade)
print("Minha idade é " +str (idade)+"anos\n")
print(f"Minha idade é {idade}+anos\n")
print("Minha idade é {}".format(idade)+"anos\n")

#Quando quiser exibir "meu nome é...e tenho...anos " trocando pelas variaveis nome e idade
print("Meu nome é {} e tenho {} anos".format(nome, idade))
