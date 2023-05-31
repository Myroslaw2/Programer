def calculate_project_estimate(tasks):
    estimates = []
    for task in tasks:
        a, m, b = task
        task_estimate = (a + 4 * m + b) / 6
        task_sd = (b - a) / 6
        estimates.append((task_estimate, task_sd))

    project_estimate = sum(estimate[0] for estimate in estimates)
    project_sd = sum(estimate[1] for estimate in estimates)

    confidence_interval_min = project_estimate - 2 * project_sd
    confidence_interval_max = project_estimate + 2 * project_sd

    return confidence_interval_min, confidence_interval_max


# Запит користувача на введення оцінок завдань
num_tasks = int(input("Введіть кількість завдань: "))
tasks = []
for i in range(num_tasks):
    print(f"Завдання {i + 1}:")
    a = float(input("Оцінка a: "))
    m = float(input("Оцінка m: "))
    b = float(input("Оцінка b: "))
    tasks.append((a, m, b))

# Розрахунок оцінки проекту та довірчого інтервалу
confidence_interval_min, confidence_interval_max = calculate_project_estimate(tasks)

# Виведення результатів
print(f"Project's 95% confidence interval: {confidence_interval_min} ... {confidence_interval_max} points")