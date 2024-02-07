from django.contrib import admin
from .models import Number, Tag, Presentation, Submission, Quarter

admin.site.register(Number)
admin.site.register(Tag)
admin.site.register(Presentation)
admin.site.register(Submission)
admin.site.register(Quarter)

