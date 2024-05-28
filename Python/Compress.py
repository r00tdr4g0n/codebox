import subprocess

def Decompress(a_src: str,  a_dest: str) -> bool:
    command = f"7z.exe x {a_src} -o{a_dest} -aoa"
    
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except Exception as e:
        return False