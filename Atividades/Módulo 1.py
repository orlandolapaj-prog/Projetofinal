#Módulo1

# Criar um sistema de verificação para garantir que as regras de classificação indicativa do cinema sejam cumpridas.
Faixa_Etaria_de_idade =int(input("Clinte digite a sua idade:"))

Acompanhante=input("Escreva aqui se você esta acompanhado a idade,( sim ou não):")

if Faixa_Etaria_de_idade >= 16 or Faixa_Etaria_de_idade >= 12 and Acompanhante =="sim":
    print("Acesso permitido")
else:
    print("Acesso negado. A classificação indicativa não foi atendida.")
