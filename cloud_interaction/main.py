from fastapi import FastAPI
from mangum import Mangum
from cloud_interaction.router import router as cloud_router

import uvicorn


app = FastAPI()
app.include_router(cloud_router)


mangum = Mangum(app)
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=False)
