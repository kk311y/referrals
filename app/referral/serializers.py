from rest_framework import serializers
from referral.models import Participant, Referral, Program, Staff


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        exclude = []

class ReferralSerializer(serializers.ModelSerializer):
    participant = ParticipantSerializer(many=False)
    class Meta:
        model = Referral
        exclude = ['date_of_referral']

    def create(self, validated_data):
        participant_data = validated_data.pop('participant')
        participant = ParticipantSerializer.create(ParticipantSerializer(),
                                                    validated_data=participant_data)
        referral, created = Referral.objects.update_or_create(
            participant=participant,
            referred_to_program=validated_data.pop('referred_to_program'),
            referring_staff=validated_data.pop('referring_staff')       
            ) 
        return referral


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        exclude = []


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        exclude = []

# class User(model.Model):
#     username = model.CharField('username', max_length=10)

# class Question(model.Model):
#     title = models.CharField('title', max_length=10)

# Possible way to 
# class Answer(model.Model):
#     user = model.ForeignKey(User)
#     question = model.ForeignKey(Question)
#     body = model.TextField('the answer body')
# And you need to serialise Answer, with showing the detail of Question, but not showing the detail of User, then you could define your serialisers like that:

# class QuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         exclude = []

# class AnswerSerializer(serializers.ModelSerializer):
#     question = QuestionSerializer(many=False, read_only=True)
#     class Meta:
#         model = Answer
#         exclude = []




