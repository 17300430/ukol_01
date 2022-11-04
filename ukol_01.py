def task_01():
    heritage = -1256983
    childrenNumber = 28
    if heritage >= 0:
        return heritage % childrenNumber
    else:
        return - ((- heritage) % childrenNumber)

def task_02():
    result1 = ((12**15) % 15) < 8 or (3**5) > 100
    result2 = 5 * (3**3) != 900 / 75
    return (result1, result2)

def task_03():
    string1 = '[[]]' + 'PYTHON'
    result1 = string1[:2] + string1[4:] + string1[2:4]
    string21 = 'Python'
    result21 = string21.replace('P','o').replace('y','n').replace('t','o').replace('h','n') + string21[-2:]
    string22 = 'Perl'
    result22 = (int(str(len(string22)**2)[1]))*string22[string22.find('r')]
    return (result1,result21,result22)

def task_04():
    result1 = lambda s : s[:len(s)//2].upper() + s[len(s)//2:].lower()
    result2 = lambda s : len(s)*s[0]
    return (result1,result2)

def task_05():
    return "Chyba je na 4. řádku, snažím se k textovému řetězci připojit celé číslo."

def task_06():
    result1 = lambda hobby : print('My hobby is {h}.'.format(h=hobby))
    date = '2018-11-01'
    date_split = date.split('-')
    result2 = '{dd}/{mm}'.format(dd=date_split[2], mm=date_split[1])
    return (result1, result2)

def task_07():
    hobbies = []
    hobbies.append('C#')
    hobbies.append('Java')
    hobbies.append('FORTRAN')
    hobbies.append('Python')
    print(hobbies[0])
    print(hobbies[-1])
    hobbies.clear()

def task_08():
    cities = ['Prague', 'Brno', 'Ostrava', 'Plzen', 'Liberec', 'Olomouc', 'Usti nad Labem', 'Hradec Kralove', 'Ceske Budejovice', 'Pardubice']
    cities.sort()
    # Spojit textové řetězce tak, aby byly oddělené znakem * není pomocí "".join() možné (bez dalších úprav výsledného textového řetězce).
    return "*".join(cities)

def task_09():
    return "Zadání je nesrozumitelné a nečitelné."

def task_10():
    # První část zadání je nesrozumitelné – 'payton' je zcela validní klíč.
    # Ve druhé části není vzhledem k zadání možné použít pouze jeden datový typ (musím použít slovník a slovník sám není schopen nést informaci; navíc není technicky možné udělat slovník slovníků slovníků slovníků..., protože počítač má pouze konečnou paměť).
    return {('Jméno', 'Příjmení'): '+420 123 456 789', ('Meno', "Priezvisko"): '+421 123 456 789'}

def task_11():
    info = {('Name', 'Surname'): ('John', 'Doe')}
    key = ('Name', 'Surname')
    return info[key][0] + '_' + info[key][1]