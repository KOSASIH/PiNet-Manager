import click
from pi_net_manager.core.pi_net_manager import PiNetManager

@click.group()
def cli():
    pass

@cli.command()
@click.argument("device_id")
def get_device(device_id):
    pi_net_manager = PiNetManager()
    device = pi_net_manager.get_device(device_id)
    click.echo(device)

if __name__ == "__main__":
    cli()
