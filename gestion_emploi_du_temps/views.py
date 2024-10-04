from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Departement, Metier
from .serializers import DepartementSerializer, MetierSerializer

# CRUD pour les Départements

@api_view(['GET', 'POST'])
def departement_list(request):
    if request.method == 'GET':
        departements = Departement.objects.all()
        serializer = DepartementSerializer(departements, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepartementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Département créé avec succès!',
                'departement': serializer.data
            }, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def departement_detail(request, pk):
    try:
        departement = Departement.objects.get(pk=pk)
    except Departement.DoesNotExist:
        return Response({'error': 'Département non trouvé'}, status=404)

    if request.method == 'GET':
        serializer = DepartementSerializer(departement)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DepartementSerializer(departement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Département mis à jour avec succès!',
                'departement': serializer.data
            })
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        departement.delete()
        return Response({'message': 'Département supprimé avec succès!'}, status=200)


# CRUD pour les Métiers

@api_view(['GET', 'POST'])
def metier_list(request):
    if request.method == 'GET':
        metiers = Metier.objects.all()
        serializer = MetierSerializer(metiers, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MetierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Métier créé avec succès!', 'metier': serializer.data}, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def metier_detail(request, pk):
    try:
        metier = Metier.objects.get(pk=pk)
    except Metier.DoesNotExist:
        return Response({'error': 'Métier non trouvé'}, status=404)

    if request.method == 'GET':
        serializer = MetierSerializer(metier)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MetierSerializer(metier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Métier mis à jour avec succès!', 'metier': serializer.data})
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        metier.delete()
        return Response({'message': 'Métier supprimé avec succès!'}, status=204)