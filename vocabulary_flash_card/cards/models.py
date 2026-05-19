from django.db import models
from django.db.models.functions import Lower
from vocabulary_flash_card.models import Trackable
# Create your models here.

def card_img_path(card_info_obj, img_name):
    return f'card/img/{card_info_obj.card_name}/{img_name}'


class CardsInfo(Trackable):
    card_name = models.CharField(max_length=50, verbose_name='Card name')
    card_category = models.CharField(max_length=50, verbose_name='Card categor')
    card_description = models.TextField()
    card_image = models.ImageField(upload_to=card_img_path)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower('card_name'),
                name="unique_card_name_case_insensitive"
            )
        ]
        
    def __str__(self):
        self.card_name