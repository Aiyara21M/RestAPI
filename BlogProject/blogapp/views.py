from blogapp.models import Blog
from blogapp.Serealizer import BlogSerializer
from rest_framework import viewsets



class BlogViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class=BlogSerializer


'''
class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer



class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
'''



'''
class BlogList(APIView):
    def get(self,request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BlogDetail(APIView):
    def get(self,request,id):
        try:
            blog = Blog.objects.get(pk=id)
            serializer=BlogSerializer(blog)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            return Response("404",status=status.HTTP_404_NOT_FOUND)

    def put(self,request,id):
        blog = Blog.objects.get(pk=id)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        blog = Blog.objects.get(pk=id)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''




'''
@api_view(['GET','POST'])
def blog_list(request):
    if request.method == "GET":
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       
@api_view(['GET','PUT','DELETE'])    
def blog_detail(request, id):
    try:
        blog = Blog.objects.get(pk=id)
    except  Blog.DoesNotExist:
        return Response("404",status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer=BlogSerializer(blog)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''       
    
    
