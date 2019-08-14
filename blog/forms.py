from django import forms
from tinymce import TinyMCE
from .models import Post


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ('author', 'title', 'timestamp', 'category', 'thumbnail', 'overview', 'content' 'post_tags', 'featured', 'previous_post', 'next_post')