class Aluno:
    def __init__(self,nome,idade,nota,freq):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.freq = freq

    def aprovado(self):
        if self.nota >= 6.0 and self.freq >= 0.75:
            return True
        else:
            return False