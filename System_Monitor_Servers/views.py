from django.shortcuts import render, redirect
from .models import Server
from .models import Topic
from .forms import ServerForm

def index(request):
    """The home page for System_Monitor_Servers."""
    servers = Server.objects.order_by('name')
    context = {'servers': servers}
    return render(request, 'System_Monitor_Servers/index.html', context)

def servers(request):
    """Show all servers."""
    servers = Server.objects.order_by('name')
    context = {'servers': servers}
    return render(request, 'System_Monitor_Servers/servers.html', context)

def topics(request):
    """Show all topics."""
    topics = Topic.objects.all().order_by('name')
    context = {'topics': topics}
    return render(request, 'System_Monitor_Servers/topics.html', context)

def server(request, server_id):
    """Show details for a single server."""
    server = Server.objects.get(id=server_id)
    context = {'server': server}
    return render(request, 'System_Monitor_Servers/server.html', context)

def new_server(request):
    """Add a new server."""
    if request.method == 'POST':
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('system_monitor_servers:servers')
    else:
        form = ServerForm()
    context = {'form': form}
    return render(request, 'System_Monitor_Servers/new_server.html', context)
