from fastapi import FastAPI, HTTPException, status
from typing import Optional
from pydantic import BaseModel
import time


app = FastAPI()



import psycopg2
from psycopg2.extras import RealDictCursor
 

while True:
    try:
        conn = psycopg2.connect(
            ''' Enter your db connection settings'''
    )
        cursor = conn.cursor()
        print('Database connected succesfully!')
        break
    except Exception as error:
        print("Database connection failed")
        print(f"Error: {error}")
        time.sleep(2)





@app.get('/')
def root():
    return {"message": "root"}

# Get posts
@app.get('/posts')
def posts():
    cursor.execute(""" SELECT * FROM posts ORDER BY id""")
    post_list = cursor.fetchall()
    print(post_list)
    return {"posts": post_list}


# Get post detail
@app.get('/posts/{post_id}')
def post_detail(post_id: int):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s""", (post_id,))
    post_detail = cursor.fetchone()
    if not post_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post detail not found.")
    return post_detail


# post model
class Post(BaseModel):
    author: str
    title: str
    body: str
    is_published: Optional[bool]
    rating: Optional[int]


# Create posts
@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    cursor.execute(
        """ INSERT INTO posts (author, title, body, is_published, rating) VALUES (%s, %s, %s, %s, %s)""",
        (post.author, post.title, post.body, post.is_published, post.rating)
        )
    conn.commit()
    return post


@app.put('/posts/{post_id}')
def update_post(post_id: int, post: Post):
    cursor.execute(
        """ UPDATE posts SET author=%s, title=%s, body=%s, is_published=%s WHERE id = %s """,
        (post.author, post.title, post.body, post.is_published, post_id))
    return post






# @app.post('/posts', status_code=status.HTTP_201_CREATED)
# def create_post(post: Post):
#     cursor.execute(''' INSERT INTO posts (author, title, body, is_published, rating) VALUES
#                    (%s, %s, %s, %s, %s)
#                    ''', (post.author, post.title, post.body, post.is_published, post.rating))
#     conn.commit()
#     return post

# Delete Post
@app.delete('/posts/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):
    cursor.execute(''' DELETE FROM posts WHERE id = %s RETURNING *''', (post_id,))
    deleted_id = cursor.fetchone()
    conn.commit()
    if deleted_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post item with id {post_id} not found")
    return {"message": f"Post with id {post_id} has been deleted succesfully"}



@app.put('/posts/{post_id}')
def update_post(post_id: int, post: Post):
    cursor.execute(''' UPDATE posts SET author=%s, title=%s, 
        body=%s, is_published=%s, rating=%s WHERE id= %s RETURNING *''', 
        (post.author, post.title, post.body, post.is_published, post.rating, post_id))
    post = cursor.fetchone()
    if post is None:
        raise HTTPException(stat)
    conn.commit()
    return post