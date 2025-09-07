# 🏥 Sistema CRUD para Farmácia com MongoDB

## 📚 Descrição do Projeto

Sistema de gerenciamento de medicamentos para farmácia implementando operações CRUD (Create, Read, Update, Delete) utilizando MongoDB e Python.

## 🎯 Funcionalidades

- ✅ **CREATE**: Adicionar novos medicamentos
- ✅ **READ**: Listar todos os medicamentos  
- ✅ **UPDATE**: Atualizar informações dos medicamentos
- ✅ **DELETE**: Remover medicamentos
- ✅ Interface amigável via terminal

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **MongoDB** (Atlas na nuvem)
- **PyMongo** (Driver oficial MongoDB)
- **Git** & **GitHub** (Versionamento)

## 📦 Estrutura de Dados

Cada medicamento possui:
- `_id` (Identificador único)
- `nome` (String)
- `preco` (Float)
- `quantidade` (Integer)
- `tipo` (String)
- `data_criacao` (DateTime)
- `data_atualizacao` (DateTime - opcional)

## 🚀 Como Executar

### Pré-requisitos
- Python 3.x instalado
- Conta no MongoDB Atlas (opcional)

### Instalação
```bash
# Clone o repositório
git clone https://github.com/Rafael-ODias/farmacia-mongodb-crud.git

# Entre na pasta
cd farmacia-mongodb-crud

# Instale as dependências
pip install pymongo