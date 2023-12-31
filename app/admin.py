from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from app import app, db
from app.models import Category, Product
from flask_login import logout_user, current_user
from flask import redirect
admin = Admin(app=app, name="Quan ly ban hang", template_mode="bootstrap4")
from app.models import UserRoleEnum


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class MyProductView(AuthenticatedAdmin):
    column_display_pk = True
    column_list = ['id', 'name', 'price', 'category']
    column_searchable_list = ['name']
    column_filters =['name', 'price']
    can_export = True
    can_view_details = True



class MyCategoryVIew(AuthenticatedAdmin):
    column_list = ['name', 'products']


class MyStatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


class MyLogoutView(AuthenticatedUser):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


admin.add_view(MyCategoryVIew(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyStatsView(name='Thong ke bao cao'))
admin.add_view(MyLogoutView(name='Đăng xuất'))
