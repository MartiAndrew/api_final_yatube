from posts.models import Comment, Group, Post, Follow, User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = '__all__'

        validators = {
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        }

    def validate(self, data):
        if data['user'] == data['followin']:
            raise serializers.ValidationError(
                'Подписчик не может подписаться на самого себя!'
            )
        return data
