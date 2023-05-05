from time import sleep
votos = {}
bolsonaro = 0
lula = 0
ciro = 0
daciolo = 0
votos[22] = 'Bolsonaro'
votos[13] = 'Lula'
votos[12] = 'Ciro Gomes'
votos[51] = 'Cabo Daciolo'
totvotos = 0

while True:
    nome = input('Digite seu nome completo: (0 para parar)  ')
    if nome == '0':
        break
    sleep(1)
    cpf = str(input('Digite seu CPF: '))
    sleep(2)
    print(f'Olá, {nome}, do CPF {cpf} estou verificando seus dados para uma votação mais segura! Aguarde um momento...')
    sleep(2)
    presida = int(input('Em quem você quer votar para presidente? '))
    if presida == 22:
        bolsonaro += 1
        print(f'Você votou no candidato de número {presida}, voto registrado com sucesso!')
    elif presida == 13:
        lula += 1
        print(f'Você votou no candidato de número {presida}, voto registrado com sucesso!')
    elif presida == 12:
        ciro += 1
        print(f'Você votou no candidato de número {presida}, voto registrado com sucesso!')
    elif presida == 51:
        daciolo += 1
        print(f'Você votou no candidato de número {presida}, voto registrado com sucesso!')
    else:
        print('NÚMERO INVÁLIDO! Voto anulado!')
    totvotos += 1

    sleep(3)
if totvotos == 0:
    print('Nenhum voto foi registrado')
else:
    print(f'Foram registrados {totvotos} votos.')
    print(f'Bolsonaro: {bolsonaro} votos ({bolsonaro/totvotos*100:.2f}%)')
    print(f'Lula: {lula} votos ({lula/totvotos*100:.2f}%)')
    print(f'Ciro Gomes: {ciro} votos ({ciro/totvotos*100:.2f}%)')
    print(f'Cabo Daciolo: {daciolo} votos ({daciolo/totvotos*100:.2f}%)')
porcentagem = presida / totvotos * 100
if bolsonaro > lula and bolsonaro > ciro and bolsonaro > daciolo:
    print(f'O vencedor das eleições foi Bolsonaro!')
elif lula > bolsonaro and lula > ciro and lula > daciolo:
    print(f'O vencedor das eleições foi Lula!')
elif ciro > bolsonaro and ciro > lula and ciro > daciolo:
    print(f'O vencedor das eleições foi Ciro Gomes!')
elif daciolo > bolsonaro and daciolo > lula and daciolo > ciro:
    print(f'O vencedor das eleições foi Cabo Daciolo!')
else:
    print('A eleição terminou empatada!')


