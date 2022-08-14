from django.shortcuts import redirect, render, reverse
from django.views.generic import ListView, View
from django.db.models import Count

from .models import Chat
from .forms import MessageForm


class ChatList(ListView):
    model = Chat
    template_name = 'chat/list.html'
    context_object_name = 'chats'

    def get_queryset(self):
        return Chat.objects.filter(members__in=[self.request.user]).annotate(c=Count('messages')).filter(c=1)


class MessagesView(View):
    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user not in chat.members.all():
                chat = None

        except Chat.DoesNotExist:
            chat = None

        context = {
            'chat': chat,
            'chats': Chat.objects.filter(members__in=[request.user]).annotate(c=Count('messages')).filter(c=1),
            'form': MessageForm()}
        return render(
            request,
            'chat/messages.html',
            context
        )

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('chat_messages', kwargs={'chat_id': chat_id}))


class ChatCreate(View):
    def get(self, request, user_id):
        chats = Chat.objects.filter(members__in=[request.user.id, user_id]).annotate(c=Count('members')).filter(c=2)
        if not chats:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
            chat.save()
        else:
            chat = chats.first()
        return redirect(reverse('chat_messages', kwargs={'chat_id': chat.id}))



