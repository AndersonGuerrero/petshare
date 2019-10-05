from django.db import models

# Create your models here.


class APP_Photo(models.Model):
    """
        Modelo Para fotos de las mascotas
    """
    nickname = models.CharField(max_length=1000, blank=False, null=False, help_text="nombre de usuario")
    pets_name = models.CharField(max_length=1000, blank=False, null=False, help_text="Nombre de la mascota")
    photo = models.CharField(max_length=1000, blank=False, null=False, help_text="foto de la mascota")
    likes = models.IntegerField(help_text="Votaciones de usuarios anonimos")

    class Meta:
        db_table = 'app_photo'