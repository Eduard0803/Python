from db_config import Session, DefaultTable

def insert_person(p):
    session = Session()
    new_p = DefaultTable(name=p.name.lower(), email=p.email.lower(), age=p.age)
    session.add(new_p)
    session.commit()
    session.close()

def query_person(email:str=None):
    if email is None:
        return None
    session = Session()
    person = session.query(DefaultTable).filter_by(email=email.lower()).first()
    session.close()
    if person is None:
        return None
    return person

def update_person(p)->bool:
    session = Session()
    person = session.query(DefaultTable).filter_by(email=p.email.lower()).first()
    if person is None:
        return False
    person.email = p.email.lower()
    person.name = p.name.lower()
    person.age = p.age
    session.commit()
    session.close()
    return True

def delete_person(email:str=None)->bool:
    if email is None:
        return False
    session = Session()
    person = session.query(DefaultTable).filter_by(email=email.lower()).first()
    if person is None:
        return False
    session.delete(person)
    session.commit()
    session.close()
    return True
