from django.contrib import admin
from .models import TestName
from .models import EbGroup
from .models import Ticket
from .models import Question
from .models import Answers


class TestNameAdmin(admin.ModelAdmin):
    list_display = ['name']


class EbGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'test_name']


class TicketAdmin(admin.ModelAdmin):
    list_display = ['name', 'eb_group', 'answers_true', 'answers_false']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'ticket']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'text', 'truthy']


admin.site.register(TestName, TestNameAdmin)
admin.site.register(EbGroup, EbGroupAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answers, AnswerAdmin)
