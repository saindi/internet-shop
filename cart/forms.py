from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        label=False,
        widget=forms.NumberInput(
            attrs={"class": "mr-2 quantity",
                   "value": "1"}
        )
    )

    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)