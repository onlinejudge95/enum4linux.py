import click


@click.group()
def main():
    pass


@main.command()
@click.argument("ip", required=True, type=str)
def enumerate(ip):
    click.echo(f"Hello, {ip}!")


@main.command()
@click.argument("ip", required=True, type=str)
def all(ip):
    click.echo(f"Hello, {ip}!!")
