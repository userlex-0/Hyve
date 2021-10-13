from django import forms
from .models import Post, Comment, UserProfile, MessageModel


class PostForm(forms.ModelForm):
	body = forms.CharField(
		label='',
		widget=forms.Textarea(attrs={
				'rows':'4',
				'placeholder':'Express yourself / Share your ideas / Make an announcement ...'
			}))

	image = forms.ImageField(
		required=False,
		widget=forms.ClearableFileInput(attrs={
			'mutliple': True
			})
	)

	class Meta:
		model = Post
		fields = ['body']


class CommentForm(forms.ModelForm):
	comment = forms.CharField(
		label='',
		widget=forms.Textarea(attrs={
				'rows':'3',
				'placeholder':'What do you think about this post ?'
			}))

	class Meta:
		model = Comment
		fields = ['comment']


class ProfileEditForm(forms.ModelForm):
	bio = forms.CharField(
		label='',
		widget=forms.Textarea(attrs={
				'rows':'3',
				'placeholder':'Write about yourself...'
			}))

	class Meta:
		model = UserProfile
		fields = ['bio']


class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)


class MessageForm(forms.ModelForm):
    body = forms.CharField(label='', max_length=1000)
    image = forms.ImageField(required=False)


    class Meta:
    	model = MessageModel
    	fields = ['body', 'image']


class ShareForm(forms.Form):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
            }))












