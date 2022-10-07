""" Uma lista com 5 nomes
● Uma lista com 5 e-mails
● Uma lista com 5 telefones
● Uma lista com 5 cidades
● Uma lista com 5 estados
Após """

import random



print('Bem-vindo ao gerador de dados de teste, para finalizar o programa digite "parar"...\n')
print('Quais os dados deseja imprimir?\n \n[1]Nome\n[2]E-mail\n[3]Telefone\n[4]Cidade\n[5]Estado')
print(40*'-')
escolhas = input('Digite as opcoes de acordo com os numero e separados por virgula: ')
lista = []
print(lista)


def nomes():
    nomes = ['Everton','Janice','Helga','Bruna','Fabio']
    if escolhas == 1:
        return lista.append(random.choice(nomes))
        
    
            
            
         
e_mails = ['everton@gmail.com','Janice@gmail.com','helga@gmail.com','bruna@gmail.com','fabio@hotmail.com']
email = random.choice(e_mails)
print(email)
telefones = ['927425845','145236523','425841253','546545656','456466151']
cidades = ['aveiro','agueda','coimbra','lisboa','berlin']
estados = ['PE','MA','SP','RS','PB']        
        


            
