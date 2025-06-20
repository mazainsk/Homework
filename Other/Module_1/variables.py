homeworks_done = 12
hours_passed = 1.5
course_name = 'Python'
average_time_of_homework = hours_passed / homeworks_done
# вариант с разделителями в виде пробела (вывод с параметрами по-умолчанию):
print('Курс:', course_name, ',', 'всего задач:', homeworks_done, ',', 'затрачено часов:', hours_passed, ',',
      'среднее время выполнения', average_time_of_homework, 'часа.')

# вариант без пробелов после двоеточий и перед запятыми:
print('Курс:', course_name, ', ', 'всего задач:', homeworks_done, ', ', 'затрачено часов:', hours_passed, ', ',
      'среднее время выполнения ', average_time_of_homework, ' часа.', sep='')