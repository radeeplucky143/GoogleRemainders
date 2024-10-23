from fastapi import FastAPI
from api.calender import router

app = FastAPI(title="Google Remainders", description="Managing Google Remainders..")
app.include_router(router, prefix="/google")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8085, reload=True)
