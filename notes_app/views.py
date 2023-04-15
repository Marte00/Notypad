from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


from .models import Document, Folder

def index(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('editor')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'login.html')



def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('register')
            elif  User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.is_staff = True
                user.save()
                return redirect('login')
    else:
        return render(request, 'register.html')

def editor(request):
    if request.user.is_authenticated:
        docid = int(request.GET.get('docid', 0))
        documents = Document.objects.all().filter(user=request.user)
        folders = Folder.objects.all()

        if request.method == 'GET':
            name = request.GET.get('button')
            if name is not None:
                folder = Folder.objects.get(title=name)
                documents = Document.objects.filter(folder=folder, user=request.user)
                
        if request.method == 'GET':
            name = request.GET.get('recherche')
            if name is not None:
                documents = Document.objects.filter(title=name, user=request.user)
                
        if request.method == 'POST':
            
            docid = int(request.POST.get('docid', 0))
            title = request.POST.get('title')
            content = request.POST.get('content', '')
            foldId = int(request.POST.get('folder', 0))

            if docid > 0:
                document = Document.objects.get(pk=docid)
                document.title = title
                document.content = content
                if foldId > 0:
                    document.folder = Folder.objects.get(pk=foldId)
                else:
                    document.folder = None
                document.save()

                return redirect(f'/editor?docid={docid}')
            else:
                document = Document.objects.create(title=title, content=content, user = request.user)
                return redirect(f'/editor?docid={document.id}')

        if docid > 0:
            document = Document.objects.get(pk=docid)
            folder = document.folder
        else:
            document = ''
            folder = None

        context = {
            'docid': docid,
            'documents': documents,
            'document': document,
            'folders': folders,
            'folder': folder,
        }
        return render(request, 'editor.html', context)
    else:
        return redirect('/login')

def delete_document(request, docid):
    document = Document.objects.get(pk=docid)
    document.delete()
    return redirect(f'/editor?docid=0')