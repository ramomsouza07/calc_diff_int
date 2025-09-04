# MANUAL DE USO - CALCULADORA SIMBÓLICA

Este programa permite ao usuário trabalhar com funções matemáticas simbólicas utilizando a biblioteca SymPy em Python. Com ele, é possível:

* Derivar funções em relação a qualquer variável
* Integrar funções de forma definida ou indefinida
* Alterar a função a qualquer momento durante a execução

---

## INSTRUÇÕES DE USO

1. Ao iniciar o programa, será solicitado que você digite a função inicial.

   * Exemplo: x\*\*2 + y

2. Em seguida, insira a variável principal que será usada inicialmente.

   * Exemplo: x

3. O programa exibirá a função interpretada.

4. Menu de opções:

   * 0: Derivar a função
   * 1: Integrar a função
   * 2: Alterar a função
   * 9999: Sair do programa

---

## DERIVADA

* Escolha a opção 0.
* Digite a variável em relação à qual deseja derivar.
* O programa exibirá a derivada simbólica.

  * Exemplo de entrada: x
  * Exemplo de saída: 2\*x

---

## INTEGRAL

* Escolha a opção 1.
* O programa perguntará se deseja integral definida (0) ou indefinida (1).
* Digite a variável da integração.
* Para integral definida, insira os limites a e b.
* O programa exibirá o resultado da integral.

---

## ALTERAR FUNÇÃO

* Escolha a opção 2.
* Digite a nova função e a nova variável principal.
* O programa atualizará a função e você poderá realizar novas operações.

---

## EXEMPLOS DE FUNÇÕES (REFERÊNCIA PARA O USUÁRIO)

Aqui estão algumas possibilidades de funções que podem ser digitadas no programa. O usuário pode se basear nesses exemplos para criar suas próprias funções:

1. log(x,10) + Abs(x-1) + cos(x)       → Logaritmo base 10, módulo e cosseno
2. sqrt(x) + log(x) + sin(x)           → Raiz quadrada, logaritmo natural e seno
3. exp(x) + x\*\*2 + tan(x)              → Exponencial, potência e tangente
4. Abs(x-3) + log(x,2) + cos(y)        → Valor absoluto, log base 2 e cosseno com outra variável
5. x**2 + y**2 + z\*\*2                   → Função com múltiplas variáveis
6. sin(x) + cos(y) + tan(z)            → Funções trigonométricas combinadas
7. sqrt(x**2 + y**2) + log(E\*x)        → Raiz quadrada de soma de quadrados e logaritmo natural
8. Abs(sin(x)) + exp(y)                → Valor absoluto de seno e exponencial
9. log(x\*\*2 + 1, 10) + tan(x)          → Logaritmo base 10 de expressão e tangente
10. x\*\*3 + sqrt(y) + cos(z)            → Combinação de potência, raiz e cosseno

---

## DICAS IMPORTANTES

* Use \*\* para potências: x\*\*2 = x²
* log(x) representa ln(x); log(x, 10) representa logaritmo base 10
* sqrt(x) para raiz quadrada
* Abs(x) para valor absoluto (|x|)
* Funções trigonométricas: sin(x), cos(x), tan(x)
* exp(x) para e^x
* pi e E para constantes π e e
* Sempre verifique se digitou corretamente as variáveis presentes na função

