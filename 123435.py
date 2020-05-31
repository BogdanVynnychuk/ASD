#1. Для нахождения всех подмножеств множества найдем сперва подмножества размера 1 далее 2 и по возрастающей
S = {1, 2, 3, 4, 5, 6, 7, 8, 9}

ans[]
S = list(s)
for i in range(1, len(s)):
    a = []
    for j in range(len(s) + 1 - i):
        a.append(s[j; j + 1])
    ans.append(a)
ans.append(s)

for i in ans:
    print(i)
#2. В функциональном программировании структура массива представляет собой связанный массив, то есть каждый эл указывает на следующий, массив заканчивается указателем на None:
class Node:
    def __init__(self, el):
        self.el = el
        self.next: Node = None


#3. Естественной заменой цикла в данной структуре является рекурсия, обращаться к следующему эл пока он не окажется    None:
def for_(core):
    if core is not None:
        print(core.el, end=" ")
        for_(core.next)
    print()
#4. Интересно научиться находить подмножества множества вопрос нахождения всех пожмножеств длины 1 не стоит. Поставим задачу интереснее все подмножества длины 3
#6.Запуск рекурсии Естественно что для записи мы будем так жеиспользовать рекурсивную структуру, соответственно нам нужно создать новый список списков, определить функцию слияния 2х списков и запустить 2 рекурсии Одну для первого элемента подмножества другую для второго Схема на следующем слайде:

 def rec_launch(core):
    if core.next is None:
        return
    new = rec1(core, core.next))
    return add_back(new, rec1_launch(core.next))

 def add_back(l1, l2, core=None):
    if core is None:
        core = l1
    if l1.next is not None:
        return add_back(l1.next, l2, core)
    else:
        l1.next = l2
        return core

 def rec1(core, cur):
    if cur is not None:
        new = Node(core.el)
        new.next = Node(cur.el)
        new_l.next = rec1(core, cur.text)
        return new_l
    else:
        return None
#6. Идея состоит в дописывании к элементу 1 всех подмножеств длины 2 и запуска той же процедуры для следующего элемента

 def rec2(core):
    if core.next.next is None:
        return
    return add_back(buils(core, rec1_launch(core.next)), rec2(core.next))