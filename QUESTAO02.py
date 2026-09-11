nome = 'Juvenaldo Florentino'
nome = "".join(nome.split())

import re
partes = re.findall(r'[A-Z][a-z]*', nome)
nome_corrigido = " ".join(partes)
print(nome_corrigido)

# import = importa um módulo ou biblioteca.
# re = módulo usado para trabalhar com expressões regulares (Regex).
# * = indica repetição de zero ou mais vezes.