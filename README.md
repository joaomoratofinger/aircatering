# 🛫 AirCatering BI Dashboard

Sistema completo de Business Intelligence para gestão corporativa com visualizações interativas e análises em tempo real.

## 🌟 **Demonstração Online**
🔗 **[Acesse o Dashboard](https://aircatering.streamlit.app)** (após deploy)

## 📊 **Módulos Disponíveis**

### **🏠 Dashboard Principal**
- KPIs consolidados da empresa
- Métricas das empresas do grupo
- Faturamento, vendas e margens
- Evolução temporal

### **💰 Vendas**
- Análise de vendas por período
- Performance por vendedor
- Vendas por categoria e região
- Ticket médio e conversão

### **💼 Financeiro**
- Fluxo de caixa
- Receitas vs Despesas
- Análise por categoria
- Indicadores financeiros

### **📦 Estoque**
- Controle de inventário
- Alertas de estoque baixo
- Valor do estoque por categoria
- Gestão de produtos

### **👥 Recursos Humanos**
- Gestão de funcionários
- **Turnover e Absenteísmo**
- Salários por departamento
- Análises temporais de RH

### **🏭 Produção**
- Métricas de produção
- Eficiência por linha/turno
- Controle de qualidade
- Custos de produção

## 🚀 **Como Executar Localmente**

```bash
# Clone o repositório
git clone https://github.com/joaomoratofinger/aircatering.git
cd aircatering

# Instale as dependências
pip install -r requirements.txt

# Gere os dados de exemplo
python utils/gerar_dados.py

# Execute o dashboard
streamlit run app.py
```

## 📋 **Dependências**

- Python 3.8+
- Streamlit
- Plotly
- Pandas
- NumPy
- Faker

## 🛠️ **Personalização**

### **Logo da Empresa**
Adicione seu logo em `assets/logo.png` e ele aparecerá automaticamente na sidebar.

### **Dados**
Os dados são gerados automaticamente pelo script `utils/gerar_dados.py`. Modifique conforme necessário para seus dados reais.

## 📱 **Responsivo**
Dashboard otimizado para desktop e mobile com layout adaptativo.

---

**Desenvolvido com ❤️ usando Streamlit**

## 🛠️ Tecnologias

- **Frontend**: Streamlit
- **Visualização**: Plotly, Matplotlib
- **Dados**: Pandas, Numpy
- **Simulação**: Faker para dados de exemplo

## 📈 Funcionalidades

- Dashboards interativos
- Gráficos em tempo real
- Filtros dinâmicos
- Exportação de relatórios
- Interface responsiva