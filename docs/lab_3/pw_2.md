# Практическая работа №3.2

## Практическое задание 1

### Описание задания

Реализовать ендпоинты для добавления и просмотра скиллов методом, описанным в пункте выше.

### Выполнение задания

Для начала создадим serializer для преобразования объектов скиллов между Django-форматом и JSON-форматом:

```python title="warriors_project/warriors_app/serializers.py"
class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"
```

Теперь используя созданный serializer создадим два представления для просмотра и добавления скиллов:

```python title="warriors_project/warriors_app/views.py"
# Просмотр скиллов
class SkillListAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


# Создание скилла
class SkillCreateAPIView(APIView):
    def post(self, request):
       skill = request.data
       serializer = SkillSerializer(data=skill)
       if serializer.is_valid(raise_exception=True):
           skill_saved = serializer.save()
       return Response({"Success": "Skill '{}' created successfully.".format(skill_saved.title)})
```

Добавим данные представления в URLs:

```python title="warriors_project/warriors_app/urls.py"
urlpatterns = [
    # ...
    path('skills/', SkillListAPIView.as_view()),
    path('skills/create/', SkillCreateAPIView.as_view()),
    # ...
]
```

Теперь запустим сервер и проверим, что просмотр и добавление скиллов работают корректно:

![](../img/lab_3/pw/18.png)

![](../img/lab_3/pw/19.png)

![](../img/lab_3/pw/20.png)

![](../img/lab_3/pw/21.png)

![](../img/lab_3/pw/22.png)

Видим, что просмотр и добавление скиллов через API работают корректно.
