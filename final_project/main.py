from datetime import datetime

from fastapi import FastAPI, Request, status, Form
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from storage import database as db

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')


class NewStory(BaseModel):
    title: str
    username: str = "Anon"
    content: str


class Story(NewStory):
    pk: int
    created_at: datetime


def _serialize_stories(stories: list[tuple]) -> list[Story]:
    stories_serialized = [
        Story(
            pk=story[0],
            title=story[1],
            username=story[2],
            content=story[3],
            created_at=story[4],
        ) for story in stories
    ]
    return stories_serialized


#  WEB

@app.get('/', tags=['website'])
@app.post('/search', tags=['website'])
@app.get('/search', tags=['website'])
def all_stories(request: Request, search_text: str = Form(None)):
    if search_text:
        stories = db.search_story(query_str=search_text)
    else:
        stories = db.get_stories(limit=5)
    stories_serialized = _serialize_stories(stories)
    context = {
        'title': f'Showing results for - {search_text}' if search_text else 'Home',
        'request': request,
        'stories': stories_serialized,
    }
    return templates.TemplateResponse('all_stories.html', context=context)


@app.get('/add', tags=['website'])
def add_story(request: Request):
    context = {
        'title': 'Home',
        'request': request,
    }
    return templates.TemplateResponse('add_story.html', context=context)


@app.post('/add', tags=['website'])
def add_story_final(
        request: Request,
        title: str = Form(),
        username: str = Form("Anon"),
        content: str = Form()
):
    db.add_story(
        title=title,
        username=username,
        content=content
    )

    stories = db.get_stories(limit=5)
    stories_serialized = _serialize_stories(stories)
    context = {
        'title': 'Your story has been added',
        'request': request,
        'stories': stories_serialized,
    }
    return templates.TemplateResponse('all_stories.html', context=context)

#  API



@app.post("/api/add_story", status_code=status.HTTP_201_CREATED, tags=['API'])
def add_story(story: NewStory):
    db.add_story(
        title=story.title,
        username=story.username,
        content=story.content
    )
    return story


@app.get('/api/get_stories', tags=['API'])
@app.post('/api/get_stories', tags=['API'])
def get_stories(limit: int = 5) -> list[Story]:
    stories = db.get_stories(limit=limit)
    return _serialize_stories(stories)


@app.get('/api/search_stories', tags=['API'])
def search_stories(query_str: str) -> list[Story]:
    stories = db.search_story(query_str=query_str)
    return _serialize_stories(stories)
