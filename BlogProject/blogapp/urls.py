# ไฟล์สร้างใหม่ไว้ตั้งค่า urlและเรียกใช้งาน urls.py ใน project มาใช้ ร่วมกับ views.py ในapp
from django.urls import path
from blogapp import views

urlpatterns = [
    path('list/', views.blog_list),
    path('<int:id>', views.blog_detail),
    ]
