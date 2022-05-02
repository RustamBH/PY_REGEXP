import csv
import re
from pattern import pattern_phone, subst_phone


def get_corrected_fio_phone(contact_list: list):
    # lastname, firstname и surname
    for contact in contact_list[1:]:
        lastname_line = str(contact[0]).split(' ')
        if len(lastname_line) == 1:
            continue
        if len(lastname_line) == 2:
            contact[0] = lastname_line[0]
            contact[1] = lastname_line[1]
        elif len(lastname_line) == 3:
            contact[0] = lastname_line[0]
            contact[1] = lastname_line[1]
            contact[2] = lastname_line[2]

    all_lastnames_list = []
    for contact in contact_list[1:]:
        contact[5] = re.sub(pattern_phone, subst_phone, contact[5])
        all_lastnames_list.append(contact[0])
        firstname_line = str(contact[1]).split(' ')
        if len(firstname_line) == 2:
            contact[1] = firstname_line[0]
            contact[2] = firstname_line[1]

    return contact_list, all_lastnames_list


def del_duplicates(contact_list: list, all_lastnames_list: list):
    dup_lastname_list = list(set([x for n, x in enumerate(all_lastnames_list) if all_lastnames_list.count(x) > 1]))

    for dup_lastname in dup_lastname_list:
        dup_index_list = []
        for i, contact in enumerate(contact_list):
            if contact[0] == dup_lastname:
                dup_index_list.append(i)
                if contact[0] != '':
                    contact_list[dup_index_list[0]][0] = contact[0]
                if contact[1] != '':
                    contact_list[dup_index_list[0]][1] = contact[1]
                if contact[2] != '':
                    contact_list[dup_index_list[0]][2] = contact[2]
                if contact[3] != '':
                    contact_list[dup_index_list[0]][3] = contact[3]
                if contact[4] != '':
                    contact_list[dup_index_list[0]][4] = contact[4]
                if contact[5] != '':
                    contact_list[dup_index_list[0]][5] = contact[5]
                if contact[6] != '':
                    contact_list[dup_index_list[0]][6] = contact[6]

        dup_index_list.sort(reverse=True)
        for j in range(len(dup_index_list) - 1):
            del contact_list[dup_index_list[j]]

    return contact_list


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf8') as csv_f:
        rows = csv.reader(csv_f, delimiter=",")
        contacts_list = list(rows)

    contacts_list, all_lastname_list = get_corrected_fio_phone(contacts_list)
    contacts_list = del_duplicates(contacts_list, all_lastname_list)

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)
