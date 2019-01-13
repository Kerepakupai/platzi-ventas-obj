import click


@click.group()
def clients():
    """Manages the clientes Lifecycle"""
    pass



@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """ Creates a new Client"""
    pass


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    pass


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


