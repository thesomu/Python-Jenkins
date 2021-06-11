from django import forms  
from bill_logs.models import Export  
class LogForm(forms.ModelForm):  
    class Meta:  
        model = Export  
        fields = "__all__"  