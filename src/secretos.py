import boto3
import json
from botocore.exceptions import ClientError

def get_secret(secret_name):
    """
    Obtiene el secreto desde AWS Secrets Manager.
    """
    try:
        secrets_client = boto3.client(
            'secretsmanager',
            region_name='us-east-1',
            endpoint_url='http://localhost:4566'
        )
        get_secret_value_response = secrets_client.get_secret_value(
            SecretId=secret_name
        )
        secret = get_secret_value_response['SecretString']
        return json.loads(secret)
    except ClientError as e:
        print(f"Error al obtener el secreto {secret_name}: {e}")
        return None