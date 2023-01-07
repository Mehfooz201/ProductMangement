from django import forms
from . models import Product, Category, Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name',  'category', 'price', 'description', 'is_published']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)

        
        # widgets = {
        #     'image':forms.FileInput(attrs={'class':'form-control'}),
        #     'name':forms.TextInput(attrs={'class':'form-control'}),
        #     'price':forms.TextInput(attrs={'class':'form-control'}),
        #     'description':forms.TextInput(attrs={'class':'form-control'}),
        #     # 'is_published':forms.TextInput(attrs={'class':'form-control'}),
        # }