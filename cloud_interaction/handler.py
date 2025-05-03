import boto3
import asyncio
import os

from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv import load_dotenv

from mypy_boto3_ce import CostExplorerClient

load_dotenv("./cloud_interaction/.env")
client_info = {
    "type": os.environ["type"],
    "project_id": os.environ["project_id"],
    "private_key_id": os.environ["private_key_id"],
    "private_key": os.environ["private_key"],
    "client_email": os.environ["client_email"],
    "client_id": os.environ["client_id"],
    "auth_uri": os.environ["auth_uri"],
    "token_uri": os.environ["token_uri"],
    "auth_provider_x509_cert_url": os.environ["auth_provider_x509_cert_url"],
    "client_x509_cert_url": os.environ["client_x509_cert_url"],
    "universe_domain": os.environ["universe_domain"],
}


def get_aws_billing():
    session = boto3.Session(profile_name='backend', region_name='ap-northeast-2')
    client: CostExplorerClient = session.client("ce")

    res = client.get_cost_and_usage(
        TimePeriod={
            "Start": '2025-04-01',
            "End": '2025-04-24'
        },
        Granularity='DAILY',
        Metrics=["UnblendedCost", "UsageQuantity"]
    )


def get_gcp_billing():
    storage_account = service_account.Credentials.from_service_account_info(
        info=client_info
    )
    gcp_client = bigquery.Client(credentials=storage_account)

    # Initialize request argument(s)
    data = gcp_client.query(
        query='''
            SELECT
            SUM(cost) as total_cost,
            SUM(IFNULL(item.amount, 0)) as total_credits
            FROM
            `playground-457606.playground.gcp_billing_export_v1_0106CC_7EF913_130180`,
            UNNEST(credits) AS item;
        '''
    )

    # Handle the response
    data_frame = data.to_dataframe()
    print(data_frame.head())


def interact_cloud_billing(event, context):
    pass
