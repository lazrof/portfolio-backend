from rest_framework import serializers

from apps.translatable_content.models import Post, Content, Tag, Media

'''
class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days

'''
class PostSerializer(serializers.ModelSerializer):

    contents   = serializers.SerializerMethodField()
	
    class Meta:
        model = Post
        fields =  ('title', 'slug', 'contents', 'created_at', 'updated')

    def get_contents(self, obj):
        return ContentSerializer(obj.contents.all(), many=True).data


class MediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Media
		fields =  ('file_name', 'url', 'file_type')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class ContentSerializer(serializers.ModelSerializer):

    media   = serializers.SerializerMethodField()
    tags    = serializers.SerializerMethodField()


    class Meta:
        model = Content
        fields = (
            'media', 
            'tags', 
            'key', 
            'value',
            'created_at',
            'updated',
            'language_code'
        )

    #def get_post(self, obj):
	#	return PostSerializer(obj.post)

    def get_tags(self, obj):
        return TagSerializer(obj.tags, many=True).data

    def get_media(self, obj):
        return MediaSerializer(obj.media, many=True).data