# PS D:/C_PLUS_PLUS/FreeCode/2/2.4Template>
# g++.exe -g -std=c++20 D:/C_PLUS_PLUS/FreeCode/2/2.4Template/*.cpp -o D:/C_PLUS_PLUS/FreeCode/2/2.4Template/rooster.exe
# ooster.exe -std=c++20 D:/C_PLUS_PLUS/FreeCode☻☻.4Template/*.cpp -o D:/C_PLUS_PLUS/FreeCode☻☻.4Template

"""Copmiling c++ code

Returns:
    int: exit code
"""

import subprocess

COMPILE_SCRIPT = 'g++.exe -g -std=c++20 D:/C_PLUS_PLUS/FreeCode/2/2.4Template/*.cpp -o D:/C_PLUS_PLUS/FreeCode/2/2.4Template/rooster.exe'



def get_compile_script (script):
    """get compile script

    Args:
        script (str): receive compilation command

    Returns:
        str: script to run
    """
    print("getting script: ", script)
    return script

def run_compile_script (script):
    """run script

    Args:
        script (str): script to run
    """
    print("executing script")
    subprocess.run(script, shell=True, check=True)

if __name__ == "__main__":
    A = get_compile_script(COMPILE_SCRIPT)
    run_compile_script(A)
