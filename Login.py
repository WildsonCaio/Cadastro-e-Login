import logging
from operator import index

logging.basicConfig(level=logging.DEBUG, filename='ap.log', filemode='a', format= '%(levelname)s - %(message)s - %(asctime)s')

conta = [
    {"usuario": "caio", "senha":'1234'},
    {"usuario": "caiofelipe", "senha":'12'},
    {"usuario": "wildsonk", "senha":'wildson123'}
    ]

def check_usuario(user):
    tem = False
    indice = None
    for i in range(0,len(conta)):
        if conta[i]['usuario'] == user:
            tem = True
            indice = i
        else:
            continue 
    if tem == False:
        return logging.ERROR()  
    else:
        passw = str(input('Digite sua senha. '))
        if passw == conta[indice]['senha']:
            print(f'Bem vindo {user}.')
            logging.info(f'Usuário {user} se conectou.')
        else:
            print('Senha incorreta.')
            logging.error(f'Usuário {user} usou senha incorreta.')      
                


print('Bem Vindo.')

user = str(input('Digite o nome de usuário. '))

try:
    check_usuario(user)
except:
    logging.error(f'Usuário {user} não foi encontrado.')
    print('Usuário não encontrado. ')    



    



