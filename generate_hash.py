import hashlib
import os


def str_hash(string: str = None) -> None:
    if not string:
        print("string not found")
        return
    md5_hash = hashlib.md5(string.encode()).hexdigest()
    print(f"string_hash: {md5_hash}")


def file_hash(file_name: str = None) -> None:
    if not file_name or not os.path.exists(file_name):
        print("file not found")
        return
    md5_hash = hashlib.md5(open(file_name, "rb").read()).hexdigest()
    print(f"hash_generated: {md5_hash}")


if __name__ == "__main__":
    str_hash("example")
    file_hash("example.pdf")
