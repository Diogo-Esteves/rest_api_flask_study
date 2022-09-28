from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "Diogo Store",
        "items": [
            {"name": "chair", "price": 12.00},
            {"name": "sofa", "price": 444}
        ]
    }
]

@app.get("/store")
def get_store():
    return {"stores": stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": request_data["items"]}
    stores.append(new_store)
    return new_store, 201 
