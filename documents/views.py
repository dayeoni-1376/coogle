from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document


def search(request):
    form = DocumentForm()
    documents = Document.objects.all()
    context = {
        'form': form,
        'documents' : documents, 
    }
    return render(request, 'documents/search.html', context)


def result(request):
    query = request.GET.get('q')
    # object_list = City.objects.filter(
    #     Q(name__icontains=query) | Q(state__icontains=query)
    # )

    # 제목만 검색하던 v2 버전 
    # documents = Document.objects.filter(
    #     Q(file__icontains=query)
    # )

    # 내용도 검색할 수 있는 v3 버전 
    documents = Document.search_in_markdown(query)

    context = {
        # 'object_list': object_list,
        'query' : query,
        'documents': documents,
    }
    return render(request, 'documents/result.html', context)


def index(request):
    documents = Document.objects.all()
    context = {
        'documents': documents,
    }
    return render(request, 'documents/index.html', context)

def new(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('documents:index')
    else:
        form = DocumentForm()
    context = {
        'form': form,
    }
    return render(request, 'documents/new.html', context)


def delete(request, pk):
    document = Document.objects.get(pk=pk)
    if request.method == 'POST':
        document.delete()
    return redirect('documents:index')