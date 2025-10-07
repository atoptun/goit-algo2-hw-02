from typing import List, Optional
from dataclasses import dataclass
from pprint import pprint


@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int


@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


@dataclass
class PrintGroup:
    jobs: List[str]
    total_volume: float
    print_time: int


@dataclass
class PrintJobOrder:
    print_order: Optional[List[PrintGroup]]
    total_time: Optional[int]


def optimize_printing(print_jobs: List[PrintJob], constraints: PrinterConstraints) -> PrintJobOrder:
    """
    Оптимізує чергу 3D-друку згідно з пріоритетами та обмеженнями принтера

    Args:
        print_jobs (List[PrintJob]): Список завдань на друк
        constraints (PrinterConstraints): Обмеження принтера

    Returns:
        PrintJobOrder: порядок друку та загальний час друку
    """
    jobs_sorted = sorted(print_jobs, key=lambda j: (j.priority, j.print_time))

    total_time = 0
    print_order = []

    while jobs_sorted:
        current_group = []
        current_volume = 0
        current_items = 0

        for job in jobs_sorted:
            if (
                current_volume + job.volume <= constraints.max_volume
                and current_items + 1 <= constraints.max_items
                # and job.priority == jobs_sorted[i].priority  # if need to group by priority
            ):
                current_group.append(job)
                current_volume += job.volume
                current_items += 1
            else:
                continue 

        if not current_group:
            break  # too large job

        group_time = max(job.print_time for job in current_group)
        total_time += group_time

        print_order.append(PrintGroup(
            jobs=[job.id for job in current_group],
            total_volume=current_volume,
            print_time=group_time
        ))

        for job in current_group:
            jobs_sorted.remove(job)

    return PrintJobOrder(print_order=print_order, total_time=total_time)


# Тестування
def test_printing_optimization():
    # Тест 1: Моделі однакового пріоритету
    test1_jobs = [
        PrintJob(id="M1", volume=100, priority=1, print_time=120),
        PrintJob(id="M2", volume=150, priority=1, print_time=90),
        PrintJob(id="M3", volume=120, priority=1, print_time=150),
    ]

    # Тест 2: Моделі різних пріоритетів
    test2_jobs = [
        PrintJob(id="M1", volume=100, priority=2, print_time=120),  # лабораторна
        PrintJob(id="M2", volume=150, priority=1, print_time=90),   # дипломна
        PrintJob(id="M3", volume=120, priority=3, print_time=150),   # особистий проєкт
    ]

    # Тест 3: Перевищення обмежень об'єму
    test3_jobs = [
        PrintJob(id="M1", volume=250, priority=1, print_time=180),
        PrintJob(id="M2", volume=200, priority=1, print_time=150),
        PrintJob(id="M3", volume=180, priority=2, print_time=120)
    ]

    # Тест 4: Занадто великий об'єм
    test4_jobs = [
        PrintJob(id="M1", volume=350, priority=1, print_time=180),
        PrintJob(id="M2", volume=200, priority=1, print_time=150),
        PrintJob(id="M3", volume=180, priority=2, print_time=120)
    ]

    constraints = PrinterConstraints(
        max_volume=300,
        max_items=2
    )

    print("Тестування оптимізації черги 3D-друку")
    print(f"Обмеження принтера:")
    pprint(constraints)

    print("-" * 40)
    print("Тест 1 (однаковий пріоритет):")
    pprint(test1_jobs)
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"\nПорядок друку:")
    pprint(result1.print_order)
    print(f"Загальний час: {result1.total_time} хвилин")

    print("-" * 40)
    print("\nТест 2 (різні пріоритети):")
    pprint(test2_jobs)
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"\nПорядок друку:")
    pprint(result2.print_order)
    print(f"Загальний час: {result2.total_time} хвилин")
    
    print("-" * 40)
    print("\nТест 3 (перевищення обмежень):")
    pprint(test3_jobs)
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"\nПорядок друку:")
    pprint(result3.print_order)
    print(f"Загальний час: {result3.total_time} хвилин")

    print("-" * 40)
    print("\nТест 4 (занадто великий розмір):")
    pprint(test4_jobs)
    result4 = optimize_printing(test4_jobs, constraints)
    print(f"\nПорядок друку:")
    pprint(result4.print_order)
    print(f"Загальний час: {result4.total_time} хвилин")


if __name__ == "__main__":
    test_printing_optimization()
