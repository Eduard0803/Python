from db_config import Session, DefaultTable

def insert_person(name:str=None, age:str=None)->bool:
    if name is None or age is None:
        return False
    session = Session()
    new_p = DefaultTable(name=name.lower(), age=age)
    session.add(new_p)
    session.commit()
    session.close()
    return True

def query_person(name:str=None, age:int=None):
    if name is None or age is None:
        return None
    session = Session()
    person = session.query(DefaultTable).filter_by(name=name.lower(), age=age).first()
    if person is None:
        return None
    return person
