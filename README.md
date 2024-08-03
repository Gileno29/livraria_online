
# 🌐 Livraria

### Clonando o Repositório

```bash
git clone https://github.com/Gileno29/livraria_online.git

cd livraria_online
```

### Configurando o Back-end (Django)

```bash
# Criar ambiente virtual
python3 -m venv livraria-venv

# Ativar ambiente virtual
source agenda-venv/bin/activate  # No Windows use `venv\Scripts\activate`

# Instalar dependências necessárias para execução do projeto
pip install -r requirements.txt

#Rodar a aplicação em modo de desenvolvimento

python manage.py runserver
```


### Executando a Aplicação em produção

```bash
sudo docker-compose up 
  #execute com a flag -d para executar em segundo plano


#Parar aplicação

docker-compose down -v
```
## 📁 Estrutura de Pastas

```plaintext
├── agenda
│   ├── agenda
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── core
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── db.sqlite3
│   ├── manage.py
│   ├── static
│   │   └── css
│   │       ├── agenda.css
│   │       ├── evento.css
│   │       └── login_style.css
│   └── templates
│       ├── agenda.html
│       ├── evento.html
│       ├── login.html
│       ├── model-footer.html
│       ├── model-header.html
│       └── model-page.html
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── nginx
│   ├── Dockerfile
│   └── nginx.conf
├── readme.md
└── requirements.txt
```
> Comando utilizado para mostrar a estrutura de dados `tree  -I '__pycache__' -I 'migrations' -I 'agenda_env'`.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

1. Faça um fork do projeto
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faça o push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📧 Contato

👤 **Seu Nome**

- Github: [@Gileno29](https://github.com/Gileno29/agenda)
- LinkedIn: [Gileno Duarte](https://www.linkedin.com/in/gileno-cordeiro-duarte-75913a164/)
- Email: gilenoduarte.jobs@gmail.com
---

Desenvolvido com profissionalismo por [Gileno Duarte](https://github.com/Gileno29/agenda) 🤖.
