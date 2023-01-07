import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Product, Category, Comment
from .forms import ProductForm, CommentForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts/login')
def showAllProduct(request):
    
    category = request.GET.get('category')
    if category == None:
        products = Product.objects.filter(is_published=True)
    else:
        products = Product.objects.filter(category__name=category)

    #Pagination
    page_num = request.GET.get('page')
    paginator = Paginator(products, 3)

    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    categories = Category.objects.all()

    context = {
        'products':products,
        'categories' : categories
        }
    return render(request, 'showProducts.html', context)



@login_required(login_url='accounts/login')
def productDetails(request, pk):
    eachProduct = Product.objects.get(id=pk)
    form = CommentForm(instance=eachProduct)
    num_comments = Comment.objects.filter(product=eachProduct).count()

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=eachProduct)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            c = Comment(product=eachProduct, commentor_name=name, comment_body=body, date_added=datetime.datetime.now())
            c.save()
            return redirect('showProducts')
        else:
            print('Form is invalid')
    else:
        form = CommentForm()

    context = {
        'eachProduct':eachProduct,
        'form':form,
        'num_comments' : num_comments
        }
    return render(request, 'productDetails.html', context)
 



@login_required(login_url='accounts/login')
def addProducts(request):
    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showProducts')
    else:
        form = ProductForm()
    context = {
        'form':form
        }
    return render(request, 'addProduct.html', context)


#Update Products
@login_required(login_url='accounts/login')
def updateProducts(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showProducts')
    context = {
        'form':form
        }
    return render(request, 'updateProduct.html', context)


#Delete Products
@login_required(login_url='accounts/login')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('showProducts')
    # return render(request, 'updateProduct.html')


def searchBar(request):
    if request.method=='GET':
        query = request.GET.get('search_query')
        if query:
            products = Product.objects.filter(name__icontains=query)       
        
    return render(request, 'searchBar.html', {'products':products, 'query':query})