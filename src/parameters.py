import boto3
from botocore.exceptions import ClientError

def get_parameter(parameter_name):
    """
    Obtiene el valor de un parámetro de AWS Systems Manager Parameter Store.
    """
    try:
        ssm_client = boto3.client(
            'ssm',
            region_name='us-east-1',
            endpoint_url='http://localhost:4566'
        )
        response = ssm_client.get_parameter(
            Name=parameter_name,
            WithDecryption=True  # En caso de que el parámetro esté cifrado
        )
        return response['Parameter']['Value']
    except ClientError as e:
        print(f"Error al obtener el parámetro {parameter_name}: {e}")
        return None