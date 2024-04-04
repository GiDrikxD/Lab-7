Лабораторна робота №7

1)Вибрав ресурс зі списку №1, а саме:
https://api.nationalize.io?name=nathaniel (Predict the nationality of a person based on their name)

Відповіді на питання:
1.що саме робить даний ресурс ?
2.які запити може виконувати ?
3.яку інформацію повертає чи що є результатом його роботи ?

1.Ресурс надає можливість визначити ймовірність національності особи за її ім'ям.
2.Ресурс може обробляти GET-запити з параметром "name", який вказує на ім'я особи.
3.Результатом роботи ресурсу є JSON-об'єкт, що містить інформацію про ймовірність національності зазначеної особи.

2) Використав інсрумент Postman, після чого відправив запит на отримання даних, він може повернути в json html txt audio і т.д. Я додав парамерт "Name" і отримав результат у форматі JSON:
{
    "count": 3122,
    "name": "nathaniel",
    "country": [
        {
            "country_id": "NG",
            "probability": 0.2352432337002168
        },
        {
            "country_id": "NE",
            "probability": 0.137354391876446
        },
        {
            "country_id": "GH",
            "probability": 0.11362954237051442
        },
        {
            "country_id": "TT",
            "probability": 0.041206317562933796
        },
        {
            "country_id": "ID",
            "probability": 0.03877026949809868
        }
    ]
}

3) Зробив 5 різних параметризованих запитів з іменами "John" "Maria" "Roman" "Anna" "Carl"
Результати виведені у форматі JSON, результат наступний: 
1. John:


{
    "count": 136264,
    "name": "John",
    "country": [
        {
            "country_id": "NG",
            "probability": 0.0847435026716119
        },
        {
            "country_id": "TZ",
            "probability": 0.07038672160263389
        },
        {
            "country_id": "AE",
            "probability": 0.05800438209322167
        },
        {
            "country_id": "UG",
            "probability": 0.045333820693221824
        },
        {
            "country_id": "KE",
            "probability": 0.04406318128902763
        }
    ]
}

2. Maria:
{
    "count": 103665,
    "name": "Maria",
    "country": [
        {
            "country_id": "RO",
            "probability": 0.29107594268186776
        },
        {
            "country_id": "PT",
            "probability": 0.07103462525721099
        },
        {
            "country_id": "BR",
            "probability": 0.06521526340901339
        },
        {
            "country_id": "GR",
            "probability": 0.05664307753255076
        },
        {
            "country_id": "AO",
            "probability": 0.025285502952772786
        }
    ]
}

3. Roman:
{
    "count": 59858,
    "name": "Roman",
    "country": [
        {
            "country_id": "PR",
            "probability": 0.12834665672857143
        },
        {
            "country_id": "RO",
            "probability": 0.07814698764327964
        },
        {
            "country_id": "PE",
            "probability": 0.058174475536889064
        },
        {
            "country_id": "EC",
            "probability": 0.04822744891855228
        },
        {
            "country_id": "MX",
            "probability": 0.046845504497183665
        }
    ]
}

4. Anna:
{
    "count": 42364,
    "name": "Anna",
    "country": [
        {
            "country_id": "HU",
            "probability": 0.10508578119566725
        },
        {
            "country_id": "CN",
            "probability": 0.09578586958845405
        },
        {
            "country_id": "IT",
            "probability": 0.07341197078419195
        },
        {
            "country_id": "RU",
            "probability": 0.04469582117194373
        },
        {
            "country_id": "UA",
            "probability": 0.040442227016543396
        }
    ]
}

5. Carl:
{
    "count": 9203,
    "name": "Carl",
    "country": [
        {
            "country_id": "CN",
            "probability": 0.1764293777840477
        },
        {
            "country_id": "GH",
            "probability": 0.06547238425593764
        },
        {
            "country_id": "DE",
            "probability": 0.05771826812097546
        },
        {
            "country_id": "US",
            "probability": 0.04965152006036107
        },
        {
            "country_id": "HK",
            "probability": 0.027361593420391853
        }
    ]
}

4) Пайтон код вище.
Опис запиту: Цей код виконує GET-запит на ресурс з вказаним іменем, отримує відповідь у форматі JSON та виводить ймовірності національностей для вказаного імені у зручному форматі.
