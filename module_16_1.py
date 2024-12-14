from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def welcome() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return {f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def read_name(username, age: int):
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
