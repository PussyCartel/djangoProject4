from django.db import models

# Create your models here.

class VarOption(models.Model):
    Var_opt = models.CharField(max_length=12)

    def __str__(self):
        return f"Переменная - {self.Var_opt}"


class VarSlug(models.Model):
    slug = models.SlugField(unique=True, verbose_name='Уникальный идентификатор для цитирования')

    def __str__(self):
        return f"Идентификатор - {self.slug}"


class Var(models.Model):
    VarName = models.CharField(max_length=20, verbose_name='Имя переменной')
    VarMean = models.ForeignKey(VarOption, on_delete=models.CASCADE, default=1, verbose_name='Её значения')
    MeaningToUser = models.CharField(max_length=255, verbose_name='Отображение переменной для пользователя', null=True)
    MeaningToAttestation = models.CharField(max_length=255, verbose_name='Отображение переменной для авторизированного пользователя', null=True)
    QuoteMean = models.ForeignKey(VarSlug, verbose_name='Уникальный идентификатор для цитирования', on_delete=models.CASCADE, null=True)
    Start_date = models.DateField(auto_now=True)


class Attestation(models.Model):
    date = models.DateTimeField(auto_now=True)
    variables = models.ForeignKey(Var, on_delete=models.CASCADE, verbose_name='переменные', null=True)
    decode = models.CharField(max_length=255, verbose_name='Расшифровка параметра', null=True)
    variable_meaning = models.CharField(max_length=255, verbose_name='Значение переменной', null=True)
    source = models.CharField(max_length=255, verbose_name='Источник', null=True)
    articel = models.CharField(max_length=255, verbose_name='Анкета', null=True)
    mark = models.BooleanField(default=False)