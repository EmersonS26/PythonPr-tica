class Escola:
    def Ingressão(self,nome,turma,sala,numeroAluno ):
        self.nome = nome
        self.turma = turma
        self.sala = sala
        self.numeroAluno = numeroAluno
        
    def aluno(self):
        print(f"O aluno de numero {self.numeroAluno}, de nome {self.nome}, ingressou na turma de {self.turma}, na sala {self.sala} ")

new = Escola()
new.Ingressão("Railan",2024,17,1)
new.aluno()


