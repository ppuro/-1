from functools import *

# это функция, описывающая ходы игроков
# здесь мы создаём массив, в который закидываем подходящие нам значения для куч

def move(m1, m2):
    x = []
    if m1 > 0:
        x.append((m1 - 1, m2))
    if m2 > 0:
        x.append((m1, m2 - 1))
    if m1 > 1:
        x.append(((m1 + 1) // 2, m2))
    if m2 > 1:
        x.append((m1, (m2 + 1) // 2))
    return x

# это функция, описывающая ход игры.
# её логика в том, что мы отсылаемся на результат прошлой победы так же,
# как и в решении задания ручками или в экселе

# мы можем сказать, что артём достигает победы за один ход после того, как
# попадает в 'win!' хотя бы один из его ходов

# аналогично яна побеждает своим первым ходом, если попадает в 'artem1',
# но уже каждым из своих ходов

# артём побеждает своим вторым ходом,
# если хотя бы один его ход ведёт в 'yana1'

# яна же побеждает своим вторым ходом,
# если все её ходы ведут в 'artem1' или 'artem2'

@lru_cache(None)
def game(t):
    a, b = t
    if a + b <= 40:
        return 'win!'
    if any(game(i) == 'win!' for i in move(a, b)):
        return 'artem1'
    if all(game(i) == 'artem1' for i in move(a, b)):
        return 'yana1'
    if any(game(i) == 'yana1' for i in move(a, b)):
        return 'artem2'
    if all(game(i) == 'artem1' or game(i) == 'artem2' for i in move(a, b)):
        return 'yana2'

for i in range(80, 10, -1):
    t = 25, i
    print(i, game(t))
