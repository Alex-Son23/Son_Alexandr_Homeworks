def thesaurus(*args):
    staff = {}
    for employee in args:
        first_char_name = employee[0]
        if staff.get(first_char_name) is None:
            staff[first_char_name] = [employee]
        else:
            staff[first_char_name].append(employee)
    return staff


x = thesaurus('Alex', 'Mikey', 'Alllo', 'Clown', 'Casha')
print(x)


def thesaurus1(staff, *args):
    for employee in args:
        first_char_name = employee[0]
        if staff.get(first_char_name) is None:
            staff[first_char_name] = [employee]
        else:
            staff[first_char_name].append(employee)
    return staff


def thesaurus_adv(*args):
    full_name_staff = {}
    for employee in args:
        full_name_employee = employee.split()
        first_char_surname = full_name_employee[1][0]

        if full_name_staff.get(first_char_surname) is None:
            full_name_staff[first_char_surname] = thesaurus1({}, employee)
        else:
            first_char_name_dict = full_name_staff[first_char_surname]
            full_name_staff[first_char_surname] = thesaurus1(first_char_name_dict, employee)
    return full_name_staff


status = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(status)
