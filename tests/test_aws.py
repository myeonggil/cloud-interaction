import boto3

from pprint import pprint
from mypy_boto3_ce import CostExplorerClient

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
pprint(res)
