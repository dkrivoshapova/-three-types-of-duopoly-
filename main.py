def main():
    """
    Тhe function analyzes three types of duopoly and determines the best option for market participants
    :return: None
    """
    a, b, c = q_d()
    mc1, mc2 = mc()
    tc1 = 0
    tc2 = 0
    if mc1 == 0:
        tc1 = tc()
    if mc2 == 0:
        tc2 = tc()
    if c == 'p':
        a = a / b
        b = 1 / b
    table()
    qc1, qc2 = cournot(a, b, mc1, mc2)
    pc1, pc2, p_p = equilibrium(qc1, qc2, a, b, mc1, mc2, tc1, tc2)
    print('|{:^167s}|'.format('Дуополия Штакельберга, если первый количественный лидер'))
    q1l, q2p = shtakelberg(a, b, mc1, mc2)
    p1l, p2p, p_1l = equilibrium(q1l, q2p, a, b, mc1, mc2, tc1, tc2)
    print('|{:^167s}|'.format('Дуополия Штакельберга, если второй колличественный лидер'))
    q2l, q1p = shtakelberg(a, b, mc2, mc1)
    p1p, p2l, p_2l = equilibrium(q1p, q2l, a, b, mc1, mc2, tc1, tc2)
    print('Для покупателя не выгодна', benefit(p_p, p_1l, p_2l))
    print('Для первого производителя более выгодна', benefit(pc1, p1l, p1p))
    print('Для второго производителя более выгодна', benefit(pc2, p2p, p2l))


def q_d():
    """
    requests a demand function or an inverse demand function
    :return:the coefficients of the demand function and the variable with respect to which it is set
    """
    n = ''
    while True:
        qd = input('Введите функцию рыночного спроса в формате a-bP или обратную функцию спроса a-bQ:').lower().strip()
        if qd.count('q') == 1 and qd.count('p') == 0:
            n = 'q'
        elif qd.count('p') == 1 and qd.count('q') == 0:
            n = 'p'
        p = qd.find(n)
        m = qd.find('-')
        if p > -1 and m > -1:
            try:
                x = float(qd[:m])
                y = float(qd[m + 1:p])
            except ValueError:
                print(qd, 'не является верным значением.Попробуйте ещё раз')
                continue
        else:
            print(qd, 'не является верным значением.Попробуйте ещё раз')
            continue
        return x, y, n


def mc():
    """
    Requests marginal costs of firms
    :return: marginal cost values
    """
    while True:
        o = input('Вам известны предельные издержки фирм? Введите 1 или 0:').lower()
        if o == '1':
            c1 = input('Введите значение предельных издержек первой фирмы:')
            c2 = input('Введите значение предельных издержек второй фирмы:')
            try:
                c1 = float(c1)
                c2 = float(c2)
            except ValueError:
                print(c1, c2, 'не является верным значением.Попробуйте ещё раз')
                continue
        else:
            print('Возможно, нужно найти их самостоятельно. Попробуйте снова')
            print('Придельные издержки-это производная от общих издержек,которые должны быть заданы в условии.')

            continue
        return c1, c2


def tc():
    """
    Requests total costs of firms
    :return: total cost values
    """
    while True:
        tot = input('Введите значение общих издержек первой фирмы или 0:')
        try:
            tot = float(tot)
        except ValueError:
            print(tot, 'не является верным значением.Попробуйте ещё раз')
            continue
        return tot


def cournot(x, y, c1, c2):
    """
    Calculates the output of firms in the cournot duopoly model
    :param x:coefficient of the demand function
    :param y:coefficient of the demand function
    :param c1:marginal cost of the first company
    :param c2:marginal cost of the second company
    :return: output of firms in the cournot duopoly model
    """
    q1 = (x + c2 - 2 * c1) / (3 * y)
    q2 = ((x - c1) / y) - 2 * q1
    print('|{:^167s}|'.format('Дуополия Курно'))
    return q1, q2


def shtakelberg(x, y, cl, cf):
    """
    Calculates the output of firms in the cournot duopoly model
    :param x:coefficient of the demand function
    :param y:coefficient of the demand function
    :param cl:marginal cost of the lieder company
    :param cf:marginal cost of the follow company
    :return: output of firms in the cournot duopoly model
    """
    ql = (x + cf - (2 * cl)) / (2 * y)
    qf = (x - cf) / (2 * y) - ql / 2

    return ql, qf


def equilibrium(p1, p2, x, y, c1, c2, tot1, tot2):
    """

    :param p1: production of the first company
    :param p2: production of the second company
    :param x: coefficient of the demand function
    :param y: coefficient of the demand function
    :param c1: marginal cost of the first company
    :param c2: marginal cost of the second company
    :param tot1: total cost of the first company
    :param tot2: total cost of the second company
    :return: profit of companies and the market price
    """
    q = p1 + p2
    p = x - y * q  # рыночная цена
    if c1 != 0:
        pr1 = (p - c1) * p1  # прибыль первого
    else:
        pr1 = p * p1 - tot1
    if c2 != 0:
        pr2 = (p - c2) * p2  # прибыль второго
    else:
        pr2 = p * p1 - tot2
    d1 = p1 / q  # долярынка первого
    d2 = p2 / q  # доля рынка второго
    print('|' + '_' * 167 + '|')
    print(
        '|{:^20.2f}|{:^20.2f}|{:^20.2f}|{:^20.2f}|{:^20.2f}|{:^20.2f}|{:^20.2%}|{:^20.2%}|'.format(p1, p2, q, p, pr1,
                                                                                                   pr2, d1, d2))
    print('|' + '_' * 167 + '|')
    return pr1, pr2, p


def table():
    """
    Create a table for calculated market equilibrium parameters
    :return:None.
    """
    print('_' * 168)
    t = ['Равновесный объем', 'Равновесная цена', 'Прибыль', 'Рыночная доля']
    w = ['первого', 'второго', 'рынка', '']
    print('|{:^20s}|{:^20s}|{:^20s}|{:^20s}|{:^20s}|{:^20s}|{:^20s}|{:^20s}|'.format(t[0], t[0], t[0], t[1], t[2], t[2],
                                                                                     t[3], t[3]))
    print('|{:^20s}|{:^20s}|{:^20s}|{:^20s}|{:^20s}|{:^20s}|{:^20s}|{:^20s}|'.format(w[0], w[1], w[2], w[2], w[0], w[1],
                                                                                     w[0], w[1]))
    print('_' * 168)


def benefit(x, y, z):
    """
    Determines the best option for a particular market participant
    :param x:value in duopoly of Cournot
    :param y:value in duopoly of Shtakelberg. lieder- first company
    :param z:value in duopoly of Shtakelberg. lieder- second company
    :return: the most profitable type of duopoly
    """
    t = max(x, y, z)
    if t == x:
        u = 'Дуаполия Курно'
    elif t == y:
        u = 'Дуаполия Штакельберга, если первый колличественный лидер'
    else:
        u = 'Дуополия Штакельберга, если второй колличественный лидер'
    return u


main()
