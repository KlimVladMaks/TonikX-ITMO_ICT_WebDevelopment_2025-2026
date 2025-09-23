# Практическая работа №2.2

## Практическое задание 1

Правильно настроить связь между автомобилем, владением и владельцем.

### Выполнение задания 1

Чтобы реализовать связь "многие-ко-многим" между владельцем и автомобилем через владение, воспользуемся полем `ManyToManyField`:

```python title="django_project_klimenkov/project_first_app/models.py"
class Owner(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)

    # Добавим это поле для реализации связи "многие-ко-многим"
    cars = models.ManyToManyField('Car', through='Ownership')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
```

Теперь связь между владельцем и автомобилем стала более полной, что даёт возможность в перспективе обращаться к автомобилям через их владельца и к владельцам через автомобиль, которым они обладали или обладают.

Чтобы применить эти изменения нужно будет сделать миграцию:

```
python3 manage.py makemigrations project_first_app
python3 manage.py migrate
```
