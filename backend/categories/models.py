from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class MainCategory(models.Model):
    name = models.CharField(_('Название'), max_length=100)
    slug = models.SlugField(_('URL-адрес'), max_length=100, unique=True)
    is_active = models.BooleanField(_('Активна'), default=True)


    class Meta:
        verbose_name = _('Основная категория')
        verbose_name_plural = _('Основные категории')
        ordering = ['name']


    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)


class SubCategory(models.Model):
    name = models.CharField(_('Название'), max_length=100)
    slug = models.SlugField(_('URL-адрес'), max_length=100, unique=True)
    parent = models.ForeignKey(
        MainCategory,
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True,
        verbose_name=_('Родительская категория'),
    )
    is_active = models.BooleanField(_('Активна'), default=True)


    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
        ordering = ['name']


    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    @property
    def is_parent(self):
        return not bool(self.parent)

    @property
    def full_path(self):
        if self.parent:
            return f"{self.parent.full_path} > {self.name}"
        
        return self.name
