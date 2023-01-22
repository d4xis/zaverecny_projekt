class Pojisteny:

    '''Trida pro vypis udaju pojistence'''
    
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon
    
    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f'{self.jmeno} {self.prijmeni}, {self.vek} let, {self.telefon}'