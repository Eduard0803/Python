import hashlib
import os


def file_hash(file_name: str = None) -> str:
    if not file_name or not os.path.exists(file_name):
        return
    return str(hashlib.md5(open(file_name, "rb").read()).hexdigest())


if __name__ == "__main__":
    print(file_hash("file.pdf"))
