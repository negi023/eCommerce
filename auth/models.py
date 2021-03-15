from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.db.models import UniqueConstraint
# from django.contrib.auth.backends import BaseBackend
from . models.static_vars import USER_TYPE


class AbstractTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MyUserManager(BaseUserManager):
    # using=self.db means to save the obj into default database.
    # If you have multiple db then you can accordingly
    def create_user(self, email, password):
        if email:
            email = BaseUserManager.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        admin = self.model(email=email)
        admin.set_password(password)
        admin.is_active = True
        admin.is_staff = True
        admin.is_superuser = True
        admin.save(using=self.db)
        return admin
               
        
class MyUser(AbstractBaseUser, AbstractTime):
    """Basic field required to create a user, and authenticate it."""
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_type = models.CharField(choices=USER_TYPE, max_length=5)