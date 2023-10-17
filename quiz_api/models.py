from django.db import models


class CreatedAt(models.Model):
    """
    Абстрактная модель для наследования с датой создания.
    """

    created_at = models.DateTimeField(
        verbose_name='Дата создания'
    )

    class Meta:
        abstract = True


class Quiz(CreatedAt):
    """
    Модель квиза, которая включает в себя поля
    уникального номера вопроса от сервера вопросов,
    текст вопроса, категорию, ответ и стоимость подсказки.
    """

    question_id = models.PositiveIntegerField(verbose_name='Номер вопроса', db_index=True, unique=True)
    text = models.TextField(verbose_name='Текст вопроса')
    category = models.ForeignKey(to='Category', verbose_name='Категория', on_delete=models.CASCADE)
    answer = models.TextField(verbose_name='Ответ')
    value = models.PositiveIntegerField(verbose_name='Стоимость подсказки', null=True)

    def __str__(self) -> str:
        return f'[{self.category.id}] {self.text[:40]}...'


class Category(CreatedAt):
    """
    Модель категории, которая включает в себя только наименование.
    """
    title = models.CharField(verbose_name='Наименование', max_length=100)

    def __str__(self) -> str:
        return self.title
