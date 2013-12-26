from django import forms

class PlaylistForm(forms.Form):
    track_slug = forms.CharField(widget=forms.HiddenInput())
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(PlaylistForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError('Cookies must be enabled')
            return self.cleaned_data
