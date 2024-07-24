#ไฟล์สร้างใหม่ เรียกใช้ serializers เพียงกำหนดข้อมูล เป็น json

from blogapp.models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model =Blog
        fields = "__all__"  #["title","dct","active"]