__author__ = 'siddharthshukla'
from django.forms import ModelForm
from apps.quests.models import Quest, Response, in_range, to_rad
from apps.accounts.models import Account

class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ["user", "quest", "lat", "long"]

    def clean(self):
        cleaned_data = super(ResponseForm, self).clean()
        print(cleaned_data)
        import pdb; pdb.set_trace()


