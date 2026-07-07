from django.db import models


class Note(models.Model):
    heading = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок статьи",
        unique=True,
    )
    content = models.TextField(
        verbose_name="Содержимое статьи",
        help_text="Введите статью",
    )
    preview = models.ImageField(
        upload_to="preview/",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите превью статьи",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")
    views = models.IntegerField(verbose_name="Количество просмотров", default=0)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["updated_at", "heading"]

    def __str__(self):
        return self.heading
