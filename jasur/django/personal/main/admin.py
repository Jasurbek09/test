from django.contrib import admin
from main.models import *


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    pass
class ServiceAdmin(admin.ModelAdmin):
    pass
class InformationAdmin(admin.ModelAdmin):
    pass
class ProjectTypeAdmin(admin.ModelAdmin):
    pass
class ProjectAdmin(admin.ModelAdmin):
    pass
class CommentAdmin(admin.ModelAdmin):
    pass
class PlanAdmin(admin.ModelAdmin):
    pass
class PartnerAdmin(admin.ModelAdmin):
    pass
class PostCategoryAdmin(admin.ModelAdmin):
    pass
class PostAuthorAdmin(admin.ModelAdmin):
    pass
class PostAdmin(admin.ModelAdmin):
    pass
class NewAdmin(admin.ModelAdmin):
    pass
class QualificationAdmin(admin.ModelAdmin):
    pass
class ExperienceAdmin(admin.ModelAdmin):
    pass
class FAQAdmin(admin.ModelAdmin):
    pass
class PodpischikiAdmin(admin.ModelAdmin):
    pass
class StudentAdmin(admin.ModelAdmin):
    pass
class OthersAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Information, InformationAdmin)
admin.site.register(ProjectType, ProjectTypeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(PostAuthor, PostAuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(Qualification, QualificationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Podpischiki, PodpischikiAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Others, OthersAdmin)

