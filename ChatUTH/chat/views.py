import sys
from django.shortcuts import render, redirect
from .models import *
from .services.crawler import crawl_data_from_url

# from django.contrib import admin

# from django.contrib.auth.decorators import login_required

# Create your views here.
import pdb
import logging
logger = logging.getLogger('chat')

def TrangChu(request):
    return render(request, 'chat/index.html')

URL = [
    {"url": "https://tuyensinh.ut.edu.vn/danh-sach-nganh-chuyen-nganh/", "name": "Danh sách ngành, chuyên ngành"},
    {"url": "https://ut.edu.vn/articles/tong-quan-7.html", "name": "Tổng quan"},
    {"url": "https://ut.edu.vn/articles/su-menh---tam-nhin-13.html", "name": "Sứ mệnh - Tầm nhìn"},
    {"url": "https://ut.edu.vn/articles/chuc-nang---nhiem-vu-14.html", "name": "Chức năng - Nhiệm vụ"},
    {"url": "https://ut.edu.vn/thong-bao-moi/thong-tin-tuyen-sinh-nam-2025-29179.html", "name": "Thông tin tuyển sinh năm 2025"},
    {"url": "https://ut.edu.vn/thong-bao-moi/danh-muc-quy-doi-diem-tieng-anh-theo-muc-danh-gia-chung-chi-ngoai-ngu-29356.html", "name": "Danh mục quy đổi điểm tiếng Anh theo mức đánh giá chứng chỉ ngoại ngữ"},
    {"url": "https://ut.edu.vn/thong-bao-moi/uth-chinh-thuc-mo-cong-dang-ky-cac-phuong-thuc-xet-tuyen-som-dai-hoc-chinh-quy-2024-29093.html", "name": "UTH chính thức mở cổng đăng ký các phương thức xét tuyển sớm đại học chính quy 2024"},
    {"url": "https://tuyensinh.ut.edu.vn/danh-sach-nganh-chuyen-nganh/", "name": "Danh sách ngành, chuyên ngành"},
    {"url": "", "name": ""}
]
def add_URL():
    for item in URL:
        if not item["url"] or CrawledPage.objects.filter(url=item["url"]).exists():
            break
        CrawledPage.objects.create(
            name=item["name"],
            url=item["url"],
            content_json=crawl_data_from_url(item["url"])
        )

def admin(request):
    add_URL()
    return redirect("ChatURLAdmin")


def add_crawled_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        url = request.POST.get("url")

        crawled_data = crawl_data_from_url(url)

        CrawledPage.objects.create(
            name=name,
            url=url,
            content_json=crawled_data
        )
        return redirect("ChatURLAdmin")

    urls = CrawledPage.objects.order_by("-crawled_at")
    # logger.error(f"thong tin cua url {urls}")
    return render(request, 'chat/admin.html', {"urls": urls})


def quanLi(request):
    return render(request, 'chat/dashboard.html')