import sys
import math

def get_coef(index: int, prompt: str) -> float:
    try:
        return float(sys.argv[index])
    except (IndexError, ValueError):
        pass

    while True:
        try:
            return float(input(prompt + "\n"))
        except ValueError:
            print("Введено некорректное значение. Коэффициент должен быть числом. Повторите ввод.")

def solve_biquadratic(a: float, b: float, c: float) -> list[float]:
    def roots_from_t(t: float) -> list[float]:
        match t:
            case t_val if t_val > 0:
                return [math.sqrt(t_val), -math.sqrt(t_val)]
            case 0.0:
                return [0.0]
            case _: 
                return []
    match a:
        case 0.0:
            print("Уравнение не биквадратное.")
            match b:
                case 0.0:
                    return []
                case _:
                    return roots_from_t(-c / b)
        case _:
            D = b**2 - 4*a*c
            match D:
                case d_val if d_val < 0:
                    return []
                case 0.0:
                    return roots_from_t(-b / (2 * a))
                case d_val if d_val > 0:
                    t1 = (-b + math.sqrt(d_val)) / (2 * a)
                    t2 = (-b - math.sqrt(d_val)) / (2 * a)
                    unique_roots = set(roots_from_t(t1) + roots_from_t(t2))
                    return sorted(list(unique_roots))

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    
    roots = solve_biquadratic(a, b, c)

    match roots:
        case []:
            print('Нет действительных корней')
        case [root]:
            print(f'Один корень: {root}')
        case [root1, root2]:
            print(f'Два корня: {root1}, {root2}')
        case _:
            print(f'Количество корней: {len(roots)}')
            print(f'Корни: {", ".join(map(str, roots))}')

if __name__ == "__main__":
    main()