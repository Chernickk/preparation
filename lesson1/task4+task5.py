def deposit(amount: float, months: int, month_income):
    def count_month_income(month_income, percent):
        amount = 0
        for i in range(1, months - 1):
            amount += month_income + month_income * (percent / i)
        return amount

    deposit_v1 = {
        'begin_sum': 1000,
        'end_sum': 10000,
        6: 0.05,
        12: 0.06,
        24: 0.05,
    }
    deposit_v2 = {
        'begin_sum': 10000,
        'end_sum': 100000,
        6: 0.06,
        12: 0.07,
        24: 0.065,
    }
    deposit_v3 = {
        'begin_sum': 100000,
        'end_sum': 1000000,
        6: 0.07,
        12: 0.08,
        24: 0.075,
    }
    deposits = [deposit_v1, deposit_v2, deposit_v3]
    for dep in deposits:
        if dep['begin_sum'] <= amount < dep['end_sum']:
            percent = dep.get(months)
            if percent:
                return (months / 12 * percent) * amount + amount + count_month_income(month_income, percent)
            raise ValueError('Недопустимый срок вклада')
    raise ValueError('Недопустимая сумма вклада')


if __name__ == '__main__':
    print(deposit(100000, 6, 10000))
