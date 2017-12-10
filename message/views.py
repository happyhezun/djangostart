#_*_ coding:utf-8 _*_
from django.shortcuts import render

from models import UserMessage
# Create your views here.
def get_form(request):
    '''
    查询数据
    all_message = UserMessage.objects.filter(name='孙悟空', address='上海')
    for message in all_message:
        print message.name

    添加数据
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        message = request.POST.get('message','')

        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = 'helloworld5'

        user_message.save()

    删除数据
    all_message = UserMessage.objects.filter(name='猪八戒', address='北京')
    for message in all_message:
        print message.delete()
    '''


    return render(request, 'message_form.html')