from django import forms

PRODUCT_QUNANTITY_CHOICES = [(i,str(i)) for i in range(1,21)]

class ClaimAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUNANTITY_CHOICES,
        coerce=int
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )