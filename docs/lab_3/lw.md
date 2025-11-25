# Лабораторная работа №2

## Описание варианта работы

> В качестве варианта работы было выбрано `Задание 9` из ["Основы баз данных"](https://drive.google.com/file/d/174gPjJ7AOHfzteYcobPY0x7sFBTkN1Xx/view?usp=sharing).

Создать программную систему, предназначенную для диспетчера автобусного парка частной транспортной фирмы. Фима обслуживает несколько коммерческих маршрутов. Такая система должна обеспечивать хранение сведений о водителях, о маршрутах и характеристиках автобусов.

Каждый водитель характеризуется паспортными данными, классом, стажем работы и окладом, причем оклад зависит от класса и стажа работы.

Маршрут автобуса характеризуется номером маршрута, названием начального и конечного пункта движения, временем начала и конца движения, интервалом движения и протяженностью в минутах (время движения от кольца до кольца). Характеристиками автобуса являются: номер государственной регистрации автобуса, его тип и вместимость, причем вместимость автобуса зависит от его типа.

Каждый водитель закреплен за определенным автобусом и работает на определенном маршруте, но в случае поломки своего автобуса или болезни другого водителя может пересесть на другую машину.

В базе должен храниться график работы водителей.

Необходимо предусмотреть возможность корректировки БД в случаях поступления на работу нового водителя, списания старого автобуса, введения нового маршрута или изменения старого и т.п.

Диспетчеру автопарка могут потребоваться следующие сведения:

- Список водителей, работающих на определенном маршруте с указанием графика их работы?
- Когда начинается и заканчивается движение автобусов на каждом маршруте?
- Какова общая протяженность маршрутов, обслуживаемых автопарком?
- Какие автобусы не вышли на линию в заданный день и по какой причине (неисправность, отсутствие водителя)?
- Сколько водителей каждого класса работает в автопарке?

Необходимо предусмотреть возможность выдачи отчета по автопарку, сгруппированного по типам автобусов, с указанием маршрутов, обслуживаемых автобусами каждого типа. Для маршрутов должны быть указаны все характеристики, включая списки автобусов и водителей, обслуживающих каждый маршрут. Отчёт должен содержать сведения о суммарной протяжённости обслуживаемых маршрутов, о количестве имеющихся в автопарке автобусов каждого типа, о количестве водителей, их среднем возрасте и стаже.

## Выполнение работы

### Реализация модели базы данных средствами DjangoORM

Основываясь на требованиях задания, была разработана следующая модель базы данных средствами DjangoORM:

```python title="bus_depot_project/bus_depot_app/models.py"
class BusType(models.Model):
    """
    Тип автобуса.
    """
    name = models.CharField(max_length=50, verbose_name="Название")
    capacity = models.PositiveIntegerField(verbose_name="Вместимость")

    class Meta:
        verbose_name = "Тип автобуса"
        verbose_name_plural = "Типы автобусов"
    
    def __str__(self):
        return f"{self.name} (число мест: {self.capacity})"


class Bus(models.Model):
    """
    Автобус.
    """
    license_plate = models.CharField(
        max_length=10, 
        unique=True,
        verbose_name="Номер"
    )
    bus_type = models.ForeignKey(
        BusType,
        on_delete=models.CASCADE,
        related_name='buses',
        verbose_name="Тип автобуса"
    )
    is_active = models.BooleanField(verbose_name="Действующий")
    purchase_date = models.DateField(verbose_name="Дата приобретения")

    class Meta:
        verbose_name = "Автобус"
        verbose_name_plural = "Автобусы"
    
    def __str__(self):
        return f"{self.license_plate} ({self.bus_type.name})"


class Route(models.Model):
    """
    Маршрут.
    """
    number = models.CharField(max_length=10, unique=True, verbose_name="Номер маршрута")
    start_point = models.CharField(max_length=100, verbose_name="Начальный пункт")
    end_point = models.CharField(max_length=100, verbose_name="Конечный пункт")
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")
    interval = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Интервал движения (мин)"
    )
    duration = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Протяженность (мин)"
    )

    class Meta:
        verbose_name = "Маршрут"
        verbose_name_plural = "Маршруты"
    
    def __str__(self):
        return f"{self.number} ({self.start_point} - {self.end_point})"


class Driver(models.Model):
    """
    Водитель.
    """
    CLASS_CHOICES = [
        ('1', 'Первый класс'),
        ('2', 'Второй класс'),
        ('3', 'Третий класс'),
    ]

    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    passport = models.CharField(
        max_length=10, 
        unique=True, 
        verbose_name="Серия и номер паспорта"
    )
    birth_date = models.DateField(verbose_name="Дата рождения")
    driver_class = models.CharField(
        max_length=1,
        choices=CLASS_CHOICES,
        verbose_name="Класс водителя"
    )
    experience = models.PositiveIntegerField(
        verbose_name="Стаж (лет)"
    )
    salary = models.PositiveIntegerField(
        verbose_name="Оклад"
    )
    main_bus = models.ForeignKey(
        Bus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='main_drivers',
        verbose_name="Основной автобус"
    )
    main_route = models.ForeignKey(
        Route,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='main_drivers',
        verbose_name="Основной маршрут"
    )

    class Meta:
        verbose_name = "Водитель"
        verbose_name_plural = "Водители"
    
    def __str__(self):
        return f"{self.full_name} (автобус: {self.main_bus.license_plate}, маршрут: {self.main_route.number})"


class DriverAssignment(models.Model):
    """
    Назначение водителя.
    """
    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        related_name='assignments',
        verbose_name="Водитель"
    )
    bus = models.ForeignKey(
        Bus,
        on_delete=models.CASCADE,
        related_name='assignments',
        verbose_name="Автобус"
    )
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name='assignments',
        verbose_name="Маршрут"
    )
    date = models.DateField(verbose_name="Дата работы")
    start_time = models.TimeField(verbose_name="Время начала смены")
    end_time = models.TimeField(verbose_name="Время окончания смены")

    class Meta:
        verbose_name = "Назначение водителя"
        verbose_name_plural = "График работы водителей"
    
    def __str__(self):
        return f"{self.driver} на {self.bus} ({self.date})"


class BusStatus(models.Model):
    """
    Статус автобуса.
    """
    STATUS_CHOICES = [
        ('active', 'На линии'),
        ('not_active', 'Не на линии'),
        ('broken', 'Неисправность'),
        ('no_driver', 'Отсутствие водителя'),
    ]

    bus = models.ForeignKey(
        Bus,
        on_delete=models.CASCADE,
        related_name='statuses',
        verbose_name="Автобус"
    )
    date = models.DateField(verbose_name="Дата")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        verbose_name="Статус"
    )
    reason = models.TextField(
        blank=True,
        verbose_name="Причина отсутствия"
    )

    class Meta:
        verbose_name = "Статус автобуса"
        verbose_name_plural = "Статусы автобусов"
        unique_together = ['bus', 'date']

    def __str__(self):
        return f"{self.bus} - {self.status} ({self.date})"
```

### Реализация логики работы API средствами Django REST Framework (используя методы сериализации)

#### Реализация базовых CRUD-операций

В первую очередь для каждой модели из `models.py` были реализованы базовые CRUD-ы. Для этого для каждой модели бал создан базовый сериализатор:

```python title="bus_depot_project/bus_depot_app/serializers.py"
class BusTypeSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для типа автобуса.
    """
    class Meta:
        model = BusType
        fields = '__all__'


class BusSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для автобуса.
    """
    class Meta:
        model = Bus
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для маршрута.
    """
    class Meta:
        model = Route
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для водителя.
    """
    class Meta:
        model = Driver
        fields = '__all__'


class DriverAssignmentSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для назначения водителя.
    """
    class Meta:
        model = DriverAssignment
        fields = '__all__'


class BusStatusSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для статуса автобуса.
    """
    class Meta:
        model = BusStatus
        fields = '__all__'
```

Используя созданные сериализаторы были реализованы представления на основе ViewSet для основных CRUD-операций:

```python title="bus_depot_project/bus_depot_app/views.py"
class BusTypeViewSet(viewsets.ModelViewSet):
    """
    ViewSet для типа автобуса.
    """
    serializer_class = BusTypeSerializer
    queryset = BusType.objects.all()


class BusViewSet(viewsets.ModelViewSet):
    """
    ViewSet для автобуса.
    """
    serializer_class = BusSerializer
    queryset = Bus.objects.all()


class RouteViewSet(viewsets.ModelViewSet):
    """
    ViewSet для маршрута.
    """
    serializer_class = RouteSerializer
    queryset = Route.objects.all()


class DriverViewSet(viewsets.ModelViewSet):
    """
    ViewSet для водителя.
    """
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


class DriverAssignmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для назначения водителя.
    """
    serializer_class = DriverAssignmentSerializer
    queryset = DriverAssignment.objects.all()


class BusStatusViewSet(viewsets.ModelViewSet):
    """
    ViewSet для статуса автобуса.
    """
    serializer_class = BusStatusSerializer
    queryset = BusStatus.objects.all()
```

Далее эти представления были зарегистрированы в URLs:

```python title="bus_depot_project/bus_depot_app/urls.py"
router = DefaultRouter()
router.register('bus-types', BusTypeViewSet)
router.register('buses', BusViewSet)
router.register('routes', RouteViewSet)
router.register('drivers', DriverViewSet)
router.register('driver-assignments', DriverAssignmentViewSet)
router.register('bus-statuses', BusStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

В результате были реализованы базовые API-эндпоинты для создания, получения, изменения и удаления всех моделей.

#### Реализация специальных API-эндпоинтов

Помимо базовых CRUD-операций, в задании требовалось написать несколько специальных API-эндпоинтов, которые реализуют более сложную механику. В результате были реализованы следующие специальные эндпоинты:

##### Список водителей, работающих на определённом маршруте с указанием графика их работы

Сериализаторы:

```python title="bus_depot_project/bus_depot_app/serializers.py"
class DriverWithAssignmentsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для водителя с его назначениями.
    """
    assignments = serializers.SerializerMethodField()

    class Meta:
        model = Driver
        fields = '__all__'
    
    def get_assignments(self, obj):
        assignments = DriverAssignment.objects.filter(driver=obj)
        return DriverAssignmentSerializer(assignments, many=True).data


class RouteDriversSerializer(serializers.Serializer):
    """
    Сериализатор для маршрута с водителями и их графиком работы.
    """
    route = RouteSerializer()
    drivers = DriverWithAssignmentsSerializer(many=True)
```

Представление:

```python title="bus_depot_project/bus_depot_app/views.py"
class RouteDriversAPIView(APIView):
    """
    Список водителей, работающих на определённом маршруте с указанием графика их работы.
    """
    def get(self, request, route_id):
        # Получаем маршрут
        try:
            route = Route.objects.get(pk=route_id)
        except Route.DoesNotExist:
            return Response(
                {"error": "Маршрут не найден"}, 
                status=status.HTTP_404_NOT_FOUND
            )

        # Получаем всех водителей, для которых этот маршрут является основным
        drivers = Driver.objects.filter(main_route=route).distinct()

        # Преобразуем данные в JSON
        serializer = RouteDriversSerializer({
            'route': route,
            'drivers': drivers
        })

        # Возвращаем данные
        return Response(serializer.data)
```

URLs:

```python title="bus_depot_project/bus_depot_app/urls.py"
urlpatterns = [
    # ...
    path('routes/<int:route_id>/drivers/', RouteDriversAPIView.as_view()),
    # ...
]
```

Пример запроса:

```
GET /bus-depot/routes/1/drivers/
```

Пример ответа:

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "route": {
        "id": 1,
        "number": "R1",
        "start_point": "ул. Дзержинского, 18",
        "end_point": "ул. Полевая, 24",
        "start_time": "08:00:00",
        "end_time": "20:00:00",
        "interval": 15,
        "duration": 50
    },
    "drivers": [
        {
            "id": 1,
            "assignments": [
                {
                    "id": 1,
                    "date": "2025-01-01",
                    "start_time": "08:00:00",
                    "end_time": "16:00:00",
                    "driver": 1,
                    "bus": 1,
                    "route": 1
                }
            ],
            "full_name": "Фролов Олег Николаевич",
            "passport": "2365898564",
            "birth_date": "1980-05-02",
            "driver_class": "1",
            "experience": 5,
            "salary": 80000,
            "main_bus": 1,
            "main_route": 1
        },
        {
            "id": 2,
            "assignments": [
                {
                    "id": 2,
                    "date": "2024-09-06",
                    "start_time": "10:00:00",
                    "end_time": "18:00:00",
                    "driver": 2,
                    "bus": 2,
                    "route": 1
                },
                {
                    "id": 3,
                    "date": "2024-10-06",
                    "start_time": "10:00:00",
                    "end_time": "18:00:00",
                    "driver": 2,
                    "bus": 2,
                    "route": 2
                }
            ],
            "full_name": "Кузнецов Николай Егорович",
            "passport": "5236956324",
            "birth_date": "1996-07-02",
            "driver_class": "2",
            "experience": 3,
            "salary": 70000,
            "main_bus": 2,
            "main_route": 1
        }
    ]
}
```
