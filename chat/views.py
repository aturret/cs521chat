from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Message


def chat_view(request):
    messages = Message.objects.all()
    context = {'messages': messages}
    return render(request, 'chat/chat.html', context)

def post_message(request):
    if request.method == 'POST':
        user = request.POST['user']
        content = request.POST['content']
        message = Message(user=user, content=content)
        message.save()
    return HttpResponseRedirect(reverse('chat:chat_view'))