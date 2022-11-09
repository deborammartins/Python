def classifica_idade(idade):
    if idade == 0 or idade <= 12:
        return 'Você é Criança'

    elif idade == 13 or idade <= 17:
        return 'Você é Adolescente'

    elif idade >= 18:
        return 'Você é Adulto'

    else:
        return 'Idade inválida'

id = int(input('Qual é a sua idade? '))
print(classifica_idade(id))