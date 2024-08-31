
def send_email (massage, recipient, *, sender='university.help@gmail.com'):
    recipient_chek = False
    sender_chek = False
    if '@' not in recipient:
        recipient_chek = True
    else:
        if recipient.endswith('.ru'):
            recipient_chek = False
        elif recipient.endswith('.net'):
            recipient_chek = False
        elif recipient.endswith('.com'):
            recipient_chek = False
        else:
            recipient_chek = True
    if '@' not in sender:
        sender_chek = True
    else:
        if sender.endswith('.ru'):
            sender_chek = False
        elif sender.endswith('.net'):
            sender_chek = False
        elif sender.endswith('.com'):
            sender_chek = False
        else:
            sender_chek = True
    if recipient_chek and sender_chek:
        print(f'Ошибка в адресах отправителя и получателя. Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient_chek:
        print(f'Ошибка в адресе получателя. Невозможно Отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender_chek:
            print(f'Ошибка в адресе отправителя. Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса: {sender} на адрес: {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса: {sender} на адрес: {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru.uk', sender='urban.teacher@mail.ru')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru.uk', sender='urban.teacher@mail.ru.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
