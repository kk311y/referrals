from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from referral.models import Participant, Referral, Program, Staff
from referral.serializers import ProgramSerializer, StaffSerializer, ReferralSerializer


# Create your views here.

class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'referral/index.html'

    def get(self, request):
        queryset = Referral.objects.all()
        return Response({'referral': queryset})

@api_view(['GET', 'POST'])
def program_list(request):
    if request.method == 'GET':
        programs = Program.objects.all()

        program_serializer = ProgramSerializer(programs, many=True)
        return JsonResponse(program_serializer.data, safe=False)
    
    elif request.method == 'POST':
        program_data = JSONParser().parse(request)
        program_serializer = ProgramSerializer(data=program_data)
        if program_serializer.is_valid():
            program_serializer.save()
            return JsonResponse(program_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(program_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def staff_list(request):
    if request.method == 'GET':
        staff = Staff.objects.all()

        staff_serializer = StaffSerializer(staff, many=True)
        return JsonResponse(staff_serializer.data, safe=False)
    
    elif request.method == 'POST':
        staff_data = JSONParser().parse(request)
        staff_serializer = StaffSerializer(data=staff_data)
        if staff_serializer.is_valid():
            staff_serializer.save()
            return JsonResponse(staff_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(staff_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def program_detail(request, pk):
    try:
        program = Program.objects.get(pk=pk)
    except Program.DoesNotExist:
        return JsonResponse({'message': 'The program does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        program_serializer = ProgramSerializer(program)
        return JsonResponse(program_serializer.data)
    
    elif request.method == 'PUT':
        program_data = JSONParser().parse(request)
        program_serializer = ProgramSerializer(program, data=program_data)
        if program_serializer.is_valid():
            program_serializer.save()
            return JsonResponse(program_serializer.data)
        return JsonResponse(program_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        program.delete()
        return JsonResponse({'message': 'Program was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def referral_list(request):
    if request.method == 'GET':
        referrals = Referral.objects.all()

        referral_serializer = ReferralSerializer(referrals, many=True)
        return JsonResponse(referral_serializer.data, safe=False)
    
    elif request.method == 'POST':
        referral_data = JSONParser().parse(request)
        referral_serializer = ReferralSerializer(data=referral_data)
        if referral_serializer.is_valid():
            referral_serializer.save()
            return JsonResponse(referral_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(referral_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def referral_list_by_program(request, pk):
    referrals = Referral.objects.filter(referred_to_program=pk)

    referral_serializer = ReferralSerializer(referrals, many=True)
    return JsonResponse(referral_serializer.data, safe=False)

# from django.shortcuts import render
# from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework.response import Response
# from rest_framework.views import APIView

# from tutorials.models import Tutorial
# from tutorials.serializers import TutorialSerializer
# from rest_framework.decorators import api_view

# # Create your views here.
# # def index(request):
# #     return render(request, "tutorials/index.html")


# def index(request):
#     print("------------------------- I AM HERE")
#     queryset = Tutorial.objects.all()
#     return render(request, "tutorials/index.html", {'tutorials': queryset})


# class index(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'tutorials/index.html'

#     def get(self, request):
#         queryset = Tutorial.objects.all()
#         return Response({'tutorials': queryset})


# class list_all_tutorials(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'tutorials/tutorial_list.html'

#     def get(self, request):
#         queryset = Tutorial.objects.all()
#         return Response({'tutorials': queryset})


# @api_view(['GET', 'POST', 'DELETE'])
# def tutorial_list(request):
#     if request.method == 'GET':
#         tutorials = Tutorial.objects.all()

#         title = request.GET.get('title', None)
#         if title is not None:
#             tutorials = tutorials.filter(title__icontains=title)

#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
#         # 'safe=False' for objects serialization

#     elif request.method == 'POST':
#         tutorial_data = JSONParser().parse(request)
#         tutorial_serializer = TutorialSerializer(data=tutorial_data)
#         if tutorial_serializer.is_valid():
#             tutorial_serializer.save()
#             return JsonResponse(tutorial_serializer.data,
#                                 status=status.HTTP_201_CREATED)
#         return JsonResponse(tutorial_serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         count = Tutorial.objects.all().delete()
#         return JsonResponse(
#             {
#                 'message':
#                 '{} Tutorials were deleted successfully!'.format(count[0])
#             },
#             status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def tutorial_detail(request, pk):
#     try:
#         tutorial = Tutorial.objects.get(pk=pk)
#     except Tutorial.DoesNotExist:
#         return JsonResponse({'message': 'The tutorial does not exist'},
#                             status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         tutorial_serializer = TutorialSerializer(tutorial)
#         return JsonResponse(tutorial_serializer.data)

#     elif request.method == 'PUT':
#         tutorial_data = JSONParser().parse(request)
#         tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
#         if tutorial_serializer.is_valid():
#             tutorial_serializer.save()
#             return JsonResponse(tutorial_serializer.data)
#         return JsonResponse(tutorial_serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         tutorial.delete()
#         return JsonResponse({'message': 'Tutorial was deleted successfully!'},
#                             status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def tutorial_list_published(request):
#     tutorials = Tutorial.objects.filter(published=True)

#     if request.method == 'GET':
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
