import vk_api
import random

'''
Отправка сообщений от имени группы. token - токен группы, которая отправит сообщение. 
Для отправки воспользуйтесь функцией send_messages, передав ей 3 параметра:
    type_of_chat ('d' если отправляем в беседу или 'u', если в личку)
    chai_id (id чата куда отправляем)
    message (текст отправляемого сообщения)
В послденей строке - мой id vk, для теста
'''

def send_message(type_of_chat, chat_id, message):
    if type_of_chat == 'd':
        vk_session.method('messages.send', {'chat_id': chat_id, 'message': message, 'random_id': random.randint(0, 999999)})
    elif type_of_chat == 'u':
        vk_session.method('messages.send', {'user_id': chat_id, 'message': message, 'random_id': random.randint(0, 999999)})

vk_session = vk_api.VkApi(token='Вставь сюда токен')

send_message('u', 565312948, 'Привет, Олеж :D')
