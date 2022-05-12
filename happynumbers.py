"""
Happy Numbers

Como saber se um número é feliz ou triste?
1. Dado um número inteiro positivo
2. Substitua o número pela soma dos quadrados dos seus dígitos.
3. Se o resultado 1, o número é feliz
4. Caso contrário, repita o processo indefinidamente

Os números que resultares em 1, são felizes.
Os que resultarem em 1 são tristes

Exemplo

O número 7 é feliz?

7² = 49
4² + 9² = 16 + 81 = 97
9² + 7² = 81 + 49 = 130
1² + 3² + 0² = 1 + 9 + 0 = 10
1² + 0² = 1
7 é feliz!

"""


def sum_of_squares(number):
    return sum(int(char) ** 2 for char in str(number))


def happy(number):
    next_ = sum(int(char) ** 2 for char in str(number))
    return number in (1, 7) if number < 10 else happy(next_)


if __name__ == '__main__':
    assert sum_of_squares(130) == 10
    assert all(happy(n) for n in (1, 10, 100, 130, 97))
    assert not happy(4)
