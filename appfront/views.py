from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from app1.models import Hamkari, Farakhan, Profile_ready, User, Picture_farakhan
from datetime import date
from kavenegar import *
import jdatetime


# Create your views here.
def index(request):
    last_login = ''
    if request.user.is_authenticated:
        last_login = str(jdatetime.date.fromgregorian(date=request.user.last_login))
    farakhan = Farakhan.objects.filter(date_first__gte=date.today())
    farakhan_place = []
    farakhan_title = []
    farakhan_date_f = []
    farakhan_id = []
    for i in farakhan:
        farakhan_place.append(i.place)
        farakhan_title.append(i.farakhan_title)
        farakhan_date_f.append(str(i.date_first))
        farakhan_id.append(i.id)

    context = {
        'farakhan_place': farakhan_place,
        'farakhan_title': farakhan_title,
        'farakhan_date_f': farakhan_date_f,
        'farakhan_id': farakhan_id,
        'last_login': last_login,
    }

    print('vared login shod')
    return render(request, 'index.html', context=context)


def gallery(request, id=None):
    last_login = ''
    if request.user.is_authenticated:
        last_login = str(jdatetime.date.fromgregorian(date=request.user.last_login))


    farakhan_id = Farakhan.objects.get(id = id)
    picture = Picture_farakhan.objects.filter(farakhan = farakhan_id)

    picture_url = []
    for i in picture:
        picture_url.append(i.picture.url)


    context = {
        'last_login': last_login,
        'picture_url' : picture_url,
    }
    return render(request, 'gallery.html', context= context)


def folder_gallery(request):
    last_login = ''
    if request.user.is_authenticated:
        last_login = str(jdatetime.date.fromgregorian(date=request.user.last_login))

    farakhan = Farakhan.objects.all()
    farakhan_title = []
    farakhan_id = []
    for i in farakhan:
        farakhan_title.append(i.farakhan_title)
        farakhan_id.append(i.id)
    range = len(farakhan_id)
    context = {
        'last_login': last_login,
        'farakhan_title': farakhan_title,
        'farakhan_id': farakhan_id,
        'range' : range,
    }
    return render(request, 'folder_gallery.html', context=context)


def register(request):
    last_login = ''
    if request.user.is_authenticated:
        last_login = str(jdatetime.date.fromgregorian(date=request.user.last_login))

    if request.method == 'POST':
        receptor = request.POST.get('mobile')
        print('vared sms shod')
        print(receptor)
        api = KavenegarAPI('5A31706B38614D7352536A6F2B3173493959753258636E4A7363347777396B7672416F33657076426B4E6F3D')
        params = {'sender': '1000596446', 'receptor': receptor, 'message': 'سلام جواد جون!!!!!!!!!!!!!!!!!!!'}
        response = api.sms_send(params)
        print(response)
        return redirect('appfront:login')

    users = User.objects.all()
    username_list = []
    for i in users:
        username_list.append(i.username)

    context = {
        'username_list': username_list,
        'last_login': last_login,
    }

    return render(request, 'register.html', context=context)


def cooperation(request):
    last_login = ''
    if request.user.is_authenticated:
        last_login = str(jdatetime.date.fromgregorian(date=request.user.last_login))
    id_profile = request.user.profile.id

    context = {
        'id_profile': id_profile,
        'last_login': last_login,
    }
    return render(request, 'cooperation.html', context=context)


def cooperation_code(request):
    last_login = ''
    if request.user.is_authenticated:
        last_login = str(jdatetime.date.fromgregorian(date=request.user.last_login))
    context = {
        'last_login': last_login,
    }
    return render(request, 'cooperation_code.html', context=context)


def edit_profile(request, id=None):
    last_login = ''
    if request.user.is_authenticated:
        last_login = str(jdatetime.date.fromgregorian(date=request.user.last_login))

        id_profile = request.user.profile.id
        id_user = request.user.id

        context = {
            'id_profile': id_profile,
            'id_user': id_user,
            'last_login': last_login,
        }
        return render(request, 'edit_profile.html', context=context)


def create_farakhan(request):
    last_login = ''
    if request.user.is_authenticated:
        last_login = str(jdatetime.date.fromgregorian(date=request.user.last_login))
    context = {
        'last_login': last_login,
    }
    return render(request, 'create_farakhan.html', context=context)


def farakhan_detail(request, id=None):
    last_login = ''
    if request.user.is_authenticated:
        last_login = str(jdatetime.date.fromgregorian(date=request.user.last_login))

    if request.method == 'POST':
        print('vared post shod')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('vared user shod')
            login(request, user)
            return redirect('appfront:farakhan_detail', id)
        else:
            return redirect('appfront:login')
    else:
        farakhan = Farakhan.objects.get(id=id)
        farakhan_title = farakhan.farakhan_title
        farakhan_content = farakhan.farakhan_content
        farakhan_place = farakhan.place
        farakhan_date_f = farakhan.date_first
        farakhan_date_e = farakhan.date_end
        farakhan_type = farakhan.hamkari_type
        if farakhan_type == 'n':
            farakhan_type = 'نقدی'
        if farakhan_type == 'k':
            farakhan_type = 'خدمات'
        if farakhan_type == 'e':
            farakhan_type = 'اجناس اهدایی'

        id_farakhan = farakhan.id
        id_profile = None
        if request.user.is_authenticated:
            id_profile = request.user.profile.id

        context = {
            'farakhan_title': farakhan_title,
            'farakhan_place': farakhan_place,
            'farakhan_date_f': farakhan_date_f,
            'farakhan_date_e': farakhan_date_e,
            'farakhan_type': farakhan_type,
            'id_profile': id_profile,
            'id_farakhan': id_farakhan,
            'farakhan_content': farakhan_content,
            'last_login': last_login,
        }

        return render(request, 'farakhan_detail.html', context=context)


def farakhan_detail_sherkat(request, id=None):
    last_login = ''
    if request.user.is_authenticated:
        last_login = str(jdatetime.date.fromgregorian(date=request.user.last_login))
    context = {
        'last_login': last_login,
    }
    return render(request, 'farakhan_detail_sherkat.html', context=context)


def success(request):
    last_login = ''
    if request.user.is_authenticated:
        last_login = str(jdatetime.date.fromgregorian(date=request.user.last_login))
    context = {
        'last_login': last_login,
    }
    return render(request, 'success.html', context=context)


def profile(request):
    last_login = ''
    if request.user.is_authenticated:
        last_login = str(jdatetime.date.fromgregorian(date=request.user.last_login))

        username = request.user.username
        first_name = request.user.profile.first_name
        last_name = request.user.profile.last_name
        father_name = request.user.profile.father_name
        date_birth = request.user.profile.date_birth
        national_code = request.user.profile.national_code
        email = request.user.profile.email
        id_user = request.user.id
        id_profile = request.user.profile.id

        hamkari_user = Hamkari.objects.filter(profile__user=request.user)
        farakhan_ready = Profile_ready.objects.filter(profile__user=request.user)

        farakhan_ready_title = []
        farakhan_ready_date_f = []
        farakhan_ready_place = []

        for i in farakhan_ready:
            farakhan_ready_title.append(i.farakhan.farakhan_title)
            farakhan_ready_place.append(i.farakhan.place)
            farakhan_ready_date_f.append(str(i.farakhan.date_first))

        hamkari_type = ''
        farakhan_title = []
        farakhan_date_f = []
        farakhan_place = []
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
                farakhan_title.append(i.farakhan_title)
                farakhan_place.append(i.place)
                farakhan_date_f.append(str(i.date_first))

        if 'e' in l:
            hamkari_type += ' اجناس اهدایی '
            farakhan_name = Farakhan.objects.filter(hamkari_type='e')
            for i in farakhan_name:
                farakhan_title.append(i.farakhan_title)
                farakhan_place.append(i.place)
                farakhan_date_f.append(str(i.date_first))

        if 'n' in l:
            hamkari_type += ' نقدی '
            farakhan_name = Farakhan.objects.filter(hamkari_type='n')
            for i in farakhan_name:
                farakhan_title.append(i.farakhan_title)
                farakhan_place.append(i.place)
                farakhan_date_f.append(str(i.date_first))

        info = {
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'father_name': father_name,
            'date_birth': date_birth,
            'national_code': national_code,
            'email': email,
            'hamkari_type': hamkari_type,
            'farakhan_title': farakhan_title,
            'farakhan_date_f': farakhan_date_f,
            'farakhan_place': farakhan_place,
            'farakhan_ready_title': farakhan_ready_title,
            'farakhan_ready_date_f': farakhan_ready_date_f,
            'farakhan_ready_place': farakhan_ready_place,
            'id_user': id_user,
            'id_profile': id_profile,
            'last_login': last_login,
        }

        return render(request, 'profile.html', context=info)
    else:
        return redirect('appfront:login')


def Login(request):
    last_login = ''
    if request.user.is_authenticated:
        last_login = str(jdatetime.date.fromgregorian(date=request.user.last_login))
    context = {
        'last_login': last_login,
    }
    if request.method == 'POST':
        print('vared shoddddddddddddddddddddddddddddddddddddd')
        if request.user.is_authenticated:
            logout(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:

            print('vared user shod')
            login(request, user)
            return redirect('appfront:profile')
        else:
            return redirect('appfront:login')
    else:
        print('vared login shod')
        return render(request, 'login.html', context=context)


def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('appfront:index')


def test(request):
    return render(request, 'test.html')
