def verificar_aprovacao(nota):
    if nota >= 6:
        print("Passou de ano!")
    else:
        print("Reprovado, tente de novo!")


verificar_aprovacao(8)


def verificar_voto(idade):
    if idade >= 16:
        print("Pode votar!")
    else:
        print("Ainda não pode votar.")


verificar_voto(15)


def classificar_nota(nota):
    if 90 <= nota <= 100:
        print("Parabéns, você tirou A")
    elif 80 <= nota < 90:
        print("Muito bem, você tirou B")
    elif 70 <= nota < 80:
        print("Bom trabalho, você tirou C")
    elif 60 <= nota < 70:
        print("Fique atento, você tirou D.")
    else:
        print("Estude um pouco mais, você tirou F.")


classificar_nota(85)


def somar_numeros():
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    try:
        soma = float(num1) + float(num2)
        print("A soma é:", soma)
    except ValueError:
        print("Digite só números!")


somar_numeros()


def verificar_senha():
    senha = input("Digite a senha: ")
    if senha == "Python123":
        print("Acesso liberado!")
    else:
        print("Senha errada!")


verificar_senha()


def contar_ate_10():
    num = 1
    while num <= 10:
        print(num)
        num += 1


contar_ate_10()


def organizar_lista():
    numeros = [8, 3, 10, 1, 5]
    numeros.sort()
    print("Números organizados:", numeros)


organizar_lista()


def acessar_registros():
    alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
    print("Primeiro aluno:", alunos[0])
    print("Último aluno:", alunos[-1])


acessar_registros()


def dobro(numero):
    return f"O dobro de {numero} é {numero * 2}"


print(dobro(5))


def contar_letras(nome):
    return f"O nome {nome} tem {len(nome)} letras"


print(contar_letras("Ana"))
