from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .firebase import db

# Create your views here.
@api_view(['POST'])
def create_student(request):
    data = request.data
    doc_ref = db.collection("students").document()
    doc_ref.set(data)
    return Response({"msg": "Student created", "id": doc_ref.id},status=status.HTTP_201_CREATED)

@api_view(['GET'])
def list_student(request):
    students_ref=db.collection('students')
    docs=students_ref.stream()
    students=[]
    for doc in docs:
        student=doc.to_dict()
        student["id"]=doc.id
        students.append(student)

    return Response(students,status=200)

@api_view(['GET'])
def get_student(request,rollno):
    rollno=int(rollno)
    students_ref=db.collection('students')
    docs=students_ref.stream()
    for doc in docs:
        if(doc.get('roll_no'))==rollno:
            student=doc.to_dict()
            student['id']=doc.id
            return Response(student,status=200)
        
    return Response({"msg":"Student not Found"},status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_student(request,rollno):
    rollno=int(rollno)
    student_ref=db.collection('students')
    docs=student_ref.stream()
    for doc in docs:
        if(doc.get('roll_no'))==rollno:
            student=doc.to_dict()
            doc.reference.delete()
            return Response({"msg":f"Student Deleted Successfully.","student":student},status=status.HTTP_200_OK)

    return Response({"msg":"Student Not Found."},status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_student(request,rollno):
    student_ref=db.collection('students')
    docs=student_ref.stream()
    for doc in docs:
        if(int(doc.get('roll_no'))==int(rollno)):
            student=doc.to_dict()
            doc.reference.update(request.data)
            return Response(
                            {"msg":f"Student Updated Successfully with Roll No: {rollno}",
                             "old_data":student,
                             "new_data":request.data},
                             status=status.HTTP_200_OK)
    
    return Response({"msg":"Student Not Found."},status=status.HTTP_404_NOT_FOUND)