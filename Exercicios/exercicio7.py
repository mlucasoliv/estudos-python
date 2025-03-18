from linecache import clearcache


def media_ar(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

print(f"A média do aluno é de: {media_ar(nota1,nota2,nota3)}")