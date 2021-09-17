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


class Titulo:
    def __init__(self):
        self.remuneracao = 1_000.00
        self.liquidacao = 10_000.00

    def vpl(self, taxa: float, vencimento: int) -> float:
        """
        Calcular o Valor Presente Líquido do título para a taxa e vencimento.

        O Valor Presente Líquido de um fluxo de caixa é o saldo no presente
        deste fluxo descapitalizado a uma taxa de juros composto.

        :param taxa: float
            a taxa de juros que o título será descontado
        :param vencimento: int
            a data de vencimento do título
        :return: float
            retorna o valor presente do fluxo de caixa deste titulo
        """
        if vencimento <= 0 or taxa == -1.00:
            return -1.0  # erro
        rr = self.remuneracao
        saldo = self.liquidacao
        periodos_restantes = vencimento
        while periodos_restantes:
            saldo = saldo / (1 + taxa)
            saldo = saldo + rr if periodos_restantes > 1 else saldo
            periodos_restantes -= 1
            print(f'saldo{periodos_restantes} = {saldo:,.2f}', end=", ")
        return saldo


def test(rr: float, dd: int) -> float:
    """
    Realizar o teste da classe Titulo com os parâmetros dados.

    :param rr: float
        a taxa de juros que o título será descontado
    :param dd: int
        a data de vencimento do título
    :return: None
    """
    titulo_teste = Titulo()
    output = titulo_teste.vpl(taxa=rr, vencimento=dd)
    print(f'input: {rr:.2f} e {dd} - output: {output:,.2f}')
    return output


def main_loop() -> None:
    """ Realizar todos os testes."""
    test(0.00, 0)     # output=-1 (erro período tem que ser maior que zero)
    test(-10.00, 0)   # output=-1 (erro período tem que ser maior que zero)
    test(10.00, 0)    # output=-1 (erro período tem que ser maior que zero)
    test(0.00, -10)   # output=-1 (erro período tem que ser maior que zero)
    test(-0.50, -1)   # output=-1 (erro período tem que ser maior que zero)
    test(-1.00, 1)    # output=-1 (erro taxa tem que ser diferente de -1)
    print('==')
    test(0.00, 1)     # output=10,000.00  (hp12: f REG 10000 g CFj 0 i f NPV)
    test(1.00, 1)     # output=5,000.00  (hp12: f REG 10000 g CFj 100 i f NPV)
    test(0.01, 2)     # output=10,793.06  (hp12: f REG 1000 g CFj 10000 g CFj 1 i f NPV)
    test(-0.01, 3)    # output=12,336.51  (hp12: f REG 1000 g CFj 2 g Nj 10000 g CFj 1 CHS i f NPV)
    test(0.00, 3)     # output=12,000.00  (hp12: f REG 1000 g CFj 2 g Nj 10000 g CFj 0 i f NPV)
    test(0.01, 3)     # output=11,676.30  (hp12: f REG 1000 g CFj 2 g Nj 10000 g CFj 1 i f NPV)
    test(0.99, 3)     # output=2,023.97  (hp12: f REG 1000 g CFj 2 g Nj 10000 g CFj 99 i f NPV)
    test(1.00, 3)     # output=2,000.00  (hp12: f REG 1000 g CFj 2 g Nj 10000 g CFj 100 i f NPV)
    test(1.01, 3)     # output=1,976.47  (hp12: f REG 1000 g CFj 2 g Nj 10000 g CFj 101 i f NPV)


if __name__ == '__main__':
    main_loop()
