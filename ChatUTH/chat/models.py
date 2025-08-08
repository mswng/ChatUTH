from django.db import models
from django.contrib.auth.models import User


class CrawledPage(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)  # Đường dẫn gốc
    content_json = models.JSONField()   # Dữ liệu đã crawl
    crawled_at = models.DateTimeField(auto_now_add=True)  # Thời điểm crawl

    def __str__(self):
        return self.name

class ConversationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"



class EmbeddingData(models.Model):
    crawled_data = models.ForeignKey(CrawledPage, on_delete=models.CASCADE)
    vector = models.BinaryField()  # hoặc PickleField nếu cần
    created_at = models.DateTimeField(auto_now_add=True)

