import argparse
import uvicorn

from fastapi import FastAPI
from routers import notes, users


app = FastAPI()
app.include_router(users.router)
app.include_router(notes.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


def run_server(ip: str, port: int) -> None:
    uvicorn.run(app, host=ip, port=port, log_level="info", proxy_headers=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Host parameters')
    parser.add_argument('-i', '--ip', default="127.0.0.1", required=False)
    parser.add_argument('-p', '--port', default=5000, required=False)
    args = parser.parse_args()

    print(args.port)
    run_server(args.ip, int(args.port))
