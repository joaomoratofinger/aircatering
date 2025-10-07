# Guia de Instalação e Execução - AirCatering BI

## Pré-requisitos

- Node.js 18+ 
- PostgreSQL 14+
- npm ou yarn
- Docker (opcional)

## Instalação Manual

### 1. Clone o repositório
```bash
git clone <repo-url>
cd airCatering
```

### 2. Configure o banco de dados
```bash
# Instalar PostgreSQL e criar banco
sudo -u postgres psql
CREATE DATABASE aircatering_bi;
CREATE USER aircatering_user WITH PASSWORD 'aircatering_pass';
GRANT ALL PRIVILEGES ON DATABASE aircatering_bi TO aircatering_user;
\q

# Executar scripts de criação
psql -U aircatering_user -d aircatering_bi -f database/setup.sql
psql -U aircatering_user -d aircatering_bi -f database/schemas/tables.sql
psql -U aircatering_user -d aircatering_bi -f database/seeds/sample_data.sql
```

### 3. Configure o backend
```bash
cd backend
cp .env.example .env
# Edite o arquivo .env com suas configurações
npm install
npm run dev
```

### 4. Configure o frontend
```bash
cd frontend
npm install
npm start
```

## Instalação com Docker

### 1. Usando Docker Compose
```bash
# Subir todos os serviços
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar serviços
docker-compose down
```

### 2. Acessar aplicação
- Frontend: http://localhost:3000
- Backend API: http://localhost:3001
- Adminer (DB): http://localhost:8080

## Usuários de Teste

| Email | Senha | Papel |
|-------|-------|-------|
| admin@aircatering.com | admin123 | admin |
| manager@aircatering.com | admin123 | manager |
| user@aircatering.com | admin123 | user |

## Estrutura do Projeto

```
airCatering/
├── frontend/          # React + TypeScript
├── backend/           # Node.js + Express + TypeScript
├── database/          # PostgreSQL scripts
├── docs/              # Documentação
├── docker/            # Configurações Docker
└── docker-compose.yml # Orquestração Docker
```

## Scripts Disponíveis

### Frontend
- `npm start` - Inicia em desenvolvimento
- `npm build` - Build para produção
- `npm test` - Executa testes

### Backend
- `npm run dev` - Inicia em desenvolvimento
- `npm run build` - Build para produção
- `npm start` - Inicia produção

## Módulos do Sistema

1. **Dashboard** - Visão geral e KPIs
2. **Vendas** - Gestão de vendas e clientes
3. **Faturamento** - Controle de notas fiscais
4. **Compras** - Gestão de fornecedores
5. **Financeiro** - Fluxo de caixa e transações
6. **Estoque** - Controle de inventário
7. **Produção** - Ordens de produção
8. **RH** - Gestão de funcionários
9. **Empresas** - Gestão do grupo empresarial

## Desenvolvimento

### Contribuindo
1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

### Tecnologias Utilizadas
- **Frontend**: React 18, TypeScript, Material-UI, Chart.js
- **Backend**: Node.js, Express, TypeScript, PostgreSQL
- **Database**: PostgreSQL 14+
- **Auth**: JWT + Passport.js
- **Real-time**: Socket.io

## Suporte

Para suporte e dúvidas, entre em contato com a equipe de desenvolvimento.