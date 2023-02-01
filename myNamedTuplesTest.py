from myNamedTuples import pessoa

dados = [
    pessoa('Eduardo', 'Mendas', {'residencial': '1111-111', 'móvel': '999-999-999' }, 19),
    pessoa('Luciano', 'Filho', {'residencial': '2222-222', 'móvel': '999-999-888' }, 21),
]

eduardo = dados[0]
print(eduardo.nome)
print(eduardo.sobrenome)
print(eduardo.telefone)
print(eduardo.telefone['residencial'])
print(eduardo.ddd)
