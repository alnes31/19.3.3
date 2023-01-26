import requests
import json

#определяем базовые параметры
baseURL='https://petstore.swagger.io/v2'
name_pet1='name_old'
name_pet2='name_new'
#начальные данные о питомце
data={
  "id": 0,
  "category": {"id": 0,"name": "string"},
  "name": name_pet1,
  "photoUrls": ["string"],
  "tags": [{"id": 0,"name": "string"}],
  "status": "available"
}
# основные заголовки для запросов
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Host': 'petstore.swagger.io',
    'Content-Length': '236',
    'Cache-Control': 'no-cache'
}


try:
    print('Первый шаг - делаем запрос на создание питомца')
    # первый запрос - создание нового питомца
    response=requests.post( f"{baseURL}/pet", headers=headers, data=json.dumps(data))
    # если ответ положительный выводим детальные данные и запоминаем id питомца,
    # иначе сообщаем ответ сервера
    if response.status_code==200:
        print('Код ответа - 200 \nСоздан питомец:')
        pet_id=dict(response.json())['id']
        for key in dict(response.json()):
            print(f'{key} - {dict(response.json())[key]}')
    else:
        print(f'Что-то пошло не так\n {response}\n {response.json()}')

    # вносим изменения в данные для создания запроса put
    data["id"]=pet_id
    data["name"]=name_pet2
    print(f'\nменяем имя питомца на {name_pet2}')

    # второй запрос - изменение питомца
    response=requests.put(f"{baseURL}/pet", headers=headers,data=json.dumps(data))
    # если ответ положительный выводим детальные данные,
    # иначе сообщаем ответ сервера
    if response.status_code == 200:
        print('Код ответа - 200 \nВнесены изменения:')
        for key in dict(response.json()):
            print(f'{key} - {dict(response.json())[key]}')
    else:
        print(f'Что-то пошло не так\n {response}\n {response.json()}')

    # третий запрос - получить данные о питомце
    print('\nЗапрашиваем данные с сервера о питомце по id -'+str(pet_id))
    response=requests.get( f"{baseURL}/pet/{pet_id}", headers=headers)
    # если ответ положительный выводим детальные данные,
    # иначе сообщаем ответ сервера
    if response.status_code == 200:
        print('Код ответа - 200 \nНа сервере имеются данные:')
        for key in dict(response.json()):
            print(f'{key} - {dict(response.json())[key]}')
    else:
        print(f'Что-то пошло не так\n {response}\n {response.json()}')

    # четвёртый запрос - удалить питомца
    print('\nУдаляем данные о питомце по id -'+str(pet_id))
    response=requests.delete( f"{baseURL}/pet/{pet_id}", headers=headers)
    # если ответ положительный выводим детальные данные,
    # иначе сообщаем ответ сервера
    if response.status_code == 200:
        print('Код ответа - 200 \nДанные о питомце удалены:')
        for key in dict(response.json()):
            print(f'{key} - {dict(response.json())[key]}')
    else:
        print(f'Что-то пошло не так\n {response}\n {response.json()}')

    # пятый запрос - заново пытаемся получить данные о питомце
    print('\nЗаново запрашиваем данные с сервера о питомце по id -'+str(pet_id))
    response=requests.get( f"{baseURL}/pet/{pet_id}", headers=headers)
    # если ответ положительный выводим детальные данные,
    # иначе сообщаем ответ сервера
    if response.status_code == 200:
        print('Код ответа - 200 \nНа сервере имеются данные:')
        for key in dict(response.json()):
            print(f'{key} - {dict(response.json())[key]}')
    else:
        print(f'Что-то пошло не так\n {response}\n {response.json()}')
except Exception as exception:
    print('\n Что-то пошло совсем не так\n'+str(exception))