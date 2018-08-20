# SistemaVendas
Sistema de vendas onde seja possível cadastrar produtos, registrar pagamento e acompanhar a montagem do pedido.

## Requirementos 
Virtual environment, Python3, Django

# Instalação
Ativar virtual environment em: SistemaVendas/sistemavendas
source bin/activate

Em: SistemaVendas/sistemavendas/sitevendas
python manage.py loaddata populate_db.json
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Acesse http://localhost:8000/ 
