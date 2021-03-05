from django.db import models


class TestName(models.Model):
    name = models.CharField(verbose_name='название теста')

    class Meta:
        verbose_name = 'название теста'
        verbose_name_plural = 'названия тестов'

    def __str__(self):
        return self.name


class EbGroup(models.Model):
    name = models.CharField(max_length=300, verbose_name='наименование')
    test_name = models.ForeignKey(max_length='название теста', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'группа по электробезопасности'
        verbose_name_plural = 'группы по электробезопасности'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    name = models.CharField(max_length=10, verbose_name='номер билета', unique=True)
    eb_group = models.ForeignKey(on_delete=models.CASCADE, verbose_name='группа по электробезопасности')

    class Meta:
        verbose_name = 'номер билета'
        verbose_name_plural = 'номера билетов'

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField(verbose_name='текст вопроса', max_length=600)
    ticket = models.ForeignKey(verbose_name='номер билета', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.text


class Commssion(models.Model):
    name = models.CharField(verbose_name='центральная комиссия')

    class Meta:
        verbose_name = 'центральная комиссия'
        verbose_name_plural = 'центральной комиссии'

    def __str__(self):
        return self.name


class Commssion_member(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    m_name = models.CharField(max_length=50, verbose_name='отчество')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    eb_group = models.ForeignKey(EbGroup, max_length=100, verbose_name='группа электробезопасности',
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Коммиссия'
        verbose_name_plural = 'Коммиссии'

    def __str__(self):
        return self.surname
