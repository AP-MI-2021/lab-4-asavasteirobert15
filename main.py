
def inlocuire_numere_cu_string(lista):
    """
    O functie in care numerele sunt înlocuite cu un string format din
    cuvinte care le descriu caracter cu caracter.
    :param lista: lista cu numerele - lst
    :return: lista finala - lst
    """
    final_list = []
    for numar in lista:
        numar_str = str(numar)
        numarscris = ''
        if int(numar) == numar:
            for poz in range(0, len(numar_str)-2):
                if numar_str[poz] == '-':
                    numarscris = numarscris + 'minus'
                elif numar_str[poz] == '.':
                    numarscris = numarscris + 'virgula'
                elif numar_str[poz] == '-':
                    numarscris = numarscris + 'minus'
                elif numar_str[poz] == '0':
                    numarscris = numarscris + 'zero'
                elif numar_str[poz] == '1':
                    numarscris = numarscris + 'unu'
                elif numar_str[poz] == '2':
                    numarscris = numarscris + 'doi'
                elif numar_str[poz] == '3':
                    numarscris = numarscris + 'trei'
                elif numar_str[poz] == '4':
                    numarscris = numarscris + 'patru'
                elif numar_str[poz] == '5':
                    numarscris = numarscris + 'cinci'
                elif numar_str[poz] == '6':
                    numarscris = numarscris + 'sase'
                elif numar_str[poz] == '7':
                    numarscris = numarscris + 'sapte'
                elif numar_str[poz] == '8':
                    numarscris = numarscris + 'opt'
                elif numar_str[poz] == '9':
                    numarscris = numarscris + 'noua'
            final_list.append(numarscris)
        else:
            for poz in range (0,len(numar_str)):
                if numar_str[poz] == '-':
                    numarscris = numarscris + 'minus'
                elif numar_str[poz]=='.':
                    numarscris = numarscris + 'virgula'
                elif numar_str[poz] == '-':
                    numarscris = numarscris + 'minus'
                elif numar_str[poz]== '0':
                    numarscris = numarscris + 'zero'
                elif numar_str[poz] == '1':
                    numarscris = numarscris + 'unu'
                elif numar_str[poz] == '2':
                    numarscris = numarscris + 'doi'
                elif numar_str[poz] == '3':
                    numarscris = numarscris + 'trei'
                elif numar_str[poz] == '4':
                    numarscris = numarscris + 'patru'
                elif numar_str[poz] == '5':
                    numarscris = numarscris + 'cinci'
                elif numar_str[poz] == '6':
                    numarscris = numarscris + 'sase'
                elif numar_str[poz] == '7':
                    numarscris = numarscris + 'sapte'
                elif numar_str[poz] == '8':
                    numarscris = numarscris + 'opt'
                elif numar_str[poz] == '9':
                    numarscris = numarscris + 'noua'
            final_list.append(numarscris)

    return final_list

def parte_intreaga_divizor_parte_fractionara(lista):
    """
    Functia returneaza numerele care au proprietatea ca partea lor intreaga
    este divizor al partii fractionare
    :param lista: lista de numere pe care o vom verifica - lst
    :return: lista cu numerele care respecta cerinta - lista_finala - lst
    """
    lista_finala = []
    for numar in lista:
        if int(extract_fractionar(numar)) % int(extract_intreg(numar)) == 0 and int(extract_fractionar(numar)) != 0:
            lista_finala.append(numar)

    return lista_finala


def toate_numerele_dintr_un_interval(stanga, dreapta, lista):
    """
    Functia returneaza numerele dintr-o lista care fac parte dintr-un interval deschis dat
    :param stanga: capatul din stanga al intervalului - float
    :param dreapta: capatul din dreapta al intervalului - float
    :param lista: lista din care vom alege numerele care apartin intervalului (stanga,dreapta) - lst
    :return: lista finala cu numerele ce apartin intervalului
    """

    lista_finala = []
    for numar in lista:
        copie = numar
        if copie > stanga and copie < dreapta:
            lista_finala.append(numar)

    return lista_finala


def parte_intreaga_numere_lista(lista):
    """
    Aceasta functie pune intr-o lista doar partea intreaga a numerelor din alta lista
    :param lista: o lista de numere float
    :return: lista finala in care se afla doar partea intreaga a numerelor - lst
    """

    final_list = []
    for numar in lista:
        final_list.append(int(extract_intreg(numar)))

    return final_list


def extract_intreg(numar):
    """
    Functia extrage patrea intreaga a unui numar
    :param numar: float
    :return: partea intreaga a numarului - str
    """
    return str(numar).split('.')[0]


def extract_fractionar(numar):
    """
    Functia extrage partea fractionara a unui numar
    :param numar: float
    :return: partea intreaga a numarului - str
    """
    return str(numar).split('.')[1]


def citire_interval():
    """
    Functia va citi capetele unui inverval
    :return: capetele intervalului - float-uri
    """
    stanga = float(input('Introduceti capatul din stanga al intervalului : '))
    dreapta = float(input('Introduceti capatul din dreapta al intervalului : '))

    return stanga, dreapta


def citire_lista():
    """
    Functia va citi lista data de utilizator
    :return: Functia citita
    """
    result_list = []
    string_lista = input("Introduceti lista cu elementele despartite printr-un spatiu: ")

    string_elemente = string_lista.split(sep=" ")

    for string_element in string_elemente:
        element = float(string_element)
        result_list.append(element)

    return result_list


def test_function():

    assert parte_intreaga_numere_lista([1.5, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]
    assert toate_numerele_dintr_un_interval(-4, 5, [1.5, -3.3, 8, 9.8, 3.2]) == [1.5, -3.3, 3.2]
    
def main():
    lista = []
    while True:
        print('1. Citire lista !')
        print('2. Afișarea părții întregi a tuturor numerelor din listă !')
        print('3. Afisarea tuturor numerelor care fac parte dintr-un interval deschis citit de la tastatura !')
        print('4. Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare ! ')
        print('5. Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un string format din'
              'cuvinte care le descriu caracter cu caracter.')
        print('x. Exit ! ')
        optiune = input('Alege optiunea : ')
        if optiune == '1':
            lista = citire_lista()
        elif optiune == '2':
            lista_2 = parte_intreaga_numere_lista(lista)
            print(lista_2)
        elif optiune == '3':
            inceput, final = citire_interval()
            lista_3 = toate_numerele_dintr_un_interval(inceput, final, lista)
            print(lista_3)
        elif optiune == '4':
            lista_4 = parte_intreaga_divizor_parte_fractionara(lista)
            print(lista_4)
        elif optiune == '5':
            lista_5 = inlocuire_numere_cu_string(lista)
            print(lista_5)
        elif optiune == 'x':
            break

test_function()
main()
