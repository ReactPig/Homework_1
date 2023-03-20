numb = int(input())
numb_smash = [int(a) for a in str(numb)]
numb_summ = sum(numb_smash)
print(f'Сумма чисел числа {numb!r} равна {numb_summ!r}')