from fastapi import FastAPI

app = FastAPI(
    title='Trading App'
)

fake_users = [
    {'id': 1, 'rule': 'admin', 'name': 'Bob'},
    {'id': 2, 'rule': 'user', 'name': 'Joj'},
    {'id': 3, 'rule': 'user', 'name': 'Socs'}
]

fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 123, 'amount': 2.12},
    {'id': 2, 'user_id': 1, 'currency': 'BTC', 'side': 'sell', 'price': 125, 'amount': 2.12}
]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]

@app.get('/trades')
def get_trades(limit: int = 2, offset: int = 0):
    return fake_trades[offset:][:limit]

fake_users2 = [
    {'id': 1, 'rule': 'admin', 'name': 'Bob'},
    {'id': 2, 'rule': 'user', 'name': 'Joj'},
    {'id': 3, 'rule': 'user', 'name': 'Socs'}
]

@app.post('/users/{user_id}')
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get('id') == user_id, fake_users2))[0]
    current_user['name'] = new_name
    return  {'status': 200, 'data': current_user}