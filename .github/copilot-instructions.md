<!-- Instruções específicas do projeto de Business Intelligence para o Copilot -->

# Projeto BI - Sistema de Gestão Corporativa

Este é um sistema completo de Business Intelligence para gestão corporativa com os seguintes módulos:

## Módulos do Sistema
- **Vendas**: Gestão de vendas, clientes, pedidos e comissões
- **Faturamento**: Controle de faturamento, notas fiscais e receitas
- **Compras**: Gestão de fornecedores, pedidos de compra e recebimentos
- **Financeiro**: Controle financeiro, fluxo de caixa e contas a pagar/receber
- **Estoque**: Controle de inventário, movimentações e níveis de estoque
- **Produção**: Planejamento e controle de produção
- **Recursos Humanos**: Gestão de funcionários, folha de pagamento e benefícios
- **Gestão de Empresas do Grupo**: Dashboard para gerenciar outras empresas do grupo

## Arquitetura do Projeto
- **Frontend**: React + TypeScript + Material-UI
- **Backend**: Node.js + Express + TypeScript
- **Banco de Dados**: PostgreSQL
- **Autenticação**: JWT + Passport.js
- **Dashboards**: Chart.js / Recharts
- **Real-time**: Socket.io

## Estrutura do Projeto
```
airCatering/
├── frontend/          # Aplicação React
├── backend/           # API Node.js
├── database/          # Scripts SQL e migrações
├── docs/              # Documentação
└── docker/            # Configurações Docker
```

## Instruções para o Copilot
- Sempre considerar a arquitetura modular do sistema
- Implementar validações tanto no frontend quanto no backend
- Manter padrões de código TypeScript rigorosos
- Criar componentes reutilizáveis para dashboards
- Implementar tratamento de erros robusto
- Seguir princípios de design responsivo
- Considerar performance para grandes volumes de dados