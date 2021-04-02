from django.db import models


class TestName(models.Model):
    name = models.CharField(verbose_name='название теста', max_length=500)

    class Meta:
        verbose_name = 'название теста'
        verbose_name_plural = 'названия тестов'

    def __str__(self):
        return self.name


class EbGroup(models.Model):
    name = models.CharField(max_length=300, verbose_name='наименование')
    test_name = models.ForeignKey(TestName, verbose_name='название теста', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'группа по электробезопасности'
        verbose_name_plural = 'группы по электробезопасности'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    name = models.CharField(max_length=10, verbose_name='номер билета', unique=True)
    eb_group = models.ForeignKey(EbGroup, on_delete=models.CASCADE, verbose_name='группа по электробезопасности')
    answers_true = models.DecimalField(max_digits=1, decimal_places=0, verbose_name='правильный ответ', default=0)
    answers_false = models.DecimalField(max_digits=1, decimal_places=0, verbose_name='неправильный ответ', default=0)

    class Meta:
        verbose_name = 'номер билета'
        verbose_name_plural = 'номера билетов'

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField(verbose_name='текст вопроса', max_length=600)
    ticket = models.ForeignKey(Ticket, verbose_name='номер билета', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.text


class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='вопрос')
    text = models.TextField(verbose_name='текст ответа', unique=True)
    truthy = models.BooleanField(verbose_name='правильность ответа')

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'

    def __str__(self):
        return self.text
