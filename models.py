from django.db import models


class EbGroup(models.Model):
    name = models.CharField(max_length=300, verbose_name='наименование')

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
