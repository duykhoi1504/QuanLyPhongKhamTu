from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from app import app, db
from app.models import Category, Product

admin = Admin(app=app, name="Quan ly ban hang", template_mode="bootstrap4")


class MyProductView(ModelView):
    column_display_pk = True
    column_list = ['id', 'name', 'price', 'category']
    column_searchable_list = ['name']
    column_filters =['name', 'price']
    can_export = True
    can_view_details = True


class MyCategoryVIew(ModelView):
    column_list = ['name', 'products']


class MyStatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


admin.add_view(MyCategoryVIew(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyStatsView(name='Thong ke bao cao'))
