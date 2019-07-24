import click, requests, os


@click.group()
@click.option('--name', prompt=True)
@click.option('--password', prompt=True)
@click.pass_context
def login(ctx, name, password):
    token_url = "https://tiki.vn/api/v2/tokens"
    data = {'grant_type': 'password', 'email': name, 'password': password}
    response = requests.post(token_url, data=data)
    ctx.obj = response.cookies
    click.echo(response.status_code)
    
@login.command()
@click.pass_context
def getadd(ctx):
    getaddress = "https://tiki.vn/api/v2/me/addresses"
    address = requests.get(getaddress, cookies=ctx.obj)
    click.echo(address.status_code)
    

if __name__ == '__main__':
    login()