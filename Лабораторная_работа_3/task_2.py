# TODO Напишите функцию find_common_participants
def find_common_participants(g1, g2, sep=','):
    a = g1.split(sep)
    b = g2.split(sep)
    common = [x for x in a if x in b]
    return sorted(set(common))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group, sep='|')
print("Общие участники:", result)
# TODO Провеьте работу функции с разделителем отличным от запятой
