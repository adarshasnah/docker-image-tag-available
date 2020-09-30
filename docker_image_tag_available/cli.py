import click
import requests
import sys

@click.command()
@click.option("--registry-url", envvar='REGISTRY_URL', prompt="Enter url for docker registry", required=True, help="Url for docker registry")
@click.option("--user", envvar='REGISTRY_USER', prompt="User", required=True, help="Username for docker registry")
@click.option("--password", envvar='REGISTRY_PWD', prompt="Password", required=True, help="Password for docker registry")
@click.option("--image-name", envvar='IMAGE_NAME', prompt="Image", required=True, help="Image for docker registry")
@click.option("--image-version", envvar='IMAGE_VERSION', prompt="Version", required=True, help="Version for docker registry")
def main(registry_url, user, password, image_name, image_version):

    try:        
        r = requests.get('%s/v2/%s/tags/list' % (registry_url, image_name), auth=(user, password))
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        click.echo(click.style('Cannot connect to registry', fg='red'))
        sys.exit(1)
    else:        
        tags = r.json()['tags']
    
        if image_version in tags:
            click.echo(click.style('Version not available', fg='red'))
            sys.exit(1)
        else:
            click.echo(click.style('Version available', fg='green'))
            sys.exit(0)