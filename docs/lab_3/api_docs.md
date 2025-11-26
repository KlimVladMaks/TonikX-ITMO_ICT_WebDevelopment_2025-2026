# Документация для API-эндпоинтов

## Базовые API-эндпоинты

### `GET /bus-depot/bus-types/`

Тело запроса не требуется.

Формат ответа:

```json
[
    {
        "id": <id>,
        "name": <название>,
        "capacity": <вместимость>
    },
    <...>
]
```

### `POST /bus-depot/bus-types/`

Формат тела запроса:

```json
{
    "name": <название>,
    "capacity": <вместимость>
}
```

### `GET /bus-depot/bus-types/<id>/`

Тело запроса не требуется.

Формат ответа:

```json
{
    "id": <id>,
    "name": <название>,
    "capacity": <вместимость>
}
```

### `PUT /bus-depot/bus-types/<id>/`

Формат тела запроса:

```json
{
    "name": <название>,
    "capacity": <вместимость>
}
```

### `PATCH /bus-depot/bus-types/<id>/`

Формат тела запроса:

```json
{
    "name": <название>,
    "capacity": <вместимость>
}
```

### `DELETE /bus-depot/bus-types/<id>/`

Тело запроса не требуется.

### `GET /bus-depot/buses/`

Тело запроса не требуется.

Формат ответа:

```json
[
    {
        "id": <id>,
        "license_plate": <номер>,
        "is_active": <действующий>,
        "purchase_date": <дата_приобретения>,
        "bus_type": <тип_автобуса>
    },
    <...>
]
```

### `POST /bus-depot/buses/`

Формат тела запроса:

```json
{
    "license_plate": <номер>,
    "is_active": <действующий>,
    "purchase_date": <дата_приобретения>,
    "bus_type": <тип_автобуса>
}
```

### `GET /bus-depot/buses/<id>/`

Тело запроса не требуется.

Формат ответа:

```json
{
    "id": <id>,
    "license_plate": <номер>,
    "is_active": <действующий>,
    "purchase_date": <дата_приобретения>,
    "bus_type": <тип_автобуса>
}
```

### `PUT /bus-depot/buses/<id>/`

Формат тела запроса:

```json
{
    "license_plate": <номер>,
    "is_active": <действующий>,
    "purchase_date": <дата_приобретения>,
    "bus_type": <тип_автобуса>
}
```

### `PATCH /bus-depot/buses/<id>/`

Формат тела запроса:

```json
{
    "license_plate": <номер>,
    "is_active": <действующий>,
    "purchase_date": <дата_приобретения>,
    "bus_type": <тип_автобуса>
}
```

### `DELETE /bus-depot/buses/<id>/`

Тело запроса не требуется.

### `GET /bus-depot/routes/`

Тело запроса не требуется.

Формат ответа:

```json
[
    {
        "id": <id>,
        "number": <номер>,
        "start_point": <начальный_пункт>,
        "end_point": <конечный_пункт>,
        "start_time": <время_начала>,
        "end_time": <время_окончания>,
        "interval": <интервал_движения_мин>,
        "duration": <протяжённость_мин>
    },
    <...>
]
```

### `POST /bus-depot/routes/`

Формат тела запроса:

```json
{
    "number": <номер>,
    "start_point": <начальный_пункт>,
    "end_point": <конечный_пункт>,
    "start_time": <время_начала>,
    "end_time": <время_окончания>,
    "interval": <интервал_движения_мин>,
    "duration": <протяжённость_мин>
}
```

### `GET /bus-depot/routes/<id>/`

Тело запроса не требуется.

Формат ответа:

```json
{
    "id": <id>,
    "number": <номер>,
    "start_point": <начальный_пункт>,
    "end_point": <конечный_пункт>,
    "start_time": <время_начала>,
    "end_time": <время_окончания>,
    "interval": <интервал_движения_мин>,
    "duration": <протяжённость_мин>
}
```

### `PUT /bus-depot/routes/<id>/`

Формат тела запроса:

```json
{
    "number": <номер>,
    "start_point": <начальный_пункт>,
    "end_point": <конечный_пункт>,
    "start_time": <время_начала>,
    "end_time": <время_окончания>,
    "interval": <интервал_движения_мин>,
    "duration": <протяжённость_мин>
}
```

### `PATCH /bus-depot/routes/<id>/`

Формат тела запроса:

```json
{
    "number": <номер>,
    "start_point": <начальный_пункт>,
    "end_point": <конечный_пункт>,
    "start_time": <время_начала>,
    "end_time": <время_окончания>,
    "interval": <интервал_движения_мин>,
    "duration": <протяжённость_мин>
}
```

### `DELETE /bus-depot/routes/<id>/`

Тело запроса не требуется.

### `GET /bus-depot/drivers/`

Тело запроса не требуется.

Формат ответа:

```json
[
    {
        "id": <id>,
        "full_name": <фио>,
        "passport": <номер_паспорта>,
        "birth_date": <дата_рождения>,
        "driver_class": <класс_водителя>,
        "experience": <опыт_лет>,
        "salary": <зарплата>,
        "main_bus": <основной_автобус>,
        "main_route": <основной_маршрут>
    },
    <...>
]
```

### `POST /bus-depot/drivers/`

Формат тела запроса:

```json
{
    "full_name": <фио>,
    "passport": <номер_паспорта>,
    "birth_date": <дата_рождения>,
    "driver_class": <класс_водителя>,
    "experience": <опыт_лет>,
    "salary": <зарплата>,
    "main_bus": <основной_автобус>,
    "main_route": <основной_маршрут>
}
```

### `GET /bus-depot/drivers/<id>/`

Тело запроса не требуется.

Формат ответа:

```json
{
    "id": <id>,
    "full_name": <фио>,
    "passport": <номер_паспорта>,
    "birth_date": <дата_рождения>,
    "driver_class": <класс_водителя>,
    "experience": <опыт_лет>,
    "salary": <зарплата>,
    "main_bus": <основной_автобус>,
    "main_route": <основной_маршрут>
}
```

### `PUT /bus-depot/drivers/<id>/`

Формат тела запроса:

```json
{
    "full_name": <фио>,
    "passport": <номер_паспорта>,
    "birth_date": <дата_рождения>,
    "driver_class": <класс_водителя>,
    "experience": <опыт_лет>,
    "salary": <зарплата>,
    "main_bus": <основной_автобус>,
    "main_route": <основной_маршрут>
}
```

### `PATCH /bus-depot/drivers/<id>/`

Формат тела запроса:

```json
{
    "full_name": <фио>,
    "passport": <номер_паспорта>,
    "birth_date": <дата_рождения>,
    "driver_class": <класс_водителя>,
    "experience": <опыт_лет>,
    "salary": <зарплата>,
    "main_bus": <основной_автобус>,
    "main_route": <основной_маршрут>
}
```

### `DELETE /bus-depot/drivers/<id>/`

Тело запроса не требуется.

### `GET /bus-depot/driver-assignments/`

Тело запроса не требуется.

Формат ответа:

```json
[
    {
        "id": <id>,
        "date": <дата>,
        "start_time": <время_начала_смены>,
        "end_time": <время_окончания_смены>,
        "driver": <водитель>,
        "bus": <автобус>,
        "route": <маршрут>
    },
    <...>
]
```

### `POST /bus-depot/driver-assignments/`

Формат тела запроса:

```json
{
    "date": <дата>,
    "start_time": <время_начала_смены>,
    "end_time": <время_окончания_смены>,
    "driver": <водитель>,
    "bus": <автобус>,
    "route": <маршрут>
}
```

### `GET /bus-depot/driver-assignments/<id>/`

Тело запроса не требуется.

Формат ответа:

```json
{
    "id": <id>,
    "date": <дата>,
    "start_time": <время_начала_смены>,
    "end_time": <время_окончания_смены>,
    "driver": <водитель>,
    "bus": <автобус>,
    "route": <маршрут>
}
```

### `PUT /bus-depot/driver-assignments/<id>/`

Формат тела запроса:

```json
{
    "date": <дата>,
    "start_time": <время_начала_смены>,
    "end_time": <время_окончания_смены>,
    "driver": <водитель>,
    "bus": <автобус>,
    "route": <маршрут>
}
```

### `PATCH /bus-depot/driver-assignments/<id>/`

Формат тела запроса:

```json
{
    "date": <дата>,
    "start_time": <время_начала_смены>,
    "end_time": <время_окончания_смены>,
    "driver": <водитель>,
    "bus": <автобус>,
    "route": <маршрут>
}
```

### `DELETE /bus-depot/driver-assignments/<id>/`

Тело запроса не требуется.

### `GET /bus-depot/bus-statuses/`

Тело запроса не требуется.

Формат ответа:

```json
[
    {
        "id": <id>,
        "date": <дата>,
        "status": <статус>,
        "reason": <причина>,
        "bus": <автобус>
    },
    <...>
]
```

### `POST /bus-depot/bus-statuses/`

Формат тела запроса:

```json
{
    "date": <дата>,
    "status": <статус>,
    "reason": <причина>,
    "bus": <автобус>
}
```

### `GET /bus-depot/bus-statuses/<id>/`

Тело запроса не требуется.

Формат ответа:

```json
{
    "id": <id>,
    "date": <дата>,
    "status": <статус>,
    "reason": <причина>,
    "bus": <автобус>
}
```

### `PUT /bus-depot/bus-statuses/<id>/`

Формат тела запроса:

```json
{
    "date": <дата>,
    "status": <статус>,
    "reason": <причина>,
    "bus": <автобус>
}
```

### `PATCH /bus-depot/bus-statuses/<id>/`

Формат тела запроса:

```json
{
    "date": <дата>,
    "status": <статус>,
    "reason": <причина>,
    "bus": <автобус>
}
```

### `DELETE /bus-depot/bus-statuses/<id>/`

Тело запроса не требуется.
