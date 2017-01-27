import click

from push_service import Service


@click.command()
@click.argument('device_id')
@click.argument('message')
def cli_push(device_id, message):
    """Push MESSAGE to DEVICE_ID"""
    post_data = {
        'tokens': [device_id],
        'data':
            {
                'message': message
            }
    }

    service = Service(post_data)
    response = service.post()
    print("Response: " + str(response.json()))
    return response


if __name__ == '__main__':
    cli_push()
