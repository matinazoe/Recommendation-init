from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Project, Review, UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines=(UserProfileInline, )


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('repo', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']
	
class RepoAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('id', 'url', 'owner_id', 'name', 'description', 'language', 'created_at', 'updated_at')
    search_fields = ['name','owner_id', 'language']
	
admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserProfileAdmin)

admin.site.register(Project, RepoAdmin)
admin.site.register(Review, ReviewAdmin)
