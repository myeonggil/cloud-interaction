from fastapi.routing import APIRouter
from google.cloud import billing_v1


router = APIRouter(prefix="cloud")

gcp_client = billing_v1.CloudBillingAsyncClient()


@router.post("/gcp")
async def interact_google_cloud_platform():
    # Initialize request argument(s)
    request = billing_v1.GetProjectBillingInfoRequest(
        name="name_value",
    )

    # Make the request
    response = await gcp_client.get_project_billing_info(request=request)

    # Handle the response
    print(response)


@router.post("/aws")
async def interact_amazon_web_service():
    pass
