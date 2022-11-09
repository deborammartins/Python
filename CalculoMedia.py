def calcula_media(M1, M2, M3):
    import numpy as np
    m = np.mean([M1, M2, M3])

    if m == 0 or m <= 4.0:
        return 'Aluno REPROVADO!'

    elif m == 4.1 or m <= 6.0:
        e = float(input('Aluno de EXAME! Qual a nota do Exame?  '))
        if e > 6.0:
            return 'Aluno APROVADO! PARABÉNS!'
        else:
            return 'Aluno REPROVADO!'

    elif m > 6.0:
        return 'Aluno APROVADO! PARABÉNS!'

m1 = float(input('Qual a sua primeira nota? '))
m2 = float(input('Qual a sua segunda nota? '))
m3 = float(input('Qual a sua terceira nota?'))
calcula_media(m1, m2, m3)