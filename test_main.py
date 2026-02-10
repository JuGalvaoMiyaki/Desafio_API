from fastapi.testclient import TestClient  #importando TestClient do fastapi
from main import app #importando app do arquivo main

client = TestClient(app)  #criando o objeto TestClient

def test_mensagem(): #criando função de teste
    response = client.get("/") #variavel response recebe o resultado do endpoint
    assert response.status_code == 200 #assegure que o resultado do endpoint terá o status code 200 - bem sucedido
    assert response.json() == {"mensagem": "Tudo okay por aqui"} #assegure de que o resultado será a mensagem em json
