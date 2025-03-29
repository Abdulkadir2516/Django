from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)  # Görev başlığı
    description = models.TextField(blank=True)  # Görev açıklaması
    created_at = models.DateTimeField(auto_now_add=True)  # Görev oluşturulma tarihi
    completed = models.BooleanField(default=False)  # Görev tamamlama durumu

    def __str__(self):
        return self.title
