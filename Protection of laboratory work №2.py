# Задание - отсортировать строку по возрастанию суммы первых двух букв в слове (по кодировке ascii)
def get_ascii_num(a, b = None):
    '''Возвращает сумму номеров ascii первых двух букв, при отсутствии второй буквы возвращает только её номер'''
    if b:
        return ord(a) - 96 + ord(b) - 96
    return ord(a) - 96


def sort_words_in_string_by_asсii_num(str_):
    '''Сортировка пузырьком строки по возрастанию суммы первых двух букв в слове'''
    mass = str_.split()
    count_mass = [[] for i in range(78)]
    res = []

    for item in mass:
        if len(item) == 1:
            count_mass[get_ascii_num(item[0])].append(item)
        else:
            count_mass[get_ascii_num(item[0], item[1])].append(item)

    for i in range(len(count_mass)):
        for item in count_mass[i]:
            res.append(item)

    return ' '.join(res)


def testing(str_, n):
    '''Тестирование'''
    print(f"Тест №{n} -> " + str_ + " --> " + sort_words_in_string_by_asсii_num(str_))


if __name__ == '__main__':
    test_mass = ['z y x w v u t s r q p o n m l k j i h g f e d c b a',
                 'zl yl xl wl vl ul tl sl rl ql pl ol nl ml ll kl jl il hl gl fl el dl cl bl al',
                 'zz yy xx ww vv uu tt ss rr qq pp oo nn mm ll kk jj ii hh gg ff ee dd cc bb aa',
                 'zzz yyz xxz wwz vvz uuz ttz ssz rrz qqz ppz ooz nnz mmz llz kkz jjz iiz hhz ggz ffz eez ddz ccz bbz aaz',
                 'gg aa gg zz gg ff dd ee dd cc aa dd bb aa a',
                 'e d d d c b a a a f f g g g',
                 'z y x w v u t s r q p o n m l k j i h g f e d c b a zz yy xx ww vv uu tt ss rr qq pp oo nn mm ll kk jj ii hh gg ff ee dd cc bb aa',
                 'python apthon python pathon pzthon python zpthon ypthon',
                 'two python developers came to the bar and started a dialogue one says to the other i do not know python and the second answers me too']
    for i in range(len(test_mass)):
        testing(test_mass[i], i+1)