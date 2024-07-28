# TutosDevs - Tutoriais para Iniciantes

**TutosDevs** é um projeto de extensão desenvolvido para a Escola de Inverno para Meninas, focado em ensinar HTML, CSS, JavaScript, Python e Django de forma gratuita. O projeto foi criado por Ana Paula Lourenço, uma desenvolvedora FullStack e estudante de Análise e Desenvolvimento de Sistemas na PUCPR.

## Índice

- [TutosDevs - Tutoriais para Iniciantes](#tutosdevs---tutoriais-para-iniciantes)
  - [Índice](#índice)
  - [Sobre o Projeto](#sobre-o-projeto)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
  - [Configuração do Ambiente](#configuração-do-ambiente)
  - [Uso](#uso)
  - [Contribuição](#contribuição)
  - [Contato](#contato)

## Sobre o Projeto

O **TutosDevs** é uma plataforma de tutoriais para iniciantes que fornece recursos educativos gratuitos para aprender programação e desenvolvimento web. Este projeto foi desenvolvido como parte do processo de seleção para ser monitora voluntária na Escola de Inverno para Meninas, promovida pelo Grupo de Alunas de Ciências Exatas (GRACE) do ICMC USP.

## Tecnologias Utilizadas

- **Django**: Framework para desenvolvimento web em Python.
- **HTML/CSS/JavaScript**: Tecnologias básicas para criação de páginas web e interação com o usuário.
- **Python**: Linguagem de programação usada no back-end.
- **Git**: Sistema de controle de versão para gerenciamento de código fonte.

## Configuração do Ambiente

Para configurar o ambiente de desenvolvimento e rodar o projeto localmente, siga os passos abaixo:

1. **Faça um fork do repositório.**

2. **Clone o repositório**

    ```bash
    git clone https://github.com/seu_usuario/seu_repositorio.git
    ```

3. **Crie e ative um ambiente virtual**

    ```bash
    cd seu_repositorio
    python -m venv venv
    source venv/bin/activate  # Para Windows use: venv\Scripts\activate
    ```

4. **Instale as dependências**

    ```bash
    pip install -r requirements.txt
    ```

5. **Configure as variáveis de ambiente**

    Crie um arquivo `.env` na raiz do projeto e adicione suas configurações específicas (por exemplo, configurações de banco de dados).

6. **Aplique as migrações do banco de dados**

    ```bash
    python manage.py migrate
    ```

7. **Inicie o servidor de desenvolvimento**

    ```bash
    python manage.py runserver
    ```

8. **Acesse o projeto**

    Abra seu navegador e vá para `http://127.0.0.1:8000/`.

## Uso

Para começar a usar a plataforma, acesse a página inicial do projeto. Aqui você encontrará tutoriais sobre HTML, CSS, JavaScript, e Python, além de boas práticas para iniciantes. Navegue pelos tutoriais e siga as instruções para aprimorar suas habilidades.

## Contribuição

Se você deseja contribuir para o projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma branch para a sua alteração (`git checkout -b minha-alteracao`).
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova funcionalidade'`).
4. Envie a branch para o repositório remoto (`git push origin minha-alteracao`).
5. Crie um pull request para revisão.

## Contato

Para mais informações ou se você tiver alguma dúvida, entre em contato comigo:

- **Email:** aanaplourenco@gmail.com ou annasouzaterapias@gmail.com
- **WhatsApp:** 41 998739318
- **Instagram:** [@aanaplourenco](https://www.instagram.com/aanaplourenco/)
- **LinkedIn:** [Ana Paula Lourenço](https://www.linkedin.com/in/aanaplourenco/)

Obrigado por visitar o TutosDevs!