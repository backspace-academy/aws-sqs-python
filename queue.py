# Load the AWS SDK for Python
import boto3

# Load the exceptions for error handling
from botocore.exceptions import ClientError, ParamValidationError

# Create AWS service client and set region
s3 = boto3.client('s3', region_name='us-east-1')

# Call the S3 service to get a list of buckets in the account
def s3_list_buckets():
    try:
        data = s3.list_buckets()
        return data
    # An error occurred
    except ParamValidationError as e:
        print("Parameter validation error: %s" % e)
    except ClientError as e:
        print("Client error: %s" % e)


# Main program
def main():
    print('Code loaded successfully')
    response = s3_list_buckets()
    print('S3 Buckets in your account:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')    

if __name__ == '__main__':
    main()
