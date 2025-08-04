from django.db import models
from categories.models import SubCategory
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit
from django.utils.translation import gettext_lazy as _
from slugify import slugify


class Product(models.Model):
    name = models.CharField(_('Название'), max_length=100)
    slug = models.SlugField(_('URL-адрес'), max_length=100, unique=True)
    description = models.CharField(_('Описание'), max_length=255, blank=True, null=True)
    price = models.FloatField(_('Цена'), max_length=100)
    sub_category = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name='product',
        blank=True,
        null=True,
        verbose_name=_('Категория')
    )
    image = models.ImageField(
        _('Изображение'), 
        upload_to='images/products/original/',
        blank=True,
        null=True
        )
    thumbnail = ProcessedImageField(
        upload_to='images/products/thumbnail/',
        processors=[ResizeToFit(220, 220)],
        format='JPEG',
        options={'quality': 100}
    )
    is_active = models.BooleanField(_('Активно'), default=True)


    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
        ordering = ['name']


    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.sub_category:
            self.sub_category = 'uncategorized'

        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug

            counter = 1
            while self.__class__.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = unique_slug

        super().save(*args, **kwargs)

    @property
    def full_path(self):
        if self.sub_category:
            return f'{self.sub_category.full_path} > {self.name}'
