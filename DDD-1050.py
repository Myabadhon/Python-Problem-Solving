key = input()
dic = {'61':'Brasilia',
       '71':'Salvador',
       '11':'Sao Paulo',
       '21':'Rio de Janeiro',
       '32':'Juiz de Fora',
       '19':'Campinas',
       '27':'Vitoria',
       '31':'Belo Horizonte'}
if key in dic:
    print(dic[key])
else:
    print("DDD nao cadastrado")