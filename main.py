"""
Marcelo, segue exercício para ser respondido até segunda-feira as 12:00
O código fonte escrito deve estar no github em um repositório criado para
este fim.
Neste mesmo repositório deve estar a documentação que achar necessária e as
considerações sobre a função desenvolvida.

----

Imagine um título de renda fixa que paga R$ 1.000 todo último dia útil do mês.
 No vencimento do título, este título pagará R$ 10.000.

Escreva uma função, em python, que retorne o valor deste título na data atual.

Esta função deverá receber dois parâmetros:
a taxa de juros (r) que o título será descontado e;
a data (d) de vencimento do título.

"""
# TODO implementar classe
class Titulo:
    pass

# TODO verificar se tem jeito melhor de trabalhar com datas
# TODO implementar procedimento do teste e output no termimal
def test(rr: float, dd: str) -> None:
    """
    Realize o teste da classe Titulo com os parâmetros dados.
    :param rr: float
        a taxa de juros que o título será descontado
    :param dd: str
        a data de vencimento do título
    :return: None
        não retorna, apenas executa
    """
    print(f'{rr} {dd}') # só para evitar erro de lint. EXCLUIR
    pass


def main_loop() -> None:
    """ Realize todos os testes."""
    pass


if __name__ == '__main__':
    main_loop()
