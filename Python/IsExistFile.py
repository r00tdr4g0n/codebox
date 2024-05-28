import os

def IsExistFile(a_file: str = None) -> bool:
    if (a_file is not None) and (len(a_file) > 0):
        return os.path.isfile(a_file)
    else:
        return False