from apps.message_form.models import Message
from django.shortcuts import render


# Create your views here.

# 返回 templates下的 html 文件。
def message_form(request):
    # 1、查询
    # （1）queryset 对象，可以进行 for 循环或进行切片
    # queryset 本身并没有进行 sql 操作
    # all_message = Message.objects.all()
    # sliced_query = Message.objects.all()[:1]
    # print(all_message.query)
    # print(sliced_query.query)

    # （2）filter # 会进行数据库的查询
    # all_message = Message.objects.filter(name="mikigo") # all_message.delete()
    # print(all_message.query)
    # for message in all_message:
    #     print(message.name)  # message.delete()

    # （3）get 返回一个对象，数据不存在或者有多条数据，如果数据不存在会抛异常
    # message = Message.objects.get(name="mikigo")
    # print(message.address)

    # 2、进行数据插入操作
    # message = Message()
    # message.name = "huang"
    # message.address = "beijin"
    # message.message = "second"
    # message.email = "huang@uniontech.com"
    # # 如果 key 存在，可以更新数据
    # message.save()
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        messages = request.POST.get("message", "")

        message = Message()
        message.name = name
        message.email = email
        message.address = address
        message.message = messages
        message.save()
        return render(request, "message_form.html", {
            "message": message
        })

    if request.method == "GET":
        var_dict = {}
        all_message = Message.objects.all()
        if all_message:
            message = all_message[0]
            var_dict = {
                "message": message
            }
        return render(request, "message_form.html", var_dict)
