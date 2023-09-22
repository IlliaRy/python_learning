import build_main as bm

def test_compair_output_with_input_constant():
    assert bm.COMPILE_SCRIPT == 'g++.exe -g -std=c++20 D:/C_PLUS_PLUS/FreeCode/2/2.4Template/*.cpp -o D:/C_PLUS_PLUS/FreeCode/2/2.4Template/rooster.exe'

def test_verify_get_compile_script():
    assert bm.get_compile_script(bm.COMPILE_SCRIPT) == 'g++.exe -g -std=c++20 D:/C_PLUS_PLUS/FreeCode/2/2.4Template/*.cpp -o D:/C_PLUS_PLUS/FreeCode/2/2.4Template/rooster.exe'
