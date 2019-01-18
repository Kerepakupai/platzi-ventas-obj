import click

from clients.models import Client as ClientModel
from clients.services import Client as ClientService


@click.group()
def clients():
    """Manages the clientes Lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='The client\'s name')
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='The client\'s company')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='The client\'s email')
@click.option('-p', '--position',
              type=str,
              prompt=True,
              help='The client\'s position')
@click.pass_context
def create(ctx, name, company, email, position):
    """ Creates a new Client"""
    client = ClientModel(name, company, email, position)
    client_service = ClientService(ctx.obj['table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['table'])
    clients_list = client_service.list_client()
    title = ' LISTADO DE CLIENTES '

    print('=' * 80)
    print(title.center(80, '*'))
    print('=' * 80)

    for client in clients_list:
        print('{name} | {company} | {email} | {position} | {uid}'.format(
            name=client['name'],
            company= client['company'],
            email=client['email'],
            position=['position'],
            uid=client['uid']
        ))


@clients.command()
@click.pass_context
def update(ctx, uid):
    """Updates a client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, uid):
    """Deletes a client"""
    pass


all = clients


