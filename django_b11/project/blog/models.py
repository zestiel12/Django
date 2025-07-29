from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(
        verbose_name="Заголовок",
        max_length=100,
    )    
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(
        verbose_name="Тег",
        max_length=100,
    )    
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Тег"
    
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(
        verbose_name="Заголовок",
        max_length=100,
    )
    cat = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="new",
        verbose_name="Категория",
        blank=True,
        null=True
    )
    tag = models.ManyToManyField(
        Tag,
        related_name="new",
        verbose_name="tags",
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="Описание",
        blank = True,
        null = True
    )
    date = models.DateTimeField(
        verbose_name='дата добавления',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name='дата изменения',
        auto_now_add=True,
    )
    author = models.CharField(
        max_length=50,
        verbose_name='автор',
        null=True,
        blank=True
    )
    views = models.PositiveIntegerField(
        verbose_name='просмотры',
        default=0,
    )
    is_published = models.BooleanField(
        verbose_name='публичность',
        default=True,
    )
    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
    
    def __str__(self):
        return self.title
    
    @property
    def image(self):
        return self.images.first()

    
class NewsImage(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Новости"
    )
    image = models.ImageField(
        "Фото",
        upload_to="news/photos",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Фото новостей'
        verbose_name_plural = 'Фото новостей'
    
    def __str__(self):
        return f"Фото-{self.news.title}"

