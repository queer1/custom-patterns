from django import forms

from .models import measurements

class measurements_form(forms.ModelForm):

    class Meta:
        model = measurements
        fields = ('neck_to_bust','shoulders', 'bust', 'underbust', 'underarm_to_waist', 'underbust_to_waist', 'waist', 'waist_to_hip', 'hip', 'hip_to_knee', 'hip_to_ankle')