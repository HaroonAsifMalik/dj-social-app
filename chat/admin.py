from django.contrib import admin
from .models import Conversation , Message

# Register your models here.
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display= ('get_participant_usernames',)


    def get_participant_usernames(self, obj):
        return ", ".join([participant.username for participant in obj.participants.all()])
    get_participant_usernames.short_description = "Participants"


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display=['id','sender','conversation','text','timestamp']