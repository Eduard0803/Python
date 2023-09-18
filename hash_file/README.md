### sistema de autenticação de arquivos por Hash md5

`pip install -r requirements.txt` para instalar as dependecias do sistema  

preencha as informações do banco no arquivo [db_config](db_config.py)  

`python create_pdf.py` para gerar um .pdf  

`uvicorn server:app --reload` para iniciar o servidor e acesse http://127.0.0.1:8000/  
