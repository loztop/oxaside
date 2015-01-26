from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from games.models import Game

from django.shortcuts import render_to_response, get_object_or_404

from django.http import HttpResponseRedirect

from django.contrib import auth

from django.contrib.auth import authenticate

from django.core.context_processors import csrf

from games.forms import MyRegistrationForm
from games.forms import MyLoginForm
from games.forms import GameForm
from django.contrib.auth.models import User


from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django_tables2   import RequestConfig
from games.tables  import GameTable, UpdateTable
from django.template import RequestContext

from datetime import datetime    
from django.utils import timezone



import datatableview
from datatableview.views import DatatableView, XEditableDatatableView
from datatableview.utils import get_datatable_structure
from datatableview import helpers


def test_editable(request):
    if request.is_ajax():
        task = request.GET.get('task')
        #updated_task = Task.objects.get(pk=task_id)
        #updated_task.task = task
        #updated_task.save()
        return HttpResponse('true')
    else:
        return render_to_response('test_editable.html')
        #return HttpResponse('not ajax')





class DemoMixin(object):
    description = """Missing description!"""
    implementation = """Missing implementation details!"""

    def get_template_names(self):
        """ Try the view's snake_case name, or else use default simple template. """
        name = self.__class__.__name__.replace("DatatableView", "")
        name = re.sub(r'([a-z]|[A-Z]+)(?=[A-Z])', r'\1_', name)
        return ["demos/" + name.lower() + ".html", "example_base.html"]

    def get_context_data(self, **kwargs):
        context = super(DemoMixin, self).get_context_data(**kwargs)
        context['implementation'] = self.implementation

        # Unwrap the lines of description text so that they don't linebreak funny after being put
        # through the ``linebreaks`` template filter.
        alert_types = ['info', 'warning', 'danger']
        paragraphs = []
        p = []
        alert = False
        for line in self.__doc__.splitlines():
            line = line[4:].rstrip()
            if not line:
                if alert:
                    p.append(u"""</div>""")
                    alert = False
                paragraphs.append(p)
                p = []
            elif line.lower()[:-1] in alert_types:
                p.append(u"""<div class="alert alert-{type}">""".format(type=line.lower()[:-1]))
                alert = True
            else:
                p.append(line)
        description = "\n\n".join(" ".join(p) for p in paragraphs)
        context['description'] = re.sub(r'``(.*?)``', r'<code>\1</code>', description)

        return context

class XEditableColumnsDatatableView(DemoMixin, XEditableDatatableView):
   
    model = Game
    datatable_options = {
        'columns': [
            'id',
            ("Headline", 'headline', helpers.make_xeditable),
            ("Blog", 'blog', helpers.make_xeditable),
            ("Published date", 'pub_date', helpers.make_xeditable),
        ]
    }

    implementation = u"""
    class XEditableColumnsDatatableView(XEditableDatatableView):
        model = Game
        datatable_options = {
            'columns': [
                'id',
                ("Headline", 'headline', helpers.make_xeditable),
                ("Blog", 'blog', helpers.make_xeditable),
                ("Published date", 'pub_date', helpers.make_xeditable),
            ]
        }
    </pre>
    <pre class="brush: javascript">
    // Page javascript
    datatableview.auto_initialize = false;
    $(function(){
        var xeditable_options = {};
        datatableview.initialize($('.datatable'), {
            fnRowCallback: datatableview.make_xeditable(xeditable_options),
        });
    })
    """










def index(request):
    #table_live = GameTable(Game.objects.all())
    table_live = GameTable(Game.objects.filter(kickoff_date__gte=timezone.now()))
    table_past = GameTable(Game.objects.filter(kickoff_date__lte=timezone.now()))

     #   table = GameTable(Game.objects.filter(user=request.user.id))


   # table_live.order_by = "kickoff_date"
   # table_past.order_by = "kickoff_date"
    #context_instance = RequestContext(request)
    RequestConfig(request).configure(table_past)
    RequestConfig(request).configure(table_live)

    #c = {}
    #c.update(csrf(request))    
    #return render(request, 'index.html', {'table_past': table_past, 'table_live': table_live})
    return render(request, 'index.html', {'table_past': table_past, 'table_live': table_live})

 ##Authentication stuff

def login(request):
    c = {}
    c.update(csrf(request))    
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
	#password = request.POST.get('password', '')
    password = 'g'

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/add_game')
    else:
        return HttpResponseRedirect('/invalid')


def loggedin(request):
    return render_to_response('loggedin.html', 
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')


def invalid_update_login(request):
    return render_to_response('invalid_update_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def register_view(request):
    if request.method == 'POST':
        data = request.POST.copy() 
        data['password1'] = 'g'
        data['password2'] = 'g'

        form = MyRegistrationForm(data)
        #form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #login in straight away
            username = request.POST.get('username', '')
            password = 'g'
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/add_game')
        
    else:
        form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('register.html', args)



def register_success(request):
    return render_to_response('register_success.html')



def update_login_view(request):
    username = request.POST.get('username', '')
	#password = request.POST.get('password', '')
    password = 'g'

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/update')
    else:
        return HttpResponseRedirect('/invalid')


def update_view(request):
	return render_to_response('update.html', 
                              {'full_name': request.user.username})


def about(request):
    return render_to_response('about.html')

def add_start(request):
    form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('add_start.html',args)




def add_login(request):
    username = request.POST.get('username', '')
    password = 'g'
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/add_game')
    else:
        form = MyLoginForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    args['form_error'] = 'Username does not exist'

    return render_to_response('add_start.html', args)



def add_register(request):
	#args = {}
	#args.update(csrf(request))
	#return render_to_response('add_register.html',args)
    if request.method == 'POST':
        data = request.POST.copy() 
        data['password1'] = 'g'
        data['password2'] = 'g'

        form = MyRegistrationForm(data)
        #form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #login in straight away
            username = request.POST.get('username', '')
            password = 'g'
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/add_game')
     
    else:
        form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('register.html', args)

def add_game(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = GameForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new game to the database.

            #form.save(commit=True)


            game=form.save(commit=False)
            game.user_id=request.user.id
            game.save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
            
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = GameForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('add_game.html', {'form': form, 'full_name': request.user.username}, context)


def update_start(request):
    form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('update_start.html',args)

#def add_login(request):
#   return render_to_response('add_game.html')

def update_login(request):
    username = request.POST.get('username', '')
    password = 'g'
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/update_game')
    else:
        form = MyLoginForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    args['form_error'] = 'Username does not exist'

    return render_to_response('update_start.html', args)


def update_game(request):

    table = UpdateTable(Game.objects.filter(user=request.user.id))
    table.order_by = "kickoff_date"
    #context_instance = RequestContext(request)
    #RequestConfig(request).configure(table)
    #c = {}
    #c.update(csrf(request))    
    
    # Get the context from the request.
    context = RequestContext(request)
    return render_to_response('update_game.html', { 'table': table,'full_name': request.user.username}, context)