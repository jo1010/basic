# дано натуральное число N, вывести все натуральные числа от 1 до N

def values(n, current=1):
    if current <= n:
        print(current)
        values(current=current+1, n=n)

values(10)

print('\n', '='*20, '\n')
# дано натуральное число N. Вывести YESб если число N является точной степенью двойки, или слово NO в противном случае
def check_pow_2(n):
    if n == 1:
        print('YES')
    else:
        if n % 2 == 0:
            check_pow_2(n // 2)
        else:
            print('NO')

check_pow_2(16)

print('\n', '='*20, '\n')

# дано натуральное число N. Вычислите сумму его цифр
def sum_val(num, res=0):
    if not num:
        return res
    res += num % 10
    num //= 10
    return sum_val(num, res)

print(sum_val(345))
