import click


@click.group()
def main():
    pass


@main.command()
@click.argument("ip", required=True, type=str)
@click.option("-u", "--user-list", is_flag=True, help="Get user list details")
@click.option(
    "-m", "--machine-list", is_flag=True, help="Get machine list details"
)
@click.option(
    "-s", "--share-list", is_flag=True, help="Get share list details"
)
@click.option(
    "-p", "--password-policy", is_flag=True, help="Get password policy details"
)
@click.option(
    "-g", "--group-list", is_flag=True, help="Get group list details"
)
@click.option(
    "-d",
    "--detailed",
    is_flag=True,
    help="Get detailed output, applies to -u & -s",
)
def enumerate(ip):
    click.echo(f"Hello, {ip}!")


@main.command()
@click.argument("ip", required=True, type=str)
def all(ip):
    click.echo(f"Hello, {ip}!!")
