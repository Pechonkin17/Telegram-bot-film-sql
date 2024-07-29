Створено телеграм бота з цілю запису фільмуів, які я переглянув. Тому, що з часом забуваю які фільми я дивився (якщо це не цікаві фільми), після перегляду можна добавити фільм в телеграм бота додавши коментар і свою оцінку. реалізовано такі функції: створення фільмів, виведення інформації про конкретний фільм, видалення фільму, оновлення фільму, показ усіх фільмів, показ усіх команд, кнопка назад, кнопка перейти за посиланням, меню:

![image](https://github.com/user-attachments/assets/4ea88261-5762-4687-a4fa-45f1f361626e)

Усі команди є опрацьовані, тобто, всі помилки і команди обробленні.

Переглянути бота: https://t.me/Film_2024_v1_bot

Опис команд бота:

1. Команда отримати всі фільми:

![image](https://github.com/user-attachments/assets/498cc3f1-84dd-4fe0-9ee0-50c631a9645b)

Якщо немає фільмів у списку:

![image](https://github.com/user-attachments/assets/d29d1997-2703-4308-95f4-a0c9608f8bc0)

2. Команда отримати детальну інформацію про фільм:

![image](https://github.com/user-attachments/assets/648f59c7-d20a-4711-8ce2-0242c1a501e6)

3. Команда створення бота:

![image](https://github.com/user-attachments/assets/dccd1380-0a81-4288-8101-6913e9465638)

![image](https://github.com/user-attachments/assets/7fc9c4c9-ce1f-4adc-8781-fa86a7e116f4)

Після створення фільму виводиться інформація про фільм Якщо ввести команду (/films, /start, /help, ... etc) - буде припинено форму для створення фільму і бот не буде очікувати наступні поля для вводу

![image](https://github.com/user-attachments/assets/f21e0ba5-a6fd-4cc1-9858-f34a61813a3e)

Є автоматична перевірка посилання, за допомогою validators. Посилання буде записане - якщо відкривається

![image](https://github.com/user-attachments/assets/187c6e5d-dc4c-43b3-821e-3ec636e8ee2f)

4. Функція оновлення інформації про фільм:

![image](https://github.com/user-attachments/assets/dc2861f1-93b4-40ca-98bb-01856d4725ac)

Якщо фільму з такою назвою немає:

![image](https://github.com/user-attachments/assets/75b03507-3a3e-46f5-8894-ba69ffa6e57c)

Перервання команди /update_film:

![image](https://github.com/user-attachments/assets/320dd33e-04ef-41ab-bc89-bd54da6c53f6)

![image](https://github.com/user-attachments/assets/d061bf00-7732-4da6-8c6c-79d55f148641)

5. Видалення фільму:

![image](https://github.com/user-attachments/assets/7de4c75f-ac60-4bd6-b883-de4e60931432)

Якщо назва фільму не існує або немає в mySQL:

![image](https://github.com/user-attachments/assets/96377a3e-31ba-4d5e-a177-8059076299a5)

6. Пошук фільму за назвою. Якщо знайдено 1 фільм - повернення детальної інформації про цей фільм. В іншому випадку - повернення списку фільмів з цією назвою.

![image](https://github.com/user-attachments/assets/2b373ef5-328b-455d-aff7-d18c13957189)

Або

![image](https://github.com/user-attachments/assets/b24ac999-1145-49af-b149-2780b20f4c0a)

Або

![image](https://github.com/user-attachments/assets/b75f9a30-a479-4a10-83ce-5fb7c5e59adf)

![image](https://github.com/user-attachments/assets/99d724e9-40ef-4ee3-95fc-1bb5ba1300cd)

7. Інструкція з командами:

![image](https://github.com/user-attachments/assets/72361bf6-2be2-433f-b5d9-64cb13a4f7fb)

8. Початок роботи бота:

![image](https://github.com/user-attachments/assets/70c1acf7-3ada-4e4d-a926-06c1ac32308f)
