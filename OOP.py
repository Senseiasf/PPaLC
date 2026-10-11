import sys
import math

class BiquadraticEquation:
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.roots = []

    def get_coef(self, index, prompt):
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

    def read_coefficients(self):
        self.a = self.get_coef(1, 'Введите коэффициент А:')
        self.b = self.get_coef(2, 'Введите коэффициент B:')
        self.c = self.get_coef(3, 'Введите коэффициент C:')

    def calculate_roots(self):
        result = set()
        a, b, c = self.a, self.b, self.c

        if a == 0.0:
            print("Уравнение не биквадратное.")
            if b != 0.0:
                t = -c / b
                if t > 0.0:
                    result.add(math.sqrt(t))
                    result.add(-math.sqrt(t))
                elif t == 0.0:
                    result.add(0.0)
        else:
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
                        
        self.roots = sorted(list(result))

    def print_roots(self):
        if not self.roots:
            print('Нет действительных корней')
        else:
            print(f'Количество корней: {len(self.roots)}')
            print(f'Корни: {", ".join(map(str, self.roots))}')


def main():
    equation = BiquadraticEquation()
    
    equation.read_coefficients()
    equation.calculate_roots()
    equation.print_roots()

if __name__ == "__main__":
    main()