def averageSalary(salary):
    min_salary = float('inf')
    max_salary = float('-inf')
    total_sum = 0
    
    for s in salary:
        if s < min_salary:
            min_salary = s
        if s > max_salary:
            max_salary = s
        total_sum += s
    
    valid_count = len(salary) - 2
    sum_valid_salaries = total_sum - min_salary - max_salary
    
    average = sum_valid_salaries / valid_count
    
    return average

salary = [4000, 3000, 1000, 2000]
print("Input:", salary)
print("Output:", averageSalary(salary))  # Output: 2500.0
