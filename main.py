def number(k,n):
    s = 0
    count = [1, 1] + [0] * (n - 1)
    for i in range(2, k + 1):
        count[i] = count[i - 1] * 2

    for i in range(k + 1, n + 1):
        count[i] = count[i - 1] * 2 - count[i - 1 - k]
        s = count[i]
        return s

    print("Кількість способів:", number(k, n))

try:
    k = int(input("Сходинки,які можна перестрибнути:"))
    n = int(input("Всі сходинки:"))
    result = number(k,n)
    if k >= n:
        print("Введено неправильні дані")
    elif  k <= 0 or n <= 0:
        print("Введено неправильні дані")
    else:
        print(result)

except ValueError:
    print("Використано не відповідний тип даних")
except Exception:
    print("Помилка!")







