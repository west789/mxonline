__author__ = 'python'
__date__ = '2017/11/13 8:49'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner, UserProfile


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    model_icon = 'fa fa-address-book-o'

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    model_icon = 'fa fa-address-book-o'

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "学习课程管理系统"
    site_footer = "版权所有 吴俊亚"
    menu_style = "accordion"

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)