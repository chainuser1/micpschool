from django.contrib import admin
from .models import ICategory, Question, Answer, QuestionResponse, CarouselIndex
from django.contrib.auth.models import User
import csv
import datetime
from django.http import HttpResponse
from .forms import CarouselIndexForm
import pickle
from django.utils.html import mark_safe

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if
             not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([field.verbose_name for field in fields] + ["Answers"])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d%m%Y')
            if isinstance(value, User) and value.first_name:
                value = value.first_name + " " + value.last_name
            data_row.append(value)
        if obj.answers:
            for answer in obj.answers.all():
                correctness = "Correct" if answer.correct else "Incorrect"
                # data_row.append("{} ({})".format(choice.choice_text, correctness))
                data_row.append(answer.answer_text)
                data_row.append(correctness)

        writer.writerow(data_row)
    return response
#this will appear on the actions to do
export_to_csv.short_description = 'Export to CSV'

class AnswerInline(admin.TabularInline):
    model = Answer


        

class QuestionAdmin(admin.ModelAdmin):
    # question_text = forms.CharField(widget=forms.Textarea())
    # form=QuestionForm
    inlines = [AnswerInline]
    readonly_fields = ['slug']
    list_display = ['__str__', 'icategory', 'published', 'save_for_exam']
    list_editable = ['published', 'save_for_exam']
    search_fields = ['question_text']
    list_filter = ['icategory', 'published', 'save_for_exam']
    actions = [export_to_csv]    

class ICategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_display = ['__str__', 'published']
    list_editable = ['published']
    search_fields = ['name']

class CarouselIndexAdmin(admin.ModelAdmin):
   
    def get_form(self, request, obj=None, **kwargs):
        form = super(CarouselIndexAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        return form

    readonly_fields = ["headshot_image"]

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.headshot.url,
            width=obj.headshot.width,
            height=obj.headshot.height,
            )
        )

admin.site.register(Question, QuestionAdmin)
admin.site.register(ICategory, ICategoryAdmin)
admin.site.register(CarouselIndex, CarouselIndexAdmin)
