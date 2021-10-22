import time

class Transposition:
    def __init__(self, filename) -> None:
        self.modes = ['multi', 'exp']
        self.mode = str()
        self.transposes = list()
        self.clear_transposes = list()
        self.read_from_file(filename)
        self.deg = int()
        
    def read_from_file(self, filename) -> None:
        quantity = 0
        with open(filename) as file_handler:
            for line in file_handler:
                line = line.replace('\n', '')
                if line in self.modes:
                    self.mode = line
                else:
                    if self.mode in self.modes:
                        quantity += 1
                        self.transposes.append(self.find_transpos(line))
                        temp = line.replace('(', '')
                        temp = temp.replace(')', '')
                        temp = temp.replace('  ', '')
                        self.clear_transposes.append(temp.split())
                        self.clear_transposes[quantity - 1] = list(map(int, self.clear_transposes[quantity - 1]))
                        if self.mode == 'exp':
                            self.transposes.append(self.transposes[0])
                            self.clear_transposes[quantity - 1] = self.clear_transposes[0]
                            #self.clear_transposes[1] = self.clear_transposes[0]
                        if self.mode == self.modes[0] and quantity > 2:
                            self.transposes = list()
                            print('Too much values. For mode "multi" you can use only 2 transpositions')
                            break
                        elif self.mode == self.modes[1] and quantity > 2:
                            print('Too much values. For mode "exp" you can use only 1 transpositions')
                            self.transposes = list()
                        # print('Q:', quantity, 'L:', line)
                    else:
                        print('First string have to be mode')
                        break
        # self.transposes[0] = list(map(int, self.transposes[0]))
        # self.transposes[1] = list(map(int, self.transposes[1]))


    def debug(self) -> None:
        print('Mode:', self.mode)
        for transpos in self.transposes:
            print(transpos)

    def max_len(self) -> int:
        lengths = [0, 0]
        for i in range(2):
            for item in self.transposes[i]:
                lengths[i] += len(item)
        if lengths[0] > lengths[1]:
            return lengths[0]
        else:
            return lengths[1]

    def min_unused(self, used) -> int:
        for number in used:
            if number in self.clear_transposes[1]:
                self.clear_transposes[1].remove(number)
        try:
            return min(self.clear_transposes[1])
        except ValueError:
            return 0

    def multiplication(self) -> str:
        indexes = {'b1': 0, 'b2': 0, 'a1': 0, 'a2': 0}
        values = {'b1': 1, 'b2': 0, 'a1': 0, 'a2': 0}
        result = str()
        startes = [1]
        used = [1]
        result += '( ' + str(1) + ' '
        for i in range(self.max_len()):
            temp_expression = list()
            for expression in self.transposes[1]:
                if values['b1'] in expression:
                    indexes['b1'] = expression.index(values['b1'])
                    length = len(expression)
                    temp_expression = list(expression)
            if indexes['b1'] < length - 1:
                indexes['b2'] = indexes['b1'] + 1
            else:
                indexes['b2'] = 0
            values['b2'] = temp_expression[indexes['b2']]
            for expression in self.transposes[0]:
                if values['b2'] in expression:
                    indexes['a1'] = expression.index(values['b2'])
                    length = len(expression)
                    temp_expression = list(expression)
            if indexes['a1'] < length - 1:
                indexes['a2'] = indexes['a1'] + 1
            else:
                indexes['a2'] = 0
            values['a2'] = temp_expression[indexes['a2']] 
            values['a1'] = temp_expression[indexes['a1']]
            if self.mode == 'multi':
                print(values['b1'], '->', values['b2'], 'to', values['a1'], '->', values['a2'])
            if values['a2'] in startes:
                min = self.min_unused(used)
                if min == 0:
                    break
                used.append(min)
                startes.append(min)
                # print(')', end=' ')
                values = {'b1': min, 'b2': 0, 'a1': 0, 'a2': 0}
                # print('(', min, end=' ')
                result += ') ( ' + str(min) + ' '
            else:
                # print(values['a2'], end=' ')
                result += str(values['a2']) + ' '
                used.append(values['a2'])
                values = {'b1': values['a2'], 'b2': 0, 'a1': 0, 'a2': 0}
            indexes = {'b1': 0, 'b2': 0, 'a1': 0, 'a2': 0}
        result += ')'
        # print(')')
        return result

    def find_transpos(self, string) -> list:
        mass, temp = list(), list()
        number = str()
        new_flag = False
        for char in string:
            if char == '(':
                new_flag = True
            elif new_flag and char not in [' ', '(', ')']:
                number += char
            elif char == ')':
                new_flag = False
                mass.append(temp)
                temp = []
            if len(number) > 0 and char == ' ':
                temp.append(int(number))
                number = str()
        return mass

    def exponentiation(self) -> None:
        result = None
        self.deg = int(input('Введите степень для перемножения, позязя: '))
        for i in range(self.deg - 1):
            # print('Transpos before:', self.transposes[1])
            # print('Clear before:', self.clear_transposes[1])
            result = self.multiplication()
            print('^' + str(i + 2) + ': ' + result)
            self.transposes[1] = self.find_transpos(result)
            temp = result.replace('(', '')
            temp = temp.replace(')', '')
            temp = temp.replace('  ', '')
            temp = temp.split()
            self.clear_transposes[1] = list(map(int, temp))


t = Transposition('ex.txt')
#print(t.transposes[0], t.transposes[1])
#print(t.clear_transposes)
if t.mode == 'multi':
    print('Result:', t.multiplication())
elif t.mode == 'exp':
    start = time.time()
    t.exponentiation()
    end = time.time()
    print('Вычисление заняло ' + str(round(end - start, 5)) + 'с')
