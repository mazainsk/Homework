# Функция send_email, которая принимает 2 обычных аргумента (message(сообщение), recipient(получатель)) и 1 обязательно
# именованный аргумент со значением по умолчанию sender = "university.help@gmail.com"

def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    list_of_domains = ('.com', '.ru', '.net')   # Кортеж из доменов, одним из которых должны оканчиваться адреса
    # п.2. Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
    # то вывести на экран (в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>"
    if (('@' not in recipient) or ('@' not in sender) or not recipient.endswith(list_of_domains) or not
        sender.endswith(list_of_domains)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    # п.3. Если <sender> и <recipient> совпадают, то вывести "Нельзя отправить письмо самому себе!"
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    # п.4. Если отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено
    # с адреса <sender> на адрес <recipient>"
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    # п.5. В противном случае вывести сообщение "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender>
    # на адрес <recipient>"
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    return

# Проверка на тестовых данных.
send_email('Это сообщение для проверки связи','vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')