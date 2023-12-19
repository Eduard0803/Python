import os

from db_config import DefaultTable, Session


def insert_file(file_name, file_content):
    session = Session()
    new_file = DefaultTable(file_name=file_name, file_content=file_content)
    session.add(new_file)
    session.commit()
    session.close()


def query_file_by_name(file_name):
    session = Session()
    file = session.query(DefaultTable).filter_by(file_name=file_name).first()
    if file is None:
        return None
    return file


if __name__ == "__main__":
    file_path = input("Insert the file name: ")

    if os.path.exists(file_path):
        option = int(input("\n1 - insert file\n2 - query file\n\nselect the option: "))
        if option == 1:
            with open(file_path, "rb") as file:
                file_data = file.read()
            insert_file(file_path, file_data)
            print("sucess")
        else:
            content = query_file_by_name(file_path)
            if not content:
                print("file not found")
            else:
                name = input("input the new name: ")
                with open(name, "wb") as file:
                    file.write(content.file_content)
                print("sucess")
    else:
        print("file not found")
