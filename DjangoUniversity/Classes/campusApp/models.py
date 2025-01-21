from django.db import models


class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_ID = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()

    def __str__(self):
        display_campus = '{0.campus_name}'
        return display_campus.format(self)

    class Meta:
        verbose_name_plural = "University Campus"