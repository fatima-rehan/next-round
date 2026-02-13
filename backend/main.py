from fastapi import FastAPI # handles backend server

from fastapi.middleware.cors import CORSMiddleware # connects react and fastapi

app = FastAPI() # creates app instance

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"], # react app's address
    allow_credentials = True,
    allow_methods = ["*"],  # '*' is all allowed
    allow_headers = ["*"],  
)

@app.get("/") # fetching data
def root():
    return {"message": "Next Round is running!"} # converts Python dicts to JSON


