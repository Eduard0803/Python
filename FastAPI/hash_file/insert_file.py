from db_config import Session, DefaultTable

def insert_file(file_name, file_content, hash_file):
    session = Session()
    new_file = DefaultTable(file_name=file_name, file_content=file_content, hash_file=hash_file)
    session.add(new_file)
    session.commit()
    session.close()

def query_file(hash_file):
    session = Session()
    file = session.query(DefaultTable).filter_by(hash_file=hash_file).first()
    if file is None:
        return None
    return file
