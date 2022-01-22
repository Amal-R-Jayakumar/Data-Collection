from django import forms
from django.conf import settings
from .models import Student
from django.core.files.images import get_image_dimensions

class CreateStudent(forms.ModelForm):
    name = forms.CharField(label="Name", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    phone = forms.CharField(label="Contact Number", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    course = forms.CharField(label="Course", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Course'}))
    year_joined = forms.IntegerField(label='Year joined', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Year Joined for Course'}))
    dob = forms.DateField(label='Date of Birth', input_formats=settings.DATE_INPUT_FORMATS, widget=forms.DateInput(
        attrs={'class': 'form-control', 'placeholder': 'DoB'}))
    gender = forms.CharField(label="Gender", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Gender'}))
    address = forms.CharField(label="Gender", widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Address', 'rows': 4}))
    photo = forms.ImageField(label="Student Photo", widget=forms.FileInput(
        attrs={'class': 'form-control', 'placeholder': 'Upload the Student\'s Photo*'}))

    class Meta:
        model = Student
        fields = 'name email phone course year_joined dob gender address photo'.split()

    def clean_profile_pic(self):
        profile_pic = self.cleaned_data['profile_pic']

        try:
            w, h = get_image_dimensions(profile_pic)

            # validate dimensions
            # max_width = max_height = 768
            # if w > max_width or h > max_height:
            #     raise forms.ValidationError(
            #         f'Please use an image that is {max_width} x {max_height} pixels or smaller.')

            # validate content type
            main, sub = profile_pic.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                                            'GIF or PNG image.')

            # #validate file size
            # if len(profile_pic) > (20 * 1024):
            #     raise forms.ValidationError(
            #         u'profile_pic file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new profile_pic
            """
            pass

        return profile_pic
