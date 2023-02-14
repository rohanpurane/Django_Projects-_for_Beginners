from django.db import models

# Create your models here.

class NonDeleted(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)

class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False)

    # Changing the behavier of ModelMaager exe. Student.objects.all() instead of Student.everything.all()
    everything = models.Manager()
    objects = NonDeleted()

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()
    class Meta:
        abstract = True

class XYZ_Shop(SoftDelete):
    name = models.CharField(max_length=70)
    qty = models.PositiveIntegerField()
    price = models.PositiveIntegerField()