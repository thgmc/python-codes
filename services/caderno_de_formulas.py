

class Juros:
    @staticmethod
    def valor_unitario_juros(valor_nominal_atualizado, fator_juros) -> float:
        """
        Args:
            VNa (float): Valor Nominal atualizado, se for o caso, calculado com 8 (oito) casas decimais, sem arredondamento.
            Fator de Juros (float): Fator de juros fixos calculado com 9 (nove) casas decimais, com arredondamento, ou (Fator de juro Flutuante x Fator de Spread) também calculado com 9 (nove) casas decimais com arredondamento – ver no Item
    “Juros Flutuantes”.

        Returns:
            float: Valor unitário dos juros acumulados no período, calculado com 8 (oito) casas decimais, sem arredondamento..
        """
        if fator_juros == 0:
            raise ValueError("O fator de juros não pode ser zero.")
        
        return valor_nominal_atualizado * (fator_juros - 1)
    
    @staticmethod
    def fator_juros(i, dut, dup) -> float:
        """
        Args:
            i (float): Taxa de juros expressa em 252 dias úteis, informada com 4 (quatro) casas decimais.
            dut (int): Número de dias úteis, assim definido:
            dup (int): Número de dias úteis, assim definido:

        Returns:
            float: Fator de juros fixos calculado com 9 (nove) casas decimais, com arredondamento.
        """
        return (( i / 100 + 1) ** (dut / 252) ) ** (dup / dut)
    

class JurosFlutuantes:
    @staticmethod
    def valor_unitario_juros(fator_indice, fator_spread, vnb) -> float:
        """
        Args:
            fator_indice (float): Fator de índice calculado com 9 (nove) casas decimais, com arredondamento.
            fator_spread (float): Fator de spread calculado com 9 (nove) casas decimais, com arredondamento.
            vnb (float): Valor Nominal Bruto, calculado com 8 (oito) casas decimais, sem arredondamento.

        Returns:
            float: Fator de juros flutuante x Fator de Spread calculado com 9 (nove) casas decimais, com arredondamento.
        ARRED(((SERIE(12)/100+1)^252-1)*100,2)
        """
        return fator_indice * fator_spread
    @staticmethod
    def taxa_cdi_ao_dia() -> float:
        cdi = 0.055131
        cdi_anualizada = round(((cdi / 100 + 1) ** 252 - 1 ) * 100, 2)
        t_dik = round(((cdi_anualizada / 100 + 1) ** (1 / 252) - 1), 8)
        p = 100
        fator_cdi = round((1 + t_dik) * p / 100, 8)
        return fator_cdi