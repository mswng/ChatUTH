from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Bảng lưu thông tin chung về trường (ít thay đổi)
class GeneralInfo(models.Model):
    title = models.CharField(max_length=255)  # Tiêu đề
    description = models.TextField()  # Nội dung chi tiết (đã làm sạch)
    url = models.URLField(blank=True, null=True)  # Đường dẫn đến thông báo chính thức
    updated_at = models.DateTimeField(auto_now=True)  # Thời gian chỉnh sửa

    def __str__(self):
        return self.title


# Bảng lưu thông tin tuyển sinh (thay đổi mỗi năm)
class AdmissionInfo(models.Model):
    YEAR_CHOICES = [(str(y), str(y)) for y in range(2000, 2100)]

    year = models.CharField(max_length=4, choices=YEAR_CHOICES)  # Năm ra thông báo

    PROGRAM_CHOICES = [
        ("regular", "Hệ chính quy"),
        ("part_time", "Hệ vừa học vừa làm"),
        ("postgraduate", "Sau đại học"),
        ("international", "Liên kết quốc tế"),
        ("high_quality", "Đào tạo chất lượng cao"),
    ]
    program_type = models.CharField(max_length=50, choices=PROGRAM_CHOICES)  # Loại chương trình

    description = models.TextField()  # Nội dung chi tiết (đã làm sạch)
    url = models.URLField(blank=True, null=True)  # Link đến thông báo chính thức
    created_at = models.DateTimeField(auto_now_add=True)  # Ngày thêm dữ liệu

    def __str__(self):
        return f"{self.year} - {self.get_program_type_display()}"


class DocumentChunk(models.Model):
    SOURCE_CHOICES = [
        ('general_info', 'General Info'),
        ('admission_info', 'Admission Info'),
    ]

    source_table = models.CharField(max_length=50, choices=SOURCE_CHOICES)  # thuộc bảng nào
    source_id = models.IntegerField()  # id của bản ghi gốc
    chunk_text = models.TextField()  # đoạn dữ liệu sau khi chunk
    faiss_vector_id = models.IntegerField()  # mapping tới vector trong FAISS index

    def __str__(self):
        return self.chunk_text[:50]
    
# Bảng metadata của FAISS index
class FaissIndexMeta(models.Model):
    index_name = models.CharField(max_length=255, unique=True)  # tên index
    dimension = models.IntegerField()  # số chiều vector
    metric_type = models.CharField(max_length=50, default="L2")  # ví dụ: L2, cosine
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.index_name

# Bảng lưu lịch sử trò chuyện
class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(
        max_length=10,
        choices=[("user", "Thí sinh"), ("assistant", "Chatbot")]
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role}: {self.message[:50]}"


class CrawledPage(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)  # Đường dẫn gốc
    content_json = models.JSONField()   # Dữ liệu đã crawl
    crawled_at = models.DateTimeField(auto_now_add=True)  # Thời điểm crawl

    def __str__(self):
        return self.name


# Bảng thông tin của người dùng. Có thể là thí sinh hoặc quản lí đăng nhập bằng google
class User(models.Model):
    ROLE_CHOICES = [
        ('candidate', 'Candidate'),
        ('admin', 'Admin'),
    ]

    google_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    avatar = models.URLField(max_length=500, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='candidate')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"