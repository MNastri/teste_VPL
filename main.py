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
    def __init__(self):
        remuneracao = 1_000.00
        liquidacao = 10_000.00
        if remuneracao+liquidacao == 0:     # só para evitar erro de lint. EXCLUIR
            pass

    def vpl(self, taxa: float, vencimento: str) -> float:
        """
        Calcular o Valor Presente Líquido do título para a taxa e vencimento.

        O Valor Presente Líquido de um fluxo de caixa é o saldo no presente
        deste fluxo descapitalizado a uma taxa de juros composta.

        :param taxa: float
            a taxa de juros que o título será descontado
        :param vencimento: str
            a data de vencimento do título
        :return: float
            retorna o valor presente do fluxo de caixa deste titulo
        """
        if taxa+int(vencimento) == 0:   # só para evitar erro de lint. EXCLUIR
            pass
        return -1.0


# TODO verificar se tem jeito melhor de trabalhar com datas (estou usando strings)
# TODO implementar procedimento do teste e output no termimal
def test(rr: float, dd: str) -> None:
    """
    Realizar o teste da classe Titulo com os parâmetros dados.

    :param rr: float
        a taxa de juros que o título será descontado
    :param dd: str
        a data de vencimento do título
    :return: None
        não retorna, apenas executa
    """
    titulo_teste = Titulo()
    output = titulo_teste.vpl(taxa=rr, vencimento=dd)
    print(f'input:{rr} e {dd} - output:{output}')


def main_loop() -> None:
    """ Realizar todos os testes."""
    test(0.00, '0')     # output=-1 (erro período tem que ser maior que zero)
    test(-1.00, '-1')   # output=-1 (erro período tem que ser maior que zero)
    test(-10.00, '0')   # output=-1 (erro período tem que ser maior que zero)
    test(10.00, '0')    # output=-1 (erro período tem que ser maior que zero)
    test(0.00, '-10')   # output=-1 (erro período tem que ser maior que zero)
    test(0.00, '1')     # output=10_000.00  (hp12: f REG 10000 g CFj 0 i f NPV)
    test(1.00, '1')     # output=5_000.00  (hp12: f REG 10000 g CFj 100 i f NPV)
    test(0.01, '2')     # output=10_793.06  (hp12: f REG 1000 g CFj 10000 g CFj 1 i f NPV)
    test(-0.01, '3')    # output=12_336.51  (hp12: f REG 1000 g CFj 2 g Nj 10000 g CFj 1 CHS i f NPV)
    test(0.00, '3')     # output=12_000.00  (hp12: f REG 1000 g CFj 2 g Nj 10000 g CFj 0 i f NPV)
    test(0.01, '3')     # output=11_676.30  (hp12: f REG 1000 g CFj 2 g Nj 10000 g CFj 1 i f NPV)
    test(0.99, '3')     # output=2_023.97  (hp12: f REG 1000 g CFj 2 g Nj 10000 g CFj 99 i f NPV)
    test(1.00, '3')     # output=2_000.00  (hp12: f REG 1000 g CFj 2 g Nj 10000 g CFj 100 i f NPV)
    test(1.01, '3')     # output=1_976.47  (hp12: f REG 1000 g CFj 2 g Nj 10000 g CFj 101 i f NPV)


if __name__ == '__main__':
    main_loop()
