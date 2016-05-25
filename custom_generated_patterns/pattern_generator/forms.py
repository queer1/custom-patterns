from django import forms

from .models import measurements
from .models import pattern

class measurements_form(forms.ModelForm):

    class Meta:
        model = measurements
        fields = ('neck_to_bust','shoulders', 'bust', 'underbust', 'underarm_to_waist', 'underbust_to_waist', 'waist', 'waist_to_hip', 'hip', 'hip_to_knee', 'hip_to_ankle')
class pattern_form(forms.ModelForm):

    class Meta:
        model = pattern
        fields = ('full_length','center_front_length', 'shoulder_tip', 'shoulder_length', 'across_shoulder', 'armhole_depth', 'bust_depth', 'bust_span', 'bust_arc', 'shoulder_slope', 'side_seam_length', 'waist_arc', 'dart_placement', 'short')