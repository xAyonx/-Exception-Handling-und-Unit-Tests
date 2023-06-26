"""1. Schreibe eine Python Funktion welche den User darum bittet eine Zahl einzugeben
 und diese als Integer zurückgibt (per return).  Versuche etwas anderes als eine Zahl
  einzugeben, es sollte ein Fehler auftreten.
 Behandle diesen Fehler wie heute gezeigt (Stichwort: try/except)."""

#num = input("Enter the input ")

#try:
#    int(num)
#    it_is = True
#except ValueError:
#    it_is = False
#print(it_is)


"""2. Schreibe eine Python Funktion welche eine Liste und einen Index übergeben bekommt und 
das Element an dem angegebenen Index zurückgibt. Sorge dafür, dass das Programm nicht abstürzt 
sondern "None" ausgibt, wenn ein IndexError auftritt."""

def element_lst(lst,index):
    try:
        return lst[index]
    except IndexError:
        return None

my_lst = [1,2,3,4,5]
index = 5


        
num = element_lst(my_lst,index)
print(num)