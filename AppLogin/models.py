from DjangoEComm.settings import AUTH_USER_MODEL
from django.db import models

# Custom user model and admin panel
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy

# 
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.





class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("Email filed can't be empty!!")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be a staff!')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser does not have superuser privileges on!')

        return self._create_user(email, password, **extra_fields)





class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    is_staff = models.BooleanField(ugettext_lazy('staff status'), default=False, help_text=ugettext_lazy('Designates whether the user can login to admin panel or not.'))
    is_active = models.BooleanField(ugettext_lazy('active status'), default=True, help_text=ugettext_lazy('Designates whether the user has site access enabled or not. Turn this off instead of deleting the user.'))

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()


    def __str__(self):
        return self.email


    def get_full_name(self):
        return self.email


    def get_short_name(self):
        return self.email



    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=264, blank=True)
    full_name = models.CharField(max_length=264, null=True, verbose_name='Your Full Name')
    address_1 = models.CharField(max_length=264, null=True, verbose_name='Your Full Address')
    city = models.CharField(max_length=40, blank=True)
    zip_code = models.CharField(max_length=20, blank=True, verbose_name='Postal Code')
    country = models.CharField(max_length=40, blank=True)
    phone = models.CharField(max_length=15, null=True, verbose_name='Your Personal Contact Number')
    date_joined = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username + "'s profile"


    def is_fully_setup(self):
        fields = [f.name for f in [self._meta.get_field('full_name'), self._meta.get_field('address_1'), self._meta.get_field('phone')]]

        for field in fields:
            value = getattr(self, field)
            
            if value is None or value == '':
                return False

        return True

    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
