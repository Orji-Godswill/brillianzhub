from django.db import models
from django.urls import reverse
from django.conf import settings


class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, null=True, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course:course_detail', kwargs={'slug': self.slug})


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.course.title} - Module {self.order}: {self.title}"


class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.course.title} - Module {self.module.order} - Topic {self.order}: {self.title}"

    def is_completed_by(self, student):
        return student in self.completed_by.all()

    def get_next_topic(self):
        next_topic = Topic.objects.filter(
            module=self.module, order__gt=self.order).order_by('order').first()
        return next_topic

    def get_previous_topic(self):
        previous_topic = Topic.objects.filter(
            module=self.module, order__lt=self.order).order_by('-order').first()
        return previous_topic


class Content(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='contents')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50, choices=[(
        'text', 'Text'), ('video', 'Video'), ('file', 'File')])
    text_content = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    file_upload = models.FileField(
        upload_to='content_files/', blank=True, null=True)

    def __str__(self):
        return f"{self.course.title} - Module {self.topic.module.order} - Topic {self.topic.order} - Content {self.id}"