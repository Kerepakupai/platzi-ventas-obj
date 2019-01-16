import click


@click.group()
def solds():
    """Manages solds"""
    pass


@solds.command()
@click.pass_context
def create(ctx, product, price, quantity):
    """Register a new sold"""
    pass


all = solds