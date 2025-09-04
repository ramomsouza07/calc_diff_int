from sympy import symbols, sympify, log, sqrt, Abs, sin, cos, tan, exp, pi, E, diff, integrate

# Função inicial
entrada = input("Digite a função inicial: ")
variavel = input("Digite a variável principal: ")

var = symbols(variavel)
f_sym = sympify(entrada)

print(f"Função interpretada: {f_sym}")

# Menu
change = int(input("\nEscolha (0 - Derivada / 1 - Integral / 2 - Alterar Função / 9999 - Sair): "))

while change != 9999:
    if change == 0:
        # Derivada
        variavel = input("Insira a variável que será derivada: ")
        var = symbols(variavel)
        df_sym = diff(f_sym, var)
        print(f"A derivada da função em relação a {variavel} é: {df_sym}")

    elif change == 1:
        # Integral
        change_i = int(input("Integral Definida (0) / Integral Indefinida (1): "))
        variavel = input("Insira a variável da integração: ")
        var = symbols(variavel)

        if change_i == 0:
            a = float(input("Insira o valor de a: "))
            b = float(input("Insira o valor de b: "))
            I_def = integrate(f_sym, (var, a, b))
            print(f"O valor da integral definida é: {I_def}")
        elif change_i == 1:
            I_indf = integrate(f_sym, var)
            print(f"A integral indefinida é: {I_indf}")
        else:
            print("Opção inválida!")

    elif change == 2:
        # Alterar função
        entrada = input("Digite a nova função: ")
        variavel = input("Digite a variável principal: ")
        var = symbols(variavel)
        f_sym = sympify(entrada)
        print(f"Função alterada com sucesso! Nova função: {f_sym}")

    else:
        print("Opção inválida!")

    change = int(input("\nEscolha (0 - Derivada / 1 - Integral / 2 - Alterar Função / 9999 - Sair): "))
