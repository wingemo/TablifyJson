# test/test_main.py
from src.main import main
import io
import sys
import pytest

def test_main(capsys):
    # Sätt sökvägen för resultatfilen
    result_file_path = 'test_results/test_results.txt'

    # Använd en StringIO för att fånga upp utmatningen
    captured_out = io.StringIO()
    sys.stdout = captured_out

    # Kör main-funktionen
    main()

    # Återställ stdout
    sys.stdout = sys.__stdout__

    # Hämta fångad utmatning
    captured_output = captured_out.getvalue().strip()

    # Skriv ut resultatet till test_results/test_results.txt
    with open(result_file_path, 'w') as f:
        f.write(captured_output)

    # Jämför fångad utmatning med förväntat resultat
    assert captured_output == "Hello, World!"
