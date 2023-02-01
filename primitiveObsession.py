dados = [
    {
        'nome': 'Eduardo',
        'sobrenome': 'Mendas',
        'telefone': {'residencial':'1111-111', 'móvel':'999-999-999'},
        'ddd': 19
    },
    {
        'nome': 'Fausto',
        'sobrenome': 'Filho',
        'telefone': {'residencial':'2222-222', 'móvel':'999-999-888'},
        'ddd': 21
    },
]

nomes_completos = [f"{dado['nome']} {dado['sobrenome']}" for dado in dados]