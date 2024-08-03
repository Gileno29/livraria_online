
# 🌐 Livraria

# Utilização

### Clonando o Repositório

```bash
git clone https://github.com/Gileno29/livraria_online.git

cd livraria_online
```

###

### instalando e configurando o banco de dados
```bash
    sudo apt-get install postgresql

    su postgres

    psql

    create role userlivraria login password 'livraria';

    create database dblivraria owner userlivraria;

    \q

```

### rodando o projeto
```bash
# Criar ambiente virtual
python3 -m venv livraria-venv

# Ativar ambiente virtual
source livraria-venv/bin/activate  # No Windows use `venv\Scripts\activate`

# Instalar dependências necessárias para execução do projeto
pip install -r requirements.txt

#Rodar a aplicação em modo de desenvolvimento
python manage.py makemigrations
python manage.py migrate

python manage.py runserver
```


## 📁 Estrutura de Pastas

```plaintext
.
├── core
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── livraria
│   ├── admin.py
│   ├── api_books.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── README.md
├── requirements.txt
└── templates
    ├── base.html
    ├── carrinho.html
    ├── detalhes.html
    ├── index.html
    └── _navbar.html
```



## 📧 Contato

👤 **Seu Nome**

- Github: [@Gileno29](https://github.com/Gileno29/agenda)
- LinkedIn: [Gileno Duarte](https://www.linkedin.com/in/gileno-cordeiro-duarte-75913a164/)
- Email: gilenoduarte.jobs@gmail.com
---

