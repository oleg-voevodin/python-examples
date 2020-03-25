from datetime import datetime
import vk_api
import random

try:
    login = input('VK логин: ')
    password = input('VK пароль: ')

    try:
        vk_session = vk_api.VkApi(login, password, app_id='2685278')
        vk_session.auth()
    except BadPassword:
        print('Bad password!'); exit()
    except vk_api.exceptions.AuthError:
        vk_session = vk_api.VkApi(login, password, app_id='2685278', auth_handler=lambda: [input('Enter two-factor auth code'), False])
        vk_session.auth()

    vk = vk_session.get_api()

    print('\nСписок ваших друзей: ')

    for k in vk.friends.get(fields='city')['items']:
        is_online = 'онлайн' if k['online'] == 1 else 'оффлайн'
        is_closed = 'закрытый' if k['is_closed'] == True else 'открытый'
        try:
            print(f' Найден друг: {k["first_name"]} {k["last_name"]} с ID {k["id"]} из города {k["city"]["title"]}, его профиль - {is_closed}. Сейчас он {is_online}. Last activity: {datetime.fromtimestamp(vk.messages.getLastActivity(user_id=k["id"])["time"]).strftime("%d-%m-%Y %H:%M:%S")}')
        except:
            print(f' Найден друг: {k["first_name"]} {k["last_name"]} с ID {k["id"]}, его профиль - {is_closed}. Сейчас он {is_online}. Last activity: {datetime.fromtimestamp(vk.messages.getLastActivity(user_id=k["id"])["time"]).strftime("%d-%m-%Y %H:%M:%S")}')


    print('\nСписок сообществ, в которых вы состоите: ')

    for k in vk.groups.get()['items']:
        for c in vk.groups.getById(group_id=k):
            print(f'Найдена группа \'{c["name"]}\' с ID: {c["id"]}')

    vk.wall.post(message=input('Введите сообщение, которое хотите запостить на Вашей стене: '))

    message = input('Сообщение, которое будет отправлено всем друзьям (введите 0 для отмены): ')
    if message != '0':
        for friend in vk.friends.get()['items']:
            vk.messages.send(user_id=friend, random_id=random.randint(0, 131767), message=message)
                  
    print('Информация о постах на Вашей стене: ')

    for k in vk.wall.get()['items']:
        try:
            is_pinned = 'Да' if k['is_pinned'] else 'Нет'
        except:
            is_pinned = 'Нет'

        try:
            if k['attachments']:
                attachments = k['attachments']
        except:
            attachments = '\n\tВ этом посте нет вложений'

        if k['comments'] != 0:
            comments = vk.wall.getComments(post_id=k['id'])['items']

        is_archived = 'Да' if k['is_archived'] == 1 else 'Нет'

        print('\n===== НАЧАЛО ПОСТА =====')
        print(f'\n ID поста: {k["id"]}')
        print(f'\n ID автора: {k["from_id"]}')
        print(f'\n ID владельца страницы: {k["owner_id"]}')
        print(f'\n Закреплен: {is_pinned}, архивирован: {is_archived}')
        print(f'\n Лайков: {k["likes"]["count"]}, репостов: {k["reposts"]["count"]}')
        print(f'\n Текст поста: {k["text"]}')
        print(f'\n= = = НАЧАЛО ВЛОЖЕНИЙ = = = \n{attachments}\n\n= = = КОНЕЦ ВЛОЖЕНИЙ = = =')
        if comments:
            print('\n= = = НАЧАЛО КОММЕНТАРИЕВ = = =')
            for k in comments:
                print(f'\nНайден комментарий: {k}\n')
            print('\n= = = КОНЕЦ КОММЕНТАРИЕВ = = =')
        print('\n===== КОНЕЦ ПОСТА =====')
except KeyboardInterrupt:
    print('\nGoodbye :D'); exit()
