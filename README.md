# Neoversity. Algorithms 2. Homework 2

goit-algo2-hw-02

## Завдання 1. Пошук максимального та мінімального елементів

Реалізуйте функцію, яка знаходить максимальний та мінімальний елементи в масиві, використовуючи метод «розділяй і володарюй».

### Реалізація [task_1.py](src/task_1.py)

Приклад тестів

``` bash
Min: 1, Max: 9 of [3, 1, 4, 1, 5, 9, 2, 6, 5]
Min: -5, Max: -1 of [-1, -2, -3, -4, -5]
Min: 42, Max: 42 of [42]
Min: 3, Max: 3 of [3, 3]
Min: 1, Max: 3 of [3, 1]
All tests passed.
```

## Завдання 2. Оптимізація черги 3D-принтера в університетській лабораторії

Розробіть програму для оптимізації черги завдань 3D-друку з урахуванням пріоритетів та технічних обмежень принтера, використовуючи жадібний алгоритм.

Опис завдання

1. Використовуйте вхідні дані у вигляді списку завдань на друк, де кожне завдання містить: ID, об'єм моделі, пріоритет та час друку.

2. Реалізуйте основну функцію `optimize_printing`, яка буде:
    * Враховувати пріоритети завдань.
    * Групувати моделі для одночасного друку.
    * Перевіряти обмеження об'єму та кількості.
    * Розраховувати загальний час друку.
    * Повертати оптимальний порядок друку.

3. Виведіть оптимальний порядок друку та загальний час виконання всіх завдань.

### Реалізація [task_2.py](src/task_2.py)

Формат результату змінений для відображення групування завдань для друку.

Приклад тестів

``` bash
Тестування оптимізації черги 3D-друку
Обмеження принтера:
PrinterConstraints(max_volume=300, max_items=2)
----------------------------------------

Тест 1 (однаковий пріоритет):
[PrintJob(id='M1', volume=100, priority=1, print_time=120),
 PrintJob(id='M2', volume=150, priority=1, print_time=90),
 PrintJob(id='M3', volume=120, priority=1, print_time=150)]

Порядок друку:
[PrintGroup(jobs=['M2', 'M1'], total_volume=250, print_time=120),
 PrintGroup(jobs=['M3'], total_volume=120, print_time=150)]
Загальний час: 270 хвилин
----------------------------------------

Тест 2 (різні пріоритети):
[PrintJob(id='M1', volume=100, priority=2, print_time=120),
 PrintJob(id='M2', volume=150, priority=1, print_time=90),
 PrintJob(id='M3', volume=120, priority=3, print_time=150)]

Порядок друку:
[PrintGroup(jobs=['M2', 'M1'], total_volume=250, print_time=120),
 PrintGroup(jobs=['M3'], total_volume=120, print_time=150)]
Загальний час: 270 хвилин
----------------------------------------

Тест 3 (перевищення обмежень):
[PrintJob(id='M1', volume=250, priority=1, print_time=180),
 PrintJob(id='M2', volume=200, priority=1, print_time=150),
 PrintJob(id='M3', volume=180, priority=2, print_time=120)]

Порядок друку:
[PrintGroup(jobs=['M2'], total_volume=200, print_time=150),
 PrintGroup(jobs=['M1'], total_volume=250, print_time=180),
 PrintGroup(jobs=['M3'], total_volume=180, print_time=120)]
Загальний час: 450 хвилин
----------------------------------------

Тест 4 (занадто великий розмір):
[PrintJob(id='M1', volume=350, priority=1, print_time=180),
 PrintJob(id='M2', volume=200, priority=1, print_time=150),
 PrintJob(id='M3', volume=180, priority=2, print_time=120)]

Порядок друку:
[PrintGroup(jobs=['M2'], total_volume=200, print_time=150),
 PrintGroup(jobs=['M3'], total_volume=180, print_time=120)]
Загальний час: 270 хвилин
```
