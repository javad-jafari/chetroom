from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .usermanagers import UserManager




class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=128, verbose_name='نام کاربری', unique=True)
    password = models.CharField( max_length=128, verbose_name='رمز عبور')
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='آخرین لاگین')
    is_staff = models.BooleanField(
        verbose_name='ابر کاربر',
        default=False,
        help_text='Designates whether the user can log into this admin site.'
    )
    is_active = models.BooleanField(
        verbose_name='کاربر فعال',
        default=True,
        help_text=
            'Designates whether this user should be treated as active. '
    )
    date_joined = models.DateTimeField(verbose_name='تاریخ پیوستن', default=timezone.now)
    objects = UserManager()
    USERNAME_FIELD = 'username'


class Saller(models.Model):

    name = models.CharField(max_length=128, verbose_name='نام فروشنده')
    user = models.OneToOneField(CustomUser, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name