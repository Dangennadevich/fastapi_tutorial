from fastapi import FastAPI, Path
from fastapi.responses import  PlainTextResponse, HTMLResponse, FileResponse

app = FastAPI()

@app.get("/")
def root():
    return {"meassage" : "Hello, student!"}


@app.get("/add")
def add(x: int, y: int) -> int:
    return x+y


@app.get("/double/{number}")
def double(number: int) -> int:
    return number * 2


@app.get("/welcome/{name}/{surname}")
def welcome(name: str = Path(min_length=3, max_length=20), surname: str = Path(min_length=3, max_length=20)) -> str:
    return f"Good luck, {name} {surname}"


@app.get("/phone/{number}")
def phone_number(number: str = Path(regex="[7-8]\d{10}$")):
    return {"phone" : number}

@app.get("/text")
def text():
    content = "Banan order Fire, Dragon and Fure - because she drinc Adrinalin Rush Banana when she was littel baby!"
    return PlainTextResponse(content=content)


@app.get("/html")
def html():
    content = "<h1> test  html <h1/>"
    return HTMLResponse(content=content)


@app.get("/file")
def file():
    content = "index.html"
    return FileResponse(
        content,
        media_type="application/octet-stream",
        filename="index_2.html"
    )


@app.get(path="/html2", response_class=HTMLResponse)
def html():
    content = "<h1> test  html <h1/>"
    return content
