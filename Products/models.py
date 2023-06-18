from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class UserDetail(models.Model):
    user_old = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField('Баланс користувача', default=0.0)
    created = models.DateTimeField('Дата створення', auto_now_add=True)

    def change_balance(self, new_balance):
        self.balance = new_balance

    class Meta:
        verbose_name = 'Інфо юзера'
        verbose_name_plural = 'Інфо юзерів'
        ordering = ['id']



class Product(models.Model):
    name = models.CharField('Назва', max_length=100)
    slug = models.SlugField(verbose_name="URL", max_length=100)
    price = models.FloatField('Стоимость товара')
    quantity = models.IntegerField('Кількість', default=1)
    text_about = models.TextField('Опис', max_length=1000)
    sale = models.IntegerField('Знижка', blank=True, null=True, default=0)
    photo = models.ImageField('Фото', upload_to='products/', null=True, default='Screenshot_2.jpg')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категорії')
    psw_and_lg = models.TextField('Дані акаунту')
    is_publish = models.BooleanField('Активно', default=True)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("products:product", kwargs={"product_slug": self.slug})

    class Meta:
        verbose_name = 'Акаунт'
        verbose_name_plural = 'Акаунти'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField('Категорія', max_length=100)
    cat_slug = models.SlugField(verbose_name="URL", max_length=100)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.cat_slug})

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
    
    

