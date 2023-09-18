from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from generate_hash import file_hash
from insert_file import insert_file

def create_pdf(file_name:str=None)->str:
    if not file_name:
        return None
    c = canvas.Canvas(file_name, pagesize=A4)
    largura, altura = A4

    c.line(100, altura - 120, largura - 100, altura - 120)
    c.drawString(100, altura - 100, f'Hash Code: {file_hash(file_name)}')
    hash = file_hash(file_name)
    c.save()
    return hash

if __name__ == "__main__":
    file_name = "file.pdf"
    hash = create_pdf(file_name)
    
    with open(file_name, 'rb') as f:
        file_data = f.read()
    insert_file(file_name, file_data, hash)
