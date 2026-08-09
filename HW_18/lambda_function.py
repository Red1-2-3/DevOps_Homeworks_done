import json
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')


    custom_filter = [
        {'Name': 'instance-state-name', 'Values': ['running']},
        {'Name': 'tag:Environment', 'Values': ['Dev']}
    ]

    response = ec2.describe_instances(Filters=custom_filter)

    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    if instance_ids:
        print(f"Зупиняємо EC2 інстанси: {instance_ids}")
        ec2.stop_instances(InstanceIds=instance_ids)
        message = f"Успішно зупинено інстанси: {instance_ids}"
    else:
        print("Запущених EC2 інстансів з вказаним тегом не знайдено.")
        message = "Немає інстансів для зупинки."

    return {
        'statusCode': 200,
        'body': json.dumps({'message': message})
    }
