#Módulo 3

#Simular o acesso ao painel de configurações do terminal, que exige uma senha específica para ser liberado.


Senha="admin_cine2024"

while True:
    Usuario=input("Disgite sua senha:")

    if Senha == Usuario:
        print("Autenticação bem-sucedida.Acesso ao painel liberado")
        break
    else:
         print("Senha incorreta. Tente novamente")