#Módulo 3

#Simular o acesso ao painel de configurações do terminal, que exige uma senha específica para ser liberado.

Usuario=input("Escreva seu nome ")

Senha="admin_cine2024"

while True:

    if Senha == Usuario:
        print("Autenticação bem-sucedida.Acesso ao painel liberado")
        break
else:
    print("Senha incorreta. Tente novamente")
