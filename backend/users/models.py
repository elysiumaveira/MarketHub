from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from products.models import Product


class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None, **extrafields):
        if not email:
            raise ValueError('Необходимо ввести Email!')
        
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extrafields)
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, email, phone_number, password=None, **extrafields):
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)

        return self.create_user(email, phone_number, password, **extrafields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Электронная почта'), unique=True)
    phone_number = models.CharField(_('Номер телефона'), unique=True, max_length=20)
    avatar = models.ImageField(_('Аватар'), upload_to='avatars/', blank=True, null=True)
    first_name = models.CharField(_('Имя пользователя'), max_length=128)
    last_name = models.CharField(_('Фамилия пользователя'), max_length=128)
    favorite_products = models.ManyToManyField(
        'products.Product', 
        verbose_name=_('Избранные товары'), 
        blank=True,
        )
    is_active = models.BooleanField(_('Активен'), default=True)
    is_staff = models.BooleanField(_('Сотрудник'), default=False)
    date_joined = models.DateField(_('Дата регистрации'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']


    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
