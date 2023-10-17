from django.contrib import admin

from quiz_api.models import Quiz, Category


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('question_id',
                    'category',
                    'value')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
