from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/mcp")
async def mcp(request: Request):
    body = await request.json()
    query = body.get("query") or body.get("prompt") or ""

    # Simple logic to return real answers
    q = query.lower()

    if "fraction" in q:
        answer = (
            "A fraction represents a part of a whole. "
            "It has a numerator (top number) and a denominator (bottom number). "
            "For example, 1/2 means one part out of two equal parts."
        )

    elif "genetic" in q:
        answer = (
            "Genetics is the study of how traits are passed from parents to offspring "
            "through DNA. Genes carry instructions that determine characteristics like "
            "eye color, height, and blood type."
        )

    else:
        answer = f"I received your question: {query}"

    return {"answer": answer}
