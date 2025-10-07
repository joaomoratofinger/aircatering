import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import os

# Configuração da página
st.set_page_config(
    page_title="AirCatering BI",
    page_icon="🛫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 0.75rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1f77b4;
        margin-bottom: 0.5rem;
    }
    .sidebar-info {
        background-color: #e6f3ff;
        padding: 0.75rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .logo-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1rem;
        padding: 0.75rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 1rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .logo-text {
        font-size: 2.5rem;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin: 0;
    }
    .logo-icon {
        font-size: 3rem;
        margin-right: 1rem;
    }
    .subtitle {
        color: #rgba(255,255,255,0.9);
        font-size: 1rem;
        margin-top: 0.5rem;
        text-align: center;
    }
    /* Reduzir espaçamentos do Streamlit */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    .element-container {
        margin-bottom: 0.5rem !important;
    }
    .stMetric {
        margin-bottom: 0.5rem !important;
    }
    .stPlotlyChart {
        margin-bottom: 0.5rem !important;
        margin-top: 0.5rem !important;
    }
    h1, h2, h3 {
        margin-top: 1rem !important;
        margin-bottom: 0.5rem !important;
    }
</style>
""", unsafe_allow_html=True)

def carregar_dados():
    """Carrega todos os datasets"""
    dados = {}
    
    try:
        if os.path.exists('data/vendas.csv'):
            dados['vendas'] = pd.read_csv('data/vendas.csv', parse_dates=['data_venda'])
        if os.path.exists('data/financeiro.csv'):
            dados['financeiro'] = pd.read_csv('data/financeiro.csv', parse_dates=['data'])
        if os.path.exists('data/estoque.csv'):
            dados['estoque'] = pd.read_csv('data/estoque.csv')
        if os.path.exists('data/rh.csv'):
            dados['rh'] = pd.read_csv('data/rh.csv', parse_dates=['data_admissao'])
        if os.path.exists('data/producao.csv'):
            dados['producao'] = pd.read_csv('data/producao.csv', parse_dates=['data_producao'])
        if os.path.exists('data/empresas_grupo.csv'):
            dados['empresas_grupo'] = pd.read_csv('data/empresas_grupo.csv', parse_dates=['data'])
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
    
    return dados

def mostrar_logo():
    """Mostra o logo da empresa - verifica se existe arquivo de imagem primeiro"""
    logo_paths = [
        'assets/logo.png',
        'assets/logotipo-1.png',  # Arquivo existente detectado
        'assets/logotipo.png',
        'assets/logo.jpg', 
        'assets/logo.jpeg',
        'assets/logo.svg',
        'logo.png',
        'logo.jpg',
        'logo.jpeg'
    ]
    
    # Verifica se existe algum arquivo de logo
    logo_encontrado = None
    for path in logo_paths:
        if os.path.exists(path):
            logo_encontrado = path
            break
    
    if logo_encontrado:
        # Se encontrou logo, exibe apenas a imagem sem texto (logo compacto)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(logo_encontrado, width=150)  # Logo ainda mais compacto
    else:
        # Se não encontrou logo, usa o design atual
        st.markdown('''
        <div class="logo-container">
            <div>
                # <div style="display: flex; align-items: center; justify-content: center;">
                #     <span class="logo-icon">🛫</span>
                #     <h1 class="logo-text">AIR CATERING</h1>
                # </div>
                <div class="subtitle">Business Intelligence Dashboard</div>
                <div style="font-size: 0.9rem; margin-top: 1rem; opacity: 0.8;">
                    💡 Dica: Adicione seu logo em 'assets/logo.png' para personalizar
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

def mostrar_logo_sidebar():
    """Mostra o logo na sidebar de forma compacta"""
    logo_paths = [
        'assets/logo.png',
        'assets/logotipo-1.png',  # Arquivo existente detectado
        'assets/logotipo.png',
        'assets/logo.jpg', 
        'assets/logo.jpeg',
        'assets/logo.svg',
        'logo.png',
        'logo.jpg',
        'logo.jpeg'
    ]
    
    # Verifica se existe algum arquivo de logo
    logo_encontrado = None
    for path in logo_paths:
        if os.path.exists(path):
            logo_encontrado = path
            break
    
    if logo_encontrado:
        # Se encontrou logo, exibe na sidebar
        st.image(logo_encontrado, width=180)
    else:
        # Se não encontrou logo, usa design compacto na sidebar
        st.markdown('''
        <div style="text-align: center; padding: 1rem 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 1rem; margin-bottom: 1rem;">
            <div style="color: white; font-size: 1.5rem; font-weight: bold;">
                🛫 AIR CATERING
            </div>
            <div style="color: rgba(255,255,255,0.8); font-size: 0.8rem;">
                Business Intelligence
            </div>
        </div>
        ''', unsafe_allow_html=True)

def main():
    # Sidebar com logo e navegação com logo e navegação
    with st.sidebar:
        # Logo na sidebar
        mostrar_logo_sidebar()  
        
        st.markdown("### 📊 Navegação")
        pagina = st.selectbox(
            "Selecione o módulo:",
            ["🏠 Dashboard Principal", "💰 Vendas", "💼 Financeiro", "📦 Estoque", "👥 Recursos Humanos", "🏭 Produção"]
        )
        
        # st.markdown('<div class="sidebar-info"><strong>Sistema:</strong> AirCatering BI<br><strong>Versão:</strong> 2.0<br><strong>Última atualização:</strong> Hoje</div>', unsafe_allow_html=True)
    
    # Carregar dados
    dados = carregar_dados()
    
    if not dados:
        st.warning("⚠️ Dados não encontrados. Execute o gerador de dados primeiro.")
        if st.button("🔄 Gerar Dados de Exemplo"):
            with st.spinner("Gerando dados..."):
                os.chdir('python_dashboard')
                os.system('python utils/gerar_dados.py')
                st.success("✅ Dados gerados com sucesso! Recarregue a página.")
                st.experimental_rerun()
        return
    
    # Renderizar página selecionada
    if pagina == "🏠 Dashboard Principal":
        mostrar_dashboard_principal(dados)
    elif pagina == "💰 Vendas":
        mostrar_vendas(dados)
    elif pagina == "💼 Financeiro":
        mostrar_financeiro(dados)
    elif pagina == "📦 Estoque":
        mostrar_estoque(dados)
    elif pagina == "👥 Recursos Humanos":
        mostrar_rh(dados)
    elif pagina == "🏭 Produção":
        mostrar_producao(dados)

def mostrar_dashboard_principal(dados):
    st.header("📈 Dashboard Principal")
    
    col1, col2, col3, col4 = st.columns(4)
    
    # KPIs principais
    if 'vendas' in dados:
        total_vendas = dados['vendas']['valor_total'].sum()
        col1.metric("💰 Total de Vendas", f"R$ {total_vendas:,.2f}")
    
    if 'financeiro' in dados:
        receitas = dados['financeiro'][dados['financeiro']['tipo'] == 'Receita']['valor'].sum()
        col2.metric("📈 Receitas", f"R$ {receitas:,.2f}")
    
    if 'estoque' in dados:
        produtos_estoque = len(dados['estoque'])
        col3.metric("📦 Produtos em Estoque", f"{produtos_estoque}")
    
    if 'rh' in dados:
        funcionarios_ativos = len(dados['rh'][dados['rh']['status'] == 'Ativo'])
        col4.metric("👥 Funcionários Ativos", f"{funcionarios_ativos}")
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        if 'vendas' in dados:
            st.subheader("📊 Vendas por Mês")
            df_vendas_mes = dados['vendas'].copy()
            df_vendas_mes['mes'] = df_vendas_mes['data_venda'].dt.to_period('M')
            vendas_mes = df_vendas_mes.groupby('mes')['valor_total'].sum().reset_index()
            vendas_mes['mes'] = vendas_mes['mes'].astype(str)
            
            fig = px.line(vendas_mes, x='mes', y='valor_total', 
                         title="Evolução das Vendas")
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        if 'vendas' in dados:
            st.subheader("🥧 Vendas por Categoria")
            vendas_cat = dados['vendas'].groupby('categoria')['valor_total'].sum().reset_index()
            
            fig = px.pie(vendas_cat, values='valor_total', names='categoria',
                        title="Distribuição por Categoria")
            st.plotly_chart(fig, use_container_width=True)
    
    # Seção das Empresas do Grupo
    if 'empresas_grupo' in dados:
        st.markdown("---")
        st.subheader("🏢 Empresas do Grupo Air Catering")
        
        df_empresas = dados['empresas_grupo']
        
        # Dados consolidados do último mês
        ultimo_mes = df_empresas['ano_mes'].max()
        df_ultimo_mes = df_empresas[df_empresas['ano_mes'] == ultimo_mes]
        
        # KPIs consolidados das empresas
        col1, col2, col3, col4 = st.columns(4)
        
        total_faturamento_grupo = df_ultimo_mes['faturamento'].sum()
        total_vendas_grupo = df_ultimo_mes['vendas'].sum()
        margem_media_grupo = df_ultimo_mes['margem_percentual'].mean()
        total_funcionarios_grupo = df_ultimo_mes['funcionarios'].sum()
        
        col1.metric("💰 Faturamento Total", f"R$ {total_faturamento_grupo:,.2f}")
        col2.metric("🛒 Vendas Total", f"R$ {total_vendas_grupo:,.2f}")
        col3.metric("📊 Margem Média", f"{margem_media_grupo:.1f}%")
        col4.metric("👥 Total Funcionários", f"{total_funcionarios_grupo}")
        
        # Gráficos das empresas
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📈 Faturamento por Empresa")
            faturamento_empresa = df_ultimo_mes.groupby('empresa')['faturamento'].sum().reset_index()
            faturamento_empresa = faturamento_empresa.sort_values('faturamento', ascending=True)
            
            fig = px.bar(faturamento_empresa, x='faturamento', y='empresa', 
                        orientation='h', title="Faturamento Mensal por Empresa",
                        color='faturamento', color_continuous_scale='Blues')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("🎯 Margem por Empresa")
            margem_empresa = df_ultimo_mes.sort_values('margem_percentual', ascending=True)
            
            fig = px.bar(margem_empresa, x='margem_percentual', y='empresa',
                        orientation='h', title="Margem % por Empresa",
                        color='margem_percentual', color_continuous_scale='Greens')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        # Evolução temporal consolidada
        st.subheader("📊 Evolução Temporal do Grupo")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Evolução do faturamento
            evolucao_faturamento = df_empresas.groupby('ano_mes')['faturamento'].sum().reset_index()
            evolucao_faturamento = evolucao_faturamento.sort_values('ano_mes')
            
            fig = px.line(evolucao_faturamento, x='ano_mes', y='faturamento',
                         title="Evolução do Faturamento Total",
                         markers=True)
            fig.update_layout(xaxis_title="Mês", yaxis_title="Faturamento (R$)")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Evolução da margem média
            evolucao_margem = df_empresas.groupby('ano_mes')['margem_percentual'].mean().reset_index()
            evolucao_margem = evolucao_margem.sort_values('ano_mes')
            
            fig = px.line(evolucao_margem, x='ano_mes', y='margem_percentual',
                         title="Evolução da Margem Média (%)",
                         markers=True, color_discrete_sequence=['green'])
            fig.update_layout(xaxis_title="Mês", yaxis_title="Margem (%)")
            st.plotly_chart(fig, use_container_width=True)

def mostrar_vendas(dados):
    st.header("💰 Módulo de Vendas")
    
    if 'vendas' not in dados:
        st.error("Dados de vendas não disponíveis")
        return
    
    df = dados['vendas']
    
    # Filtros
    col1, col2, col3 = st.columns(3)
    with col1:
        categorias = st.multiselect("Categorias", df['categoria'].unique(), default=df['categoria'].unique())
    with col2:
        regioes = st.multiselect("Regiões", df['regiao'].unique(), default=df['regiao'].unique())
    with col3:
        data_inicio = st.date_input("Data Início", df['data_venda'].min())
        data_fim = st.date_input("Data Fim", df['data_venda'].max())
    
    # Filtrar dados
    df_filtrado = df[
        (df['categoria'].isin(categorias)) &
        (df['regiao'].isin(regioes)) &
        (df['data_venda'] >= pd.to_datetime(data_inicio)) &
        (df['data_venda'] <= pd.to_datetime(data_fim))
    ]
    
    # Métricas
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de Vendas", f"R$ {df_filtrado['valor_total'].sum():,.2f}")
    col2.metric("Número de Vendas", f"{len(df_filtrado)}")
    col3.metric("Ticket Médio", f"R$ {df_filtrado['valor_total'].mean():,.2f}")
    col4.metric("Maior Venda", f"R$ {df_filtrado['valor_total'].max():,.2f}")
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        vendas_vendedor = df_filtrado.groupby('vendedor')['valor_total'].sum().sort_values(ascending=False).head(10)
        fig = px.bar(x=vendas_vendedor.values, y=vendas_vendedor.index, 
                    orientation='h', title="Top 10 Vendedores")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        vendas_canal = df_filtrado.groupby('canal')['valor_total'].sum()
        fig = px.pie(values=vendas_canal.values, names=vendas_canal.index,
                    title="Vendas por Canal")
        st.plotly_chart(fig, use_container_width=True)
    
    # Tabela de dados
    st.subheader("📊 Dados Detalhados")
    st.dataframe(df_filtrado.sort_values('data_venda', ascending=False), use_container_width=True)

def mostrar_financeiro(dados):
    st.header("💼 Módulo Financeiro")
    
    if 'financeiro' not in dados:
        st.error("Dados financeiros não disponíveis")
        return
    
    df = dados['financeiro']
    
    # Métricas principais
    receitas = df[df['tipo'] == 'Receita']['valor'].sum()
    despesas = abs(df[df['tipo'] == 'Despesa']['valor'].sum())
    lucro = receitas - despesas
    
    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Receitas", f"R$ {receitas:,.2f}")
    col2.metric("💸 Despesas", f"R$ {despesas:,.2f}")
    col3.metric("📈 Lucro", f"R$ {lucro:,.2f}", delta=f"{((lucro/receitas)*100):.1f}%")
    
    # Gráfico de fluxo de caixa
    df['data'] = pd.to_datetime(df['data'])
    df_mes = df.copy()
    df_mes['mes'] = df_mes['data'].dt.to_period('M')
    
    fluxo_mes = df_mes.groupby(['mes', 'tipo'])['valor'].sum().reset_index()
    fluxo_mes['mes'] = fluxo_mes['mes'].astype(str)
    
    fig = px.bar(fluxo_mes, x='mes', y='valor', color='tipo',
                title="Fluxo de Caixa Mensal", barmode='group')
    st.plotly_chart(fig, use_container_width=True)
    
    # Gráfico por categoria
    col1, col2 = st.columns(2)
    
    with col1:
        receitas_cat = df[df['tipo'] == 'Receita'].groupby('categoria')['valor'].sum()
        fig = px.pie(values=receitas_cat.values, names=receitas_cat.index,
                    title="Receitas por Categoria")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        despesas_cat = df[df['tipo'] == 'Despesa'].groupby('categoria')['valor'].sum()
        fig = px.pie(values=despesas_cat.values, names=despesas_cat.index,
                    title="Despesas por Categoria")
        st.plotly_chart(fig, use_container_width=True)

def mostrar_estoque(dados):
    st.header("📦 Módulo de Estoque")
    
    if 'estoque' not in dados:
        st.error("Dados de estoque não disponíveis")
        return
    
    df = dados['estoque']
    
    # Alertas de estoque baixo
    estoque_baixo = df[df['quantidade_atual'] <= df['quantidade_minima']]
    if len(estoque_baixo) > 0:
        st.warning(f"⚠️ {len(estoque_baixo)} produtos com estoque baixo!")
        with st.expander("Ver produtos com estoque baixo"):
            st.dataframe(estoque_baixo[['nome_produto', 'quantidade_atual', 'quantidade_minima']])
    
    # Métricas
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de Produtos", len(df))
    col2.metric("Valor Total Estoque", f"R$ {(df['quantidade_atual'] * df['preco_custo']).sum():,.2f}")
    col3.metric("Produtos Baixo Estoque", len(estoque_baixo))
    col4.metric("Categorias", df['categoria'].nunique())
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        estoque_cat = df.groupby('categoria')['quantidade_atual'].sum()
        fig = px.bar(x=estoque_cat.index, y=estoque_cat.values,
                    title="Quantidade por Categoria")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        valor_cat = df.groupby('categoria').apply(lambda x: (x['quantidade_atual'] * x['preco_custo']).sum())
        fig = px.pie(values=valor_cat.values, names=valor_cat.index,
                    title="Valor por Categoria")
        st.plotly_chart(fig, use_container_width=True)

def mostrar_rh(dados):
    st.header("👥 Módulo de Recursos Humanos")
    
    if 'rh' not in dados:
        st.error("Dados de RH não disponíveis")
        return
    
    df = dados['rh']
    
    # Calcular métricas de turnover e absenteísmo
    total_funcionarios = len(df)
    funcionarios_ativos = len(df[df['status'] == 'Ativo'])
    funcionarios_inativos = len(df[df['status'] == 'Inativo'])
    
    # Simular dados de turnover (baseado em funcionários inativos)
    turnover_rate = (funcionarios_inativos / total_funcionarios * 100) if total_funcionarios > 0 else 0
    
    # Simular absenteísmo (dados fictícios baseados em departamentos)
    np.random.seed(42)  # Para dados consistentes
    absenteismo_por_funcionario = np.random.normal(5, 2, len(df))  # Média 5% com desvio 2%
    absenteismo_por_funcionario = np.clip(absenteismo_por_funcionario, 0, 20)  # Entre 0-20%
    df_temp = df.copy()
    df_temp['absenteismo_pct'] = absenteismo_por_funcionario
    absenteismo_medio = df_temp['absenteismo_pct'].mean()
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Funcionários", total_funcionarios)
    col2.metric("Funcionários Ativos", funcionarios_ativos)
    col3.metric("Folha de Pagamento", f"R$ {df['salario'].sum():,.2f}")
    col4.metric("Salário Médio", f"R$ {df['salario'].mean():,.2f}")
    
    # Métricas de Turnover e Absenteísmo
    st.markdown("---")
    st.subheader("📊 Indicadores de Turnover e Absenteísmo")
    
    col1, col2, col3, col4 = st.columns(4)
    
    # Definir cores baseadas nos valores (verde = bom, amarelo = atenção, vermelho = crítico)
    turnover_color = "normal"
    if turnover_rate > 15:
        turnover_color = "inverse"
    elif turnover_rate > 10:
        turnover_color = "off"
    
    absenteismo_color = "normal"
    if absenteismo_medio > 8:
        absenteismo_color = "inverse"
    elif absenteismo_medio > 5:
        absenteismo_color = "off"
    
    col1.metric("📈 Taxa de Turnover", f"{turnover_rate:.1f}%", 
                delta=f"Meta: <10%", delta_color=turnover_color)
    col2.metric("🏠 Absenteísmo Médio", f"{absenteismo_medio:.1f}%", 
                delta=f"Meta: <5%", delta_color=absenteismo_color)
    col3.metric("➡️ Demissões", funcionarios_inativos)
    col4.metric("⏱️ Tempo Médio na Empresa", "2.3 anos")  # Simulado
    
    # Gráficos principais
    col1, col2 = st.columns(2)
    
    with col1:
        func_depto = df.groupby('departamento').size()
        fig = px.bar(x=func_depto.index, y=func_depto.values,
                    title="👥 Funcionários por Departamento",
                    color=func_depto.values, color_continuous_scale='Blues')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        salario_depto = df.groupby('departamento')['salario'].mean()
        fig = px.bar(x=salario_depto.index, y=salario_depto.values,
                    title="💰 Salário Médio por Departamento",
                    color=salario_depto.values, color_continuous_scale='Greens')
        st.plotly_chart(fig, use_container_width=True)
    
    # Análises de Turnover e Absenteísmo
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Análise de Turnover")
        
        # Turnover por departamento (simulado)
        departamentos = df['departamento'].unique()
        turnover_depto = {}
        for dept in departamentos:
            func_dept = len(df[df['departamento'] == dept])
            inativos_dept = len(df[(df['departamento'] == dept) & (df['status'] == 'Inativo')])
            turnover_depto[dept] = (inativos_dept / func_dept * 100) if func_dept > 0 else 0
        
        turnover_df = pd.DataFrame(list(turnover_depto.items()), columns=['Departamento', 'Turnover_%'])
        fig = px.bar(turnover_df, x='Departamento', y='Turnover_%',
                    title="Taxa de Turnover por Departamento",
                    color='Turnover_%', color_continuous_scale='Reds')
        fig.add_hline(y=10, line_dash="dash", line_color="orange", 
                     annotation_text="Meta: 10%")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🏠 Análise de Absenteísmo")
        
        # Absenteísmo por departamento
        absenteismo_depto = df_temp.groupby('departamento')['absenteismo_pct'].mean().reset_index()
        fig = px.bar(absenteismo_depto, x='departamento', y='absenteismo_pct',
                    title="Taxa de Absenteísmo por Departamento",
                    color='absenteismo_pct', color_continuous_scale='Oranges')
        fig.add_hline(y=5, line_dash="dash", line_color="red", 
                     annotation_text="Meta: 5%")
        st.plotly_chart(fig, use_container_width=True)
    
    # Evolução temporal (simulada)
    st.subheader("📅 Evolução Temporal")
    col1, col2 = st.columns(2)
    
    with col1:
        # Simular evolução do turnover nos últimos 12 meses
        meses = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
        turnover_mensal = np.random.normal(turnover_rate, 2, len(meses))
        turnover_mensal = np.clip(turnover_mensal, 0, 25)
        
        evolucao_turnover = pd.DataFrame({
            'Mês': meses.strftime('%Y-%m'),
            'Turnover_%': turnover_mensal
        })
        
        fig = px.line(evolucao_turnover, x='Mês', y='Turnover_%',
                     title="Evolução do Turnover (12 meses)",
                     markers=True)
        fig.add_hline(y=10, line_dash="dash", line_color="orange")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Simular evolução do absenteísmo
        absenteismo_mensal = np.random.normal(absenteismo_medio, 1, len(meses))
        absenteismo_mensal = np.clip(absenteismo_mensal, 0, 15)
        
        evolucao_absenteismo = pd.DataFrame({
            'Mês': meses.strftime('%Y-%m'),
            'Absenteísmo_%': absenteismo_mensal
        })
        
        fig = px.line(evolucao_absenteismo, x='Mês', y='Absenteísmo_%',
                     title="Evolução do Absenteísmo (12 meses)",
                     markers=True, color_discrete_sequence=['orange'])
        fig.add_hline(y=5, line_dash="dash", line_color="red")
        st.plotly_chart(fig, use_container_width=True)
    
    # Tabela detalhada com indicadores por funcionário
    st.subheader("📋 Detalhamento por Funcionário")
    
    # Preparar dados para exibição
    df_detalhado = df_temp[['nome', 'departamento', 'cargo', 'status', 'salario', 'absenteismo_pct']].copy()
    df_detalhado['absenteismo_pct'] = df_detalhado['absenteismo_pct'].round(1)
    df_detalhado = df_detalhado.rename(columns={
        'nome': 'Nome',
        'departamento': 'Departamento', 
        'cargo': 'Cargo',
        'status': 'Status',
        'salario': 'Salário',
        'absenteismo_pct': 'Absenteísmo (%)'
    })
    
    # Filtros para a tabela
    col1, col2 = st.columns(2)
    with col1:
        dept_filtro = st.selectbox("Filtrar por Departamento:", 
                                  ['Todos'] + list(df['departamento'].unique()))
    with col2:
        status_filtro = st.selectbox("Filtrar por Status:", 
                                    ['Todos', 'Ativo', 'Inativo'])
    
    # Aplicar filtros
    df_filtrado = df_detalhado.copy()
    if dept_filtro != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Departamento'] == dept_filtro]
    if status_filtro != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Status'] == status_filtro]
    
    # Destacar funcionários com alto absenteísmo
    def destacar_absenteismo(val):
        if val > 8:
            return 'background-color: #ffcccc'  # Vermelho claro
        elif val > 5:
            return 'background-color: #fff4cc'  # Amarelo claro
        return ''
    
    st.dataframe(
        df_filtrado.style.applymap(destacar_absenteismo, subset=['Absenteísmo (%)']),
        use_container_width=True
    )

def mostrar_producao(dados):
    st.header("🏭 Módulo de Produção")
    
    if 'producao' not in dados:
        st.error("Dados de produção não disponíveis")
        return
    
    df = dados['producao']
    
    # Métricas
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Produzido", f"{df['quantidade_produzida'].sum():,}")
    col2.metric("Eficiência Média", f"{(df['quantidade_produzida'] / df['quantidade_planejada'] * 100).mean():.1f}%")
    col3.metric("Custo Total", f"R$ {df['custo_producao'].sum():,.2f}")
    col4.metric("Qualidade Média", f"{df['qualidade_nota'].mean():.1f}/5")
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        prod_linha = df.groupby('linha_producao')['quantidade_produzida'].sum()
        fig = px.bar(x=prod_linha.index, y=prod_linha.values,
                    title="Produção por Linha")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        eficiencia_turno = df.groupby('turno').apply(
            lambda x: (x['quantidade_produzida'] / x['quantidade_planejada'] * 100).mean()
        )
        fig = px.bar(x=eficiencia_turno.index, y=eficiencia_turno.values,
                    title="Eficiência por Turno (%)")
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()