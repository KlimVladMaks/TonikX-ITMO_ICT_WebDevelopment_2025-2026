# Практическая работа №2.1

## Практическое задание 1

Необходимо установить Django Web framework любым доступным способом.

**Формат именований файлов:**

- Формат имени Django-проекта: “django_project_фамилия”.
- Формат имени Django-приложения: “project_first_app”.

### Выполнение задания 1

В первую очередь создадим venv-окружение для работы с Python и запустим его. Для этого выполним в терминале следующие команды:

```
python3 -m venv .venv
source .venv/bin/activate
```

Теперь установим Django:

```
pip install django
```

Создадим новый django-проект:

```
django-admin startproject django_project_klimenkov
```

А внутри этого проекта создадим новое приложение:

```
python3 manage.py startapp project_first_app
```

В результате нами был успешно установлен Django Web framework и создан базовый проект с приложением внутри. Теперь наш проект имеет следующую структуру файлов:

![1](../img/lab_2/pw_1/1.png)

Можно также проверить что проект создан корректно, запустив его на localhost с помощью команды:

```
python3 manage.py runserver
```

![2](../img/lab_2/pw_1/2.png)

И увидеть, что в браузере по адресу `http://127.0.0.1:8000/` находится приветственная страница Django:

![3](../img/lab_2/pw_1/3.png)

## Практическое задание 2.1

В проекте создать модель данных об автовладельцах в соответствии с рисунком:

![4](../img/lab_2/pw_1/4.png)

Указание: Таблицы и атрибуты именовать только на латинице.

Важно! Не забывайте о внешних ключах, полях выбора, правильном оформлении ассоциативной сущности в модели.

### Выполнение задания 2.1

В Django модели хранятся в файле `models.py`. Создадим в этом файле необходимые модели в соответствии с рисунком:

```python title="django_project_klimenkov/project_first_app/models.py"
from django.db import models
from django.contrib.auth.models import AbstractUser


class Owner(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    license_plate = models.CharField(max_length=15)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.model} ({self.license_plate})"


class DrivingLicense(models.Model):
    LICENSE_TYPES = [
        ('A', 'Категория A'),
        ('B', 'Категория B'),
        ('C', 'Категория C'),
        ('D', 'Категория D'),
        ('BE', 'Категория BE'),
        ('CE', 'Категория CE'),
        ('DE', 'Категория DE'),
        ('Tm', 'Категория Tm'),
        ('Tb', 'Категория Tb'),
        ('M', 'Категория M'),
        ('A1', 'Подкатегория A1'),
        ('B1', 'Подкатегория B1'),
        ('C1', 'Подкатегория C1'),
        ('D1', 'Подкатегория D1'),
        ('C1E', 'Подкатегория C1E'),
        ('D1E', 'Подкатегория D1E'),
    ]

    license_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10, choices=LICENSE_TYPES)
    issue_date = models.DateField()

    def __str__(self):
        return f"{self.license_number} ({self.license_type})"


class Ownership(models.Model):
    ownership_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.owner} - {self.car} ({self.start_date} - {self.end_date})"
```

Для создания модели автовладельца воспользуемся `AbstractUser`, который уже содержит в себе поля `first_name`, `last_name` и `id`, а значит можно в классе модели их не указывать.

Для создания всех остальных моделей воспользуемся более общей `Model`, для которой ID указывать нужно.

Типы данных задаём с помощью `django.db.models` (`AutoField` - для ID, `DateField` - для дат, `CharField` - для строковых значений, `ForeignKey` - для внешних ключей).

Связь "многие ко многим" между автовладельцами и автомобилями реализуем с помощью отдельной модели `Ownership`.

Делаем поле `license_type` для `DrivingLicense` выборным с помощью параметра `choices=LICENSE_TYPES`, где `LICENSE_TYPES` - список с допустимыми значениями.

Для полей, которые могут быть необязательными, указываем параметры `null=True, blank=True`.
