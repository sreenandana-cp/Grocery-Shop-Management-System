from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from admin_app.models import CategoryDb, ProductDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

# Create your views here.
def admin_dashboard(request):
    categories = CategoryDb.objects.count()
    products = CategoryDb.objects.count()
    return render(request, "dashboard.html",{
        'categories':categories,
        'products':products,
    })
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def add_categories(request):
    return render(request, "add_categories.html")
def save_category(request):
    if request.method == "POST":
        cn = request.POST.get('cname')
        des = request.POST.get('description')
        img = request.FILES['cimage']
        obj = CategoryDb(CategoryName=cn, Description=des, CategoryImage=img)
        obj.save()
        messages.success(request, "Category added successfully..!")
        return redirect(add_categories)
def view_categories(request):
    categories = CategoryDb.objects.all()
    return render(request, "view_categories.html", {'categories':categories})

def edit_categories(req, cat_id):
    data = CategoryDb.objects.get(id=cat_id)
    return render(req, "edit_categories.html", {'data':data})
def update_category(request, cat_id):
    if request.method=="POST":
        cat = request.POST.get('cname')
        des = request.POST.get('description')
        try:
            img = request.FILES['cimage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=cat_id).CategoryImage
        CategoryDb.objects.filter(id=cat_id).update(CategoryName=cat, Description=des, CategoryImage=file)
        messages.success(request, "Category updated successfully..!")
        return redirect(view_categories)
def delete_category(request,cat_id):
    data = CategoryDb.objects.filter(id=cat_id)
    data.delete()
    messages.error(request, "Category deleted successfully..!")
    return redirect(view_categories)
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
def add_products(request):
    categories = CategoryDb.objects.all()
    return render(request, "add_products.html", {'categories':categories})

def save_product(request):
    if request.method == "POST":
        cn = request.POST.get('cname')
        pn = request.POST.get('pname')
        pr = request.POST.get('price')
        des = request.POST.get('description')
        img = request.FILES['pimage']
        obj = ProductDb(Category_Name=cn,ProductName=pn, Price=pr, Description=des, ProductImage=img)
        obj.save()
        messages.success(request, "Product added successfully..!")
        return redirect(add_products)

def view_products(request):
    products = ProductDb.objects.all()
    return render(request, "view_products.html", {'products':products})

def product_edit(req, pro_id):
    product = ProductDb.objects.get(id=pro_id)
    categories = CategoryDb.objects.all()
    return render(req, "edit_products.html", {'product':product, 'categories':categories})

def UpdateProduct(request, pro_id):
    if request.method=="POST":
        cn = request.POST.get('cname')
        pn = request.POST.get('pname')
        pr = request.POST.get('price')
        des = request.POST.get('description')
        try:
            img = request.FILES['pimage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get(id=pro_id).ProductImage
        ProductDb.objects.filter(id=pro_id).update(Category_Name=cn,ProductName=pn, Price=pr, Description=des, ProductImage=file)
        return redirect(view_products)
def delete_product(request,pro_id):
    data = ProductDb.objects.filter(id=pro_id)
    data.delete()
    return redirect(view_products)
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def admin_loginpage(request):
    return render(request, "admin_login.html")
def admin_login(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pswd = request.POST.get('password')

        if User.objects.filter(username__contains=uname).exists():
            x = authenticate(username=uname, password=pswd)
            if x is not None:
                login(request, x)
                request.session['username'] = uname
                request.session['password'] = pswd
                # Welcome
                return redirect(admin_dashboard)
            else:
                print("Invalid details..!")
                return redirect(admin_loginpage)
        else:
            print("User not found..!")
            return redirect(admin_loginpage)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_loginpage)
