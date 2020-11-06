from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    Permission,
    PermissionsMixin,
)
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Country(models.Model):
    title = models.CharField(max_length=256, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        ordering = ('title',)

class Role(models.Model):
    ar_title = models.CharField(max_length=256, blank=True)
    en_title = models.CharField(max_length=256, blank=True)
    
    #TODO: connect to the mngr model
    # mngr = models.ForeignKey(country, blank=True, null=True, on_delete=models.CASCADE)
    is_visible = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.ar_title or self.en_title
    
    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')
        ordering = ('ar_title', 'en_title')


class UserManager(BaseUserManager):
    def create_user(
            self, username, email, password=None, is_staff=False, is_active=True, **extra_fields
    ):
        """Create a user instance with the given email and password."""
        email = UserManager.normalize_email(email)
        # Google OAuth2 backend send unnecessary username field
        extra_fields.pop("username", None)

        user = self.model(
            username=username,
            email=email,
            is_active=is_active,
            is_staff=is_staff, 
            **extra_fields
        )

        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self.create_user(
            username, 
            email, 
            password, 
            is_staff=True, 
            is_superuser=True, 
            **extra_fields
        )

    def staff(self):
        return self.get_queryset().filter(is_staff=True)

class User(PermissionsMixin, AbstractBaseUser):
    full_name = models.CharField(max_length=256, blank=True)
    username = models.CharField(unique=True, max_length=256, blank=True)
    email = models.EmailField(blank=True, null=True)
    avatar = models.CharField(unique=True, max_length=256, blank=True)
    phone = models.CharField(unique=True, max_length=256, blank=True)
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, blank=True, null=True, on_delete=models.CASCADE)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)    

    REQUIRED_FIELDS = ["email"]
    USERNAME_FIELD = "username"

    objects = UserManager()

    def get_short_name(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    

