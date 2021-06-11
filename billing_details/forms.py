from django import forms  
from billing_details.models import billing
class billing_Form(forms.ModelForm):  
    class Meta:  
        model = billing  
        fields = "__all__"  