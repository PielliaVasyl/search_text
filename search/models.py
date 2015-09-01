from django.db import models

# Create your models here.
class Search(models.Model):
    searching_text = models.CharField('Search text', max_length=150, default='put search text here')
    email = models.EmailField('E-mail to send response', default='put your email here')
    timestamp = models.TimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.email
