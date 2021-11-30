from django import forms
from .models import UbntModelTest

class UbntModelTestForm(forms.ModelForm):
    class Meta:
        model = UbntModelTest
        fields = ('nameubntline', 'nameubnt', 'ipubntone', 'nameubntremote', 'ipubntremote', 'prm_level')