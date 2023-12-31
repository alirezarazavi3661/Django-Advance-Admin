from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
    Group,
    Permission,
)
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom User model manager where email is the unique identifiers
    for authenticated instead of username
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create amd save a new user with the
        \given email and password and extra Data
        """
        if not email:
            raise ValueError(_("the email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create amd save a new superuser with the given email
        and password and extra Data
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model for app
    """

    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    groups = models.ManyToManyField(
        Group, blank=True, related_name="custom_users"
    )
    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name="custom_users"
    )
    USERNAME_FIELD = "email"
    # REQUEST_FIELD = []
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.email
