from django.contrib import admin
from .models import TodoModel
# from markdownx.admin import MarkdownxModelAdmin

admin.site.register(TodoModel)
# admin.site.register(Daily, MarkdownxModelAdmin)
