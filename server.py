from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/mcp")
async def mcp(request: Request):
    body = await request.json()
    return {"received": True, "body": body}


