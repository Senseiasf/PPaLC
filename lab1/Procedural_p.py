import sys
import math

def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
        coef = float(coef_str)
        return coef
    except:
        pass

    while True:
        print(prompt)
        coef_str = input()
        try:
            coef = float(coef_str)
            return coef
        except ValueError:
            print("Введено некорректное значение. Коэффициент должен быть числом. Повторите ввод.")


def get_roots(a, b, c):
    result = set() 
    
    if a == 0.0:
        print("Уравнение не биквадратное.")
        if b != 0.0:
            t = -c / b
            if t > 0.0:
                result.add(math.sqrt(t))
                result.add(-math.sqrt(t))
            elif t == 0.0:
                result.add(0.0)
        return sorted(list(result))
    
    D = b * b - 4 * a * c

    if D == 0.0:
        t = -b / (2.0 * a)
        if t > 0.0:
            result.add(math.sqrt(t))
            result.add(-math.sqrt(t))
        elif t == 0.0:
            result.add(0.0)
    elif D > 0.0:
        sqD = math.sqrt(D)
        t1 = (-b + sqD) / (2.0 * a)
        t2 = (-b - sqD) / (2.0 * a)
        
        for t in (t1, t2):
            if t > 0.0:
                result.add(math.sqrt(t))
                result.add(-math.sqrt(t))
            elif t == 0.0:
                result.add(0.0)

    return sorted(list(result))


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    
    roots = get_roots(a, b, c)

    if not roots:
        print('Нет действительных корней')
    else:
        print(f'Количество корней: {len(roots)}')
        print(f'Корни: {", ".join(map(str, roots))}')

if __name__ == "__main__":
    main()