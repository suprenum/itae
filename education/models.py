from django.db import models
from django.urls import reverse


class EduProgram(models.Model):
    title = models.CharField(max_length=60, db_index=True)
    slug = models.SlugField(max_length=60, unique=True)
    edu_code = models.CharField(max_length=7, unique=True)  # 6B06101
    body = models.TextField(db_index=True)
    thumbnail = models.ImageField(null=True, blank=True)
    academic_key = models.CharField(max_length=2)  # 6B, 7M, 8D
    study_period = models.PositiveSmallIntegerField(blank=True, default=4)
    study_price = models.PositiveIntegerField(blank=True)
    purpose = models.TextField(blank=True, db_index=True)

    def __str__(self):
        return self.title

    def get_undergraduate_url(self):
        return reverse('bachelor_program_detail_url', kwargs={'slug': self.slug})

    def get_master_url(self):
        return reverse('master_program_detail_url', kwargs={'slug': self.slug})

    def get_phd_url(self):
        return reverse('phd_program_detail_url', kwargs={'slug': self.slug})
