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


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list({random.randint(1, 10000) for _ in range(random.randint(5, 20))})
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
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


def user_with_the_most_posts(messages: list) -> int:
    sender_list = [
        message['sent_by']
        for message in messages
    ]
    id_max_number_messages = Counter(sender_list).most_common(1)[0][0]
    return id_max_number_messages


def post_with_the_most_reply(messages: list) -> str:
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


def users_with_the_highest_views(messages: list) -> str:
    seen_by_list = [
        len(message['seen_by'])
        for message in messages
    ]
    pos_max_seen_by = [
        index for index, data in enumerate(seen_by_list)
        if data == max(seen_by_list)
    ]
    ids_max_seen_by = [
        message['id']
        for index, message in enumerate(messages) 
        if index in pos_max_seen_by 
    ]
    return str(ids_max_seen_by).strip('[]')


def the_busiest_time(messages: list) -> str:
    dict_of_lists_sent = {}
    sent_morning = [
       message['sent_by'] 
       for message in messages
       if message['sent_at'].hour <= 12
    ]
    dict_of_lists_sent["утром"] = len(sent_morning)
    sent_afternoon = [
        message['sent_by'] 
        for message in messages
        if message['sent_at'].hour > 12 and 
        message['sent_at'].hour < 18
    ]
    dict_of_lists_sent["днем"] = len(sent_afternoon)
    sent_evening = [
       message['sent_by'] 
       for message in messages
       if message['sent_at'].hour >= 18
    ]
    dict_of_lists_sent["вечером"] = len(sent_evening)
    return max(dict_of_lists_sent, key=dict_of_lists_sent.get)


if __name__ == "__main__":
    messages = generate_chat_history()
    print(f'ID пользователя, отправившего больше всего сообщений: {user_with_the_most_posts(messages)}')
    print(f'ID пользователя, на сообщения которого больше всего отвечали: {post_with_the_most_reply(messages)}')
    print(f'ID пользователей, чьи сообщения видели больше всего уникальных пользователей: {users_with_the_highest_views(messages)}')
    print(f'Чаще всего пользователи отправляют сообщения {the_busiest_time(messages)}')