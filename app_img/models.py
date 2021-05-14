from django.db import models


class Images(models.Model):
    title = models.CharField(max_length=200, blank=True)
    url = models.URLField()
    created = models.DateField(auto_now_add=True,
                               db_index=True)


    def __str__(self):
        return self.title
