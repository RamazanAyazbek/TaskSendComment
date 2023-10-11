from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title=models.CharField("Заголовок", max_length=250)
    url=models.SlugField(max_length=160, unique=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.url})
    def get_review(self):
        return self.review_set.filter(parent__isnull=True)


class Review(models.Model):
    email=models.EmailField()
    name=models.CharField("Имя", max_length=255)
    text=models.TextField("Сообщение", max_length=500, blank=True, null=True)
    parent=models.ForeignKey('self', verbose_name="Родитель",  on_delete=models.SET_NULL, blank=True, null=True)
    post=models.ForeignKey(Post, verbose_name="пост", on_delete=models.CASCADE)
    photo = models.ImageField("Фото", upload_to='review_photos/', blank=True, null=True)  
    modified_by_admin = models.BooleanField("Изменено администратором", default=False) 
    def __str__(self):
        return f'{self.name} - {self.post}'
    
    class Meta:
        verbose_name="Отзыв"
        verbose_name_plural="Отзывы"






