from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from app1.models import Hamkari, Farakhan


# Create your views here.
def index(request):
    if request.method == 'POST':
        print('vared post shod')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('vared user shod')
            login(request, user)
            return redirect('appfront:farakhan_detail_sherkat',1)
        else:
            return redirect('appfront:login')
    else:
        print('vared login shod')
        return render(request, 'index.html')


def gallery(request):
    return render(request, 'gallery.html')


def folder_gallery(request):
    return render(request, 'folder_gallery.html')


def register(request):
    return render(request, 'register.html')


def cooperation(request):
    id_profile = request.user.profile.id

    context = {
        'id_profile' : id_profile,
    }
    return render(request, 'cooperation.html', context=context)

def cooperation_code(request):
    return render(request, 'cooperation_code.html')


def create_farakhan(request):
    return render(request, 'create_farakhan.html')


def farakhan_detail(request, id=None):
    if request.method == 'POST':
        print('vared post shod')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('vared user shod')
            login(request, user)
            return redirect('appfront:farakhan_detail_sherkat', 1)
        else:
            return redirect('appfront:login')
    else:
        print('vared login shod')
        return render(request, 'farakhan_detail.html')


def farakhan_detail_sherkat(request, id=None):
    return render(request, 'farakhan_detail_sherkat.html')


def success(request):
    return render(request, 'success.html')


def profile(request):
    if request.user.is_authenticated:

        username = request.user.username
        first_name = request.user.profile.first_name
        last_name = request.user.profile.last_name
        father_name = request.user.profile.father_name
        date_birth = request.user.profile.date_birth
        national_code = request.user.profile.national_code
        email = request.user.profile.email

        hamkari_user = Hamkari.objects.filter(profile__user=request.user)

        hamkari_type = ''
        farakhan_hamkari_title = []
        farakhan_hamkari_date_f = []
        farakhan_hamkari_place = []
        l = []

        for i in hamkari_user:
            if i.darman == True:
                l.append('k')
            if i.sakht == True:
                l.append('k')
            if i.amoozesh == True:
                l.append('k')
            if i.farhangi == True:
                l.append('k')
            if i.daroo == True:
                l.append('e')
            if i.lebas == True:
                l.append('e')
            if i.ghaza == True:
                l.append('e')
            if i.tahrir == True:
                l.append('e')
            if i.masaleh == True:
                l.append('e')
            if i.naghdi_mostaghim == True:
                l.append('n')
            if i.naghdi_ghest == True:
                l.append('n')

        if 'k' in l:
            hamkari_type += ' خدمات '  # TODO: the date of l_farakhan_name may not be in order
            farakhan_name = Farakhan.objects.filter(hamkari_type='k')
            for i in farakhan_name:
                farakhan_hamkari_title.append(i.hamkari_title)
                farakhan_hamkari_place.append(i.place)
                farakhan_hamkari_date_f.append(str(i.date_first))

        if 'e' in l:
            hamkari_type += ' اجناس اهدایی '
            farakhan_name = Farakhan.objects.filter(hamkari_type='e')
            for i in farakhan_name:
                farakhan_hamkari_title.append(i.hamkari_title)
                farakhan_hamkari_place.append(i.place)
                farakhan_hamkari_date_f.append(str(i.date_first))

        if 'n' in l:
            hamkari_type += ' نقدی '
            farakhan_name = Farakhan.objects.filter(hamkari_type='n')
            for i in farakhan_name:
                farakhan_hamkari_title.append(i.hamkari_title)
                farakhan_hamkari_place.append(i.place)
                farakhan_hamkari_date_f.append(str(i.date_first))

        info = {
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'father_name': father_name,
            'date_birth': date_birth,
            'national_code': national_code,
            'email': email,
            'hamkari_type': hamkari_type,
            'farakhan_hamkari_title': farakhan_hamkari_title,
            'farakhan_hamkari_date_f': farakhan_hamkari_date_f,
            'farakhan_hamkari_place': farakhan_hamkari_place,
        }

        return render(request, 'profile.html', context=info)
    else:
        return redirect('appfront:login')


def Login(request):
    if request.method == 'POST':
        print('vared post shod')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('vared user shod')
            login(request, user)
            return redirect('appfront:profile')
        else:
            return redirect('appfront:login')
    else:
        print('vared login shod')
        return render(request, 'login.html')

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'index.html')