"""1. Schreibe eine Python Funktion welche den User darum bittet eine Zahl einzugeben
 und diese als Integer zurückgibt (per return).  Versuche etwas anderes als eine Zahl
  einzugeben, es sollte ein Fehler auftreten.
 Behandle diesen Fehler wie heute gezeigt (Stichwort: try/except)."""

user_input = input("Enter the input ")

try:
    int(user_input)
    it_is = True
except ValueError:
    it_is = False

print(it_is)