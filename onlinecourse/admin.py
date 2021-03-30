from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission, Enrollment

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 3


class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 4


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInLine]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    list_display = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission)
admin.site.register(Enrollment)
