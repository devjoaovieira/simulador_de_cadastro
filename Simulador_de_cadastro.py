'''print('-=-'*20)
print('Cadastro de Usuário')
print('-=-'*20)
# O usuário digita:



nome = int(len(input('Digite seu nome completo: ').split()))
if nome < 2:
    print('!ERRO! DIGITE SEU SOBRENOME PARA CRIAR UM CADASTRO VÁLIDO')
elif nome >= 2:
    idade = int(input('Digite sua idade: '))

    if idade < 18:
        print('!ERRO! VOCÊ PRECISA TER PELO MENOS 18 ANOS PARA CRIAR UM CADASTRO VÁLIDO')
    elif idade >= 18:
        email = str(input('Digite seu e-mail: '))

        if '.com' not in email or '.edu' not in email and '@' not in email:
            print('!ERRO! DIGITE UM E-MAIL VÁLIDO')
        else:
            senha = int(len(input('Digite uma senha de 6 digitos: ')))

            if senha < 6:
                print('!ERRO! SUA SENHA PRECISA TER PELO MENOS 6 DIGITOS PARA CRIAR UM CADASTRO VÁLIDO')
            else:
                print('PARABENS! SEU CADASTRO FOI CONCLUÍDO COM SUCESSO!')'''

#---------VERSÃO CORRIGIDA---------#

print('-=-'*20)
print('Cadastro de Usuário')
print('-=-'*20)
# O usuário digita:



nome = str((input('Digite seu nome completo: ')))
qtd_palavras = len(nome.split())
#ao invés de aplicar LEN e SPLIT na primeira variável, criei uma nova e para deixar organizado

if qtd_palavras < 2:
    print('!ERRO! DIGITE SEU SOBRENOME PARA CRIAR UM CADASTRO VÁLIDO')
elif qtd_palavras >= 2:
    idade = int(input('Digite sua idade: '))

    if idade < 18:
        print('!ERRO! VOCÊ PRECISA TER PELO MENOS 18 ANOS PARA CRIAR UM CADASTRO VÁLIDO')
    elif idade >= 18:
        email = str(input('Digite seu e-mail: '))

        if '.com' not in email or '.edu' not in email and '@' not in email:
            print('!ERRO! DIGITE UM E-MAIL VÁLIDO')
        else:
            senha = int(len(input('Digite uma senha de 6 digitos: ')))

            if senha < 6:
                print('!ERRO! SUA SENHA PRECISA TER PELO MENOS 6 DIGITOS PARA CRIAR UM CADASTRO VÁLIDO')
            else:
                print('PARABENS! SEU CADASTRO FOI CONCLUÍDO COM SUCESSO!')

                