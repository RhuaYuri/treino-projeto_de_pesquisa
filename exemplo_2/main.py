import classes as c

professor = c.Professor('João')
sala = c.Sala(3)
professor.salaDeAula = sala

print('Nome do  Professor: ' + str(professor.nome()))

print('Status: ' + str(professor.EmAula()))

print('Associação com Sala. Verificação da porta: ' + str(professor.salaDeAula.FecharSala()))


