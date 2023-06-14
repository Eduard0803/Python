## formulario
script feito para estudar os metodos 'http' e framework 'FastAPI'  

para o correto funcionamento execute o código `pip install -r requirements.txt` no terminal  

apos concluidas as instalações execute o código `uvicorn main:app --reload` no terminal  

o código cria recebe dados de um formulario html, formata os dados no formato `.json` e depois exibe os dados coletados em outra página html  

[index.html](templates/index.html) - pagina da interface padrão  
[input.html](input.html) - formulario html  
[output.html](templates/output.html) - página onde exibe os dados  
[data.json](data.json) - arquivo `.json` criado com os dados coletados  
