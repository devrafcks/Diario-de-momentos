# Projeto Diário de Anotações

![Captura de tela 2025-01-11 060030](https://github.com/user-attachments/assets/61ad4c80-5f83-4972-b214-ee38f90e049e)
![Captura de tela 2025-01-11 060430](https://github.com/user-attachments/assets/6376f02f-7544-4735-bb17-960ad0341687)
![Captura de tela 2025-01-11 060719](https://github.com/user-attachments/assets/15d0635b-e48c-42be-8c84-6efe92487f23)
![Captura de tela 2025-01-11 060202](https://github.com/user-attachments/assets/aa1bdff8-f422-412b-b733-f98290632521)

Este é um **Diário de Anotações** desenvolvido para ajudar os usuários a registrar, visualizar, excluir e analisar suas anotações diárias. A solução foi construída com o backend em **Django** e usa a biblioteca **Chart.js** para gráficos interativos, permitindo que o usuário tenha uma visão mais visual sobre suas anotações. Também oferece suporte ao upload e gerenciamento de imagens associadas a cada anotação.

## Funcionalidades

### 1. **Visualização de Anotações**
   O sistema permite que os usuários visualizem suas anotações de um dia específico, exibindo informações como título, texto e pessoas associadas a cada entrada. A interface é clara e facilita o acesso às anotações registradas.

### 2. **Exclusão de Anotações**
   Existe a opção de excluir todas as anotações de um dia específico. Essa funcionalidade facilita a limpeza do diário sem a necessidade de apagar as entradas individualmente.

### 3. **Gráficos Interativos**
   Usando **Chart.js**, o sistema exibe gráficos dinâmicos que mostram o número de anotações feitas por cada pessoa. Esses gráficos ajudam a visualizar a produtividade e o engajamento de forma simples e interativa.

### 4. **Interface de Usuário**
   A interface do sistema é responsiva, garantindo uma experiência otimizada tanto em dispositivos móveis quanto em desktops. A navegação é fácil e o design é moderno, com foco em usabilidade.

## Gerenciamento de Arquivos de Mídia

A configuração do projeto permite o upload e gerenciamento de arquivos de mídia (como imagens) associadas às anotações. O Django cuida da entrega eficiente desses arquivos utilizando as configurações `MEDIA_URL` e `MEDIA_ROOT`.

## Tecnologias Utilizadas

- **Django**: Framework web utilizado para criar o backend do projeto, responsável por gerenciar o banco de dados, autenticação de usuários, roteamento e lógica de negócios.
  
- **Chart.js**: Biblioteca JavaScript usada para criar gráficos interativos que exibem o número de anotações feitas por cada pessoa.

- **HTML/CSS**: Linguagens de marcação e estilo usadas para criar a interface do usuário. O design é responsivo e otimizado para diferentes dispositivos.

- **JavaScript**: Linguagem de programação utilizada para manipular os gráficos interativos na página inicial e para gerenciar eventos de interação do usuário.

## Como Rodar o Projeto

Siga os passos abaixo para rodar o projeto em sua máquina local:

### Pré-requisitos
- Python 3.10+
- Git
- Virtualenv (opcional, mas recomendado)

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DA_PASTA_CLONADA>
   ```

2. **Crie e ative um ambiente virtual (opcional)**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No macOS/Linux:
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados**
   Rode as migrações para configurar o banco de dados SQLite:
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor local**
   ```bash
   python manage.py runserver
   ```

6. **Acesse o projeto**
   Abra o navegador e vá para:
   ```
   http://127.0.0.1:8000
   ```

## Conclusão

Este sistema de **Diário de Anotações** oferece uma maneira prática de registrar, visualizar e gerenciar suas anotações diárias, com gráficos interativos para analisar o número de entradas feitas por cada pessoa. Ele é uma excelente base para quem deseja construir um sistema de gerenciamento de anotações com Django, e pode ser facilmente expandido com novas funcionalidades, como autenticação de usuários, comentários e outras formas de visualização.
