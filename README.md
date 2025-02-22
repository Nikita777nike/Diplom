## Веб-приложение "Сайт Бугульминского медицинского колледжа"

## **Описание проекта**

"Сайт Бугульминского медицинского колледжа" — это веб-приложение предназначенное для управления учебными процессами
в медицинском колледже. Основная цель приложения заключается в предоставлении студентам и преподавателям
удобного доступа к информации об успеваемости, расписании занятий, учебной программе и другим важным аспектам
учебного процесса 

## **Основные особенности:**

- **Регистрация** пользователей.
- **Авторизация** пользователей.
- При регистрации пользователя ему присваивается логин и пароль, посредством которых он может посещать личный кабинет.


## **Технологии:**

- **Django** 5.1.3
- **DB Browser for SQlite** (база данных)
- **Python 3.x**

## **Зависимости**
```bash
Для работы проекта требуется установить зависимости, приведенные в файле:
- requirements.txt
```
## **Установка и запуск проекта**

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/Nikita777nike/Diplom.git                                    
перейдите в директорию проекта cd medical_college
```
### 2. Создайте виртуальное окружение и активируйте его
```bash
python -m venv myenv
source myenv/bin/activate   # для Linux/MacOS
myenv\Scripts\activate      # для Windows
```
### 3. Установите зависимости
```bash
pip install -r requirements.txt
```
###  4. Примените миграции базы данных
```bash
python manage.py migrate
```
### 5. Создайте суперпользователя для доступа к админ-панели
```bash
python manage.py createsuperuser
```
### 6. Запустите сервер
```bash
python manage.py runserver
```
Теперь проект доступен по адресу: http://127.0.0.1:8000/.



