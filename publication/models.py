from django.db import models
from datetime import datetime


class Publication(models.Model):
    pub_date = models.DateTimeField(default=datetime.now(), blank=False)
    place = models.ForeignKey("Place", related_name='place')
    type_play = models.ForeignKey("Type_Play", related_name='play')
    cnt_player = models.DecimalField(max_digits=2)
    cnt_min_player = models.DecimalField(max_digits=2)
    description = models.TextField(max_length=300, default='Insira aqui informações sobre o jogo.')
    pub_max_date = models.DecimalField(default=datetime.now(), blank=False)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'publication'
        verbose_name_plural = 'publications'

    def __str__(self):
        return self.pub_date + '-' + self.place
