from django.contrib import admin
from courses.models import Course, Achievment, Major, User, Group


class CourseAdmin(admin.ModelAdmin):
    pass


class AchievementAdmin(admin.ModelAdmin):
    pass

class MajorAdmin(admin.ModelAdmin):
    pass


class UserAdmin(admin.ModelAdmin):
    pass

class GroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Achievment, AchievementAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)