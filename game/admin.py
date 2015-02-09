from django.contrib import admin
from game.models import HelpText, Problem, Choice

# admin.site.register(Problem)
# admin.site.register(Choice)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class ProblemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['text']}),
        (None, {'fields': ['actual_result_title','actual_result','actual_result_source']}),
        (None, {'fields': ['tweet','tweet_link']}),
        (None, {'fields': ['background_media_url','actual_result_media_url']}),
        
    ]
    inlines = [ChoiceInline]



admin.site.register(Problem, ProblemAdmin)