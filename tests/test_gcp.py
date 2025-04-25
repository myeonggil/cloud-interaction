import asyncio
import os
import json

from google.cloud import billing_v1
from google.oauth2 import service_account


async def main():
    with open("/Users/jumyeonggil/code-workspace/cloud-interaction/client_secret.json") as client_info:
        client_info = json.load(client_info)
    storage_account = service_account.Credentials.from_service_account_file(
        info=client_info
    )
    gcp_client = billing_v1.CloudBillingAsyncClient(credentials=storage_account)

    # Initialize request argument(s)
    request = billing_v1.GetProjectBillingInfoRequest(
        name="projects/playground-457606",
    )

    # Make the request
    response = await gcp_client.get_project_billing_info(
        request=request
    )

    # Handle the response
    print(response)


if __name__ == '__main__':
    asyncio.run(main())
