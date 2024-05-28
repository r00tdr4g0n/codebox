import os

def IsExistDirectory(a_path: str = None) -> bool:
    if (a_path is not None) and (len(a_path) > 0):
        return os.path.isdir(a_path)
    else:
        return False