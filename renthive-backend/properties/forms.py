from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'property_type', 'location', 'amenities', 'is_active']
        widgets = {
            'location': forms.Textarea(attrs={'rows': 2, 'placeholder': 'e.g. {"county": "Nairobi", "coordinates": {"lat": -1.2921, "lng": 36.8219}}'}),
            'amenities': forms.Textarea(attrs={'rows': 2, 'placeholder': 'e.g. ["WiFi", "Parking"]'}),
        }
