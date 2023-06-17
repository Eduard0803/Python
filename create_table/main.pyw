from tabulate import tabulate
from create_table import create_table
from create_interface import create_interface

#cria a tabela
table = create_table('data.json')

# escreve a tabela na janela
create_interface(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
