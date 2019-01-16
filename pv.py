import click

from clients import commands as clients_commands
from solds import commands as solds_commands


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}


cli.add_command(clients_commands.all)
cli.add_command(solds_commands.solds)
