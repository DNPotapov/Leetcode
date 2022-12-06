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
  
'''Результат тестирования
Тест №1 -> z y x w v u t s r q p o n m l k j i h g f e d c b a --> a b c d e f g h i j k l m n o p q r s t u v w x y z
Тест №2 -> zl yl xl wl vl ul tl sl rl ql pl ol nl ml ll kl jl il hl gl fl el dl cl bl al --> al bl cl dl el fl gl hl il jl kl ll ml nl ol pl ql rl sl tl ul vl wl xl yl zl
Тест №3 -> zz yy xx ww vv uu tt ss rr qq pp oo nn mm ll kk jj ii hh gg ff ee dd cc bb aa --> aa bb cc dd ee ff gg hh ii jj kk ll mm nn oo pp qq rr ss tt uu vv ww xx yy zz
Тест №4 -> zzz yyz xxz wwz vvz uuz ttz ssz rrz qqz ppz ooz nnz mmz llz kkz jjz iiz hhz ggz ffz eez ddz ccz bbz aaz --> aaz bbz ccz ddz eez ffz ggz hhz iiz jjz kkz llz mmz nnz ooz ppz qqz rrz ssz ttz uuz vvz wwz xxz yyz zzz
Тест №5 -> gg aa gg zz gg ff dd ee dd cc aa dd bb aa a --> a aa aa aa bb cc dd dd dd ee ff gg gg gg zz
Тест №6 -> e d d d c b a a a f f g g g --> a a a b c d d d e f f g g g
Тест №7 -> z y x w v u t s r q p o n m l k j i h g f e d c b a zz yy xx ww vv uu tt ss rr qq pp oo nn mm ll kk jj ii hh gg ff ee dd cc bb aa --> a b aa c d bb e f cc g h dd i j ee k l ff m n gg o p hh q r ii s t jj u v kk w x ll y z mm nn oo pp qq rr ss tt uu vv ww xx yy zz
Тест №8 -> python apthon python pathon pzthon python zpthon ypthon --> apthon pathon python python python ypthon pzthon zpthon
Тест №9 -> two python developers came to the bar and started a dialogue one says to the other i do not know python and the second answers me too --> a bar came developers i dialogue and and answers me do says second know the the the one not to to other too started python python two
'''
