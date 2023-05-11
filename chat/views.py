from django.shortcuts import render
from .models import Message

def chat_view(request):
    messages = Message.objects.all()
    context = {'messages': messages}
    return render(request, 'chat/chat.html', context)

# Remove the post_message function
