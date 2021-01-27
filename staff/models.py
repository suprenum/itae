from django.db import models
from django.urls import reverse


class Member(models.Model):
    name = models.CharField(max_length=300, db_index=True)
    slug = models.SlugField(max_length=300, unique=True)

    academic_degree = models.CharField(
        max_length=300,
        blank=True,
        db_index=True
    )

    position = models.CharField(max_length=200, blank=True, db_index=True)
    education = models.TextField(blank=True, db_index=True)
    work_experience = models.TextField(blank=True, db_index=True)
    international_experience = models.TextField(blank=True, db_index=True)

    сompetitive_advantages = models.CharField(
        max_length=300,
        blank=True,
        db_index=True
    )

    training = models.TextField(
        blank=True,
        db_index=True
    )  # повышение квалификации

    academic_activity = models.TextField(blank=True, db_index=True)

    training_courses = models.CharField(
        max_length=300,
        blank=True,
        db_index=True
    )

    scientific_publications = models.TextField(blank=True, db_index=True)
    thumbnail = models.ImageField(
        default='member_default.jpg',
        upload_to='staff_images'
    )

    tags = models.ManyToManyField('Tag', blank=True, related_name='members')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('member_detail_url', kwargs={'slug': self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_staff_detail_url', kwargs={'slug': self.slug})
