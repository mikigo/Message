from django.db import models


# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名", primary_key=True)
    email = models.EmailField(verbose_name="邮箱")
    address = models.CharField(max_length=100, verbose_name="联系地址")
    message = models.CharField(max_length=1000, verbose_name="留言信息")

    class Meta:

        verbose_name = "留言信息"
        verbose_name_plural = verbose_name
        # 定义表的名称， 如果不定义默认生成表名。
        db_table = "message"
