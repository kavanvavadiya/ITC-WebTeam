from pyexpat import model
from rest_framework import serializers
from .models import Team

# class TeamSerializer(serializers.Serializer):
#     Team_name = serializers.CharField(max_length=50)
#     # Team_id = models.CharField(max_length=10,null=True,default="ITSP220000")
#     # Team_id = models.CharField(max_length=50, default="", editable=False)

#     # Team_id = models.IntegerField(primary_key=True, editable=True)
#     Team_id = serializers.CharField(max_length=10)
#     # Team_id = models.CharField(primary_key=True, editable=True,max_length=10
#     member1 = serializers.CharField(max_length=50)
#     member2 = serializers.CharField(max_length=50,default="")
#     member3 = serializers.CharField(max_length=50,default="NA")
#     member4 = serializers.CharField(max_length=50,default="NA")
#     Team_info = serializers.URLField(max_length=200)

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'