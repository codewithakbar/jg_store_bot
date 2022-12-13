from django.db import models


class Profile(models.Model):

    external_id = models.PositiveIntegerField(
        verbose_name='Foydalanuvchi "ID"si.'
    )

    name = models.CharField(
        max_length=65,
        verbose_name='Foydalanuvchi ISMI'
    )

    def __str__(self):
        return f"#{self.external_id} {self.name}"

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profillar'


class Message(models.Model):

    profile = models.ForeignKey(
        to='ugc.Profile',
        verbose_name='Profil',
        on_delete=models.PROTECT,
    )

    text = models.TextField(
        verbose_name='Matn'
    )

    created_at = models.DateTimeField(
        verbose_name='Olinadigan Vaqt',
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.profile}dan {self.pk} xabarnoma"

    
    class Meta:
        verbose_name = 'Xabar'
        verbose_name_plural = 'Xabarlar'