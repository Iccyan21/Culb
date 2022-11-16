from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from django.conf import settings

def get_favorite_image_path(instance,filename):
    return 'images/fav/{0}/{1}'.format(instance.submitter.id,filename)


class Favorite(models.Model):
    """ファボ"""
    
    class Meta:
        db_table = 'favorite'
    
    title = models.CharField(verbose_name='タイトル',max_length=254)
    comment = models.TextField(verbose_name='コメント',blank=True, null=True)
    photo = models.ImageField(verbose_name='フォト',blank=True,null=True,upload_to = get_favorite_image_path)
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL, models.PROTECT,verbose_name='投稿者')
    created_at = models.DateTimeField('作成日時',default=timezone.now)

# Create your models here.
