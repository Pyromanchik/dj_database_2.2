from django.db import models


class Tag(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=250)
    text = models.TextField('Текст статьи')
    published_at = models.DateTimeField('Дата публикации')
    image = models.ImageField('Изображение', null=True, blank=True)

    # УДАЛИТЬ СТРОКУ: scopes = ... — она не нужна!
    # Django сам создаст доступ через related_name из Scope

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='scopes',  # создаёт article.scopes.all()
        verbose_name='Статья'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name='scopes',
        verbose_name='Тег'
    )
    is_main = models.BooleanField('Основной', default=False)

    class Meta:
        verbose_name = 'Связь статьи и тега'
        verbose_name_plural = 'Связи статьи и тегов'
        unique_together = ['article', 'tag']
        ordering = ['-is_main', 'tag__name']  # основной первый, остальные — по алфавиту