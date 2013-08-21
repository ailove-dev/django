from django.db import models


class Orderable(models.Model):
    position = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        model = self.__class__

        if self.position is None:
            try:
                last = model.objects.order_by('-position')[0]
                self.position = last.position + 1
            except IndexError:
                self.position = 0

        return super(Orderable, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ('position',)
