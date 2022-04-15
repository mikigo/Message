from django.shortcuts import render

# Create your views here.

# 返回 templates下的 html 文件。
def message_form(request):
    return render(request, "message_form.html")
