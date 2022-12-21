"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
import lorem
from collections import Counter


def generate_chat_history() -> list:
    messages_amount = random.randint(200, 1000)
    users_ids = list({random.randint(1, 10000) for _ in range(random.randint(5, 20))})
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages: list = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice([None, random.choice([m["id"] for m in messages]) if messages else []]),
            "seen_by": random.sample(users_ids, random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def find_user_with_the_most_posts(messages: list) -> int:
    sender_list = [
        message['sent_by']
        for message in messages
    ]
    id_max_number_messages = Counter(sender_list).most_common(1)[0][0]
    return id_max_number_messages


def find_post_with_the_most_reply(messages: list) -> str:
    reply_for_list = [
        message['reply_for']
        for message in messages
        if message['reply_for']
    ]
    id_max_reply_message = Counter(reply_for_list).most_common(1)[0][0]
    for message in messages:
        if message['id'] == id_max_reply_message:
            id_user_max_reply_for = message['sent_by']
            break
    return id_user_max_reply_for


def find_user_with_the_highest_views(messages: list) -> str:
    dict_users_views: dict = {}
    for message in messages:
        if message['id'] in dict_users_views:
            dict_users_views[message['id']] += len(message['seen_by'])
        else:
            dict_users_views[message['id']] = len(message['seen_by'])
    return max(dict_users_views, key= lambda key: dict_users_views[key])


def find_the_busiest_time(messages: list) -> str:
    noon_hour = 12
    evening_hour = 18
    sent_morning = [
       message['sent_by'] 
       for message in messages
       if message['sent_at'].hour <= noon_hour
    ]
    sent_afternoon = [
        message['sent_by'] 
        for message in messages
        if message['sent_at'].hour > noon_hour and 
        message['sent_at'].hour < evening_hour
    ]
    sent_evening = [
       message['sent_by'] 
       for message in messages
       if message['sent_at'].hour >= evening_hour
    ]
    max_len_sent = len(sent_morning)
    result_time_of_day = 'утром'
    if len(sent_afternoon) > max_len_sent:
        max_len_sent = len(sent_afternoon)
        result_time_of_day = 'днем'
    if len(sent_evening) > max_len_sent:
        max_len_sent = len(sent_evening)
        result_time_of_day = 'вечером'
    return result_time_of_day


def make_dict(input_list_without_reply: list, input_list_with_reply: list) -> dict:
    message_with_len_reply_for = {} 
    for message_without_reply_for in input_list_without_reply: #берем пользователя с "первоначальным" сообщением
        thread_length = 0
        element_to_compare = message_without_reply_for['id']
        for _ in range (0, len(input_list_with_reply)):
            for message_with_reply_for in input_list_with_reply: #берем пользователя с сообщением-ответом
                if message_with_reply_for['reply_for'] == element_to_compare:
                    thread_length += 1
                    element_to_compare = message_with_reply_for['id']
                    break
        message_with_len_reply_for[message_without_reply_for['id']] = thread_length #формируем словарь - id: длина треда
    return message_with_len_reply_for    


def find_id_max_reply_chain(messages: list) -> str|None:
    messages_without_reply_for = [
        message
        for message in messages
        if not message['reply_for']
    ]      
    messages_with_reply_for = [
        message
        for message in messages
        if message['reply_for']
    ]
    dict_result = make_dict(messages_without_reply_for, messages_with_reply_for)
    return max(dict_result, key= lambda key: dict_result[key])


if __name__ == '__main__':
    messages = generate_chat_history()
    print(f'ID пользователя, отправившего больше всего сообщений: {find_user_with_the_most_posts(messages)}')
    print(f'ID пользователя, на сообщения которого больше всего отвечали: {find_post_with_the_most_reply(messages)}')
    print(f'ID пользователя, чьи сообщения видели больше всего уникальных пользователей: {find_user_with_the_highest_views(messages)}')
    print(f'Чаще всего пользователи отправляют сообщения {find_the_busiest_time(messages)}')
    print(f'Началом самому длинному треду послужило сообщение: {find_id_max_reply_chain(messages)}')