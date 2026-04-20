from django import forms

class TanqueForm(forms.Form):
    radio_tanque = forms.FloatField(
        label='Radio del Tanque (m)',
        min_value=0.1,
        initial=1.0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 1.0', 'step': '0.01'})
    )
    radio_orificio = forms.FloatField(
        label='Radio del Orificio (m)',
        min_value=0.01,
        initial=0.05,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 0.05', 'step': '0.001'})
    )
    altura_inicial = forms.FloatField(
        label='Altura Inicial (m)',
        min_value=0.1,
        initial=2.0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 2.0', 'step': '0.1'})
    )