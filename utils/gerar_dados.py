import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker('pt_BR')

def gerar_dados_vendas(num_registros=1000):
    """Gera dados simulados de vendas"""
    dados = []
    
    for _ in range(num_registros):
        data_venda = fake.date_between(start_date='-2y', end_date='today')
        
        registro = {
            'id': fake.uuid4(),
            'data_venda': data_venda,
            'cliente': fake.company(),
            'vendedor': fake.name(),
            'produto': fake.catch_phrase(),
            'categoria': random.choice(['Alimentação', 'Bebidas', 'Utensílios', 'Serviços']),
            'quantidade': random.randint(1, 100),
            'preco_unitario': round(random.uniform(10, 500), 2),
            'desconto': round(random.uniform(0, 0.2), 2),
            'regiao': random.choice(['Norte', 'Sul', 'Leste', 'Oeste', 'Centro']),
            'canal': random.choice(['Online', 'Loja Física', 'Telefone', 'Representante'])
        }
        
        # Calcular valores
        valor_bruto = registro['quantidade'] * registro['preco_unitario']
        valor_desconto = valor_bruto * registro['desconto']
        registro['valor_total'] = round(valor_bruto - valor_desconto, 2)
        
        dados.append(registro)
    
    return pd.DataFrame(dados)

def gerar_dados_financeiro(num_registros=500):
    """Gera dados simulados financeiros"""
    dados = []
    
    for _ in range(num_registros):
        data_transacao = fake.date_between(start_date='-1y', end_date='today')
        
        registro = {
            'id': fake.uuid4(),
            'data': data_transacao,
            'tipo': random.choice(['Receita', 'Despesa']),
            'categoria': random.choice([
                'Vendas', 'Salários', 'Fornecedores', 'Marketing', 
                'Infraestrutura', 'Impostos', 'Investimentos'
            ]),
            'descricao': fake.sentence(),
            'valor': round(random.uniform(-50000, 100000), 2),
            'conta': random.choice(['Banco Principal', 'Conta Corrente', 'Poupança', 'Investimentos']),
            'status': random.choice(['Confirmado', 'Pendente', 'Cancelado'])
        }
        
        dados.append(registro)
    
    return pd.DataFrame(dados)

def gerar_dados_estoque(num_produtos=200):
    """Gera dados simulados de estoque"""
    dados = []
    
    for _ in range(num_produtos):
        registro = {
            'id': fake.uuid4(),
            'nome_produto': fake.catch_phrase(),
            'categoria': random.choice(['Alimentação', 'Bebidas', 'Utensílios', 'Limpeza']),
            'fornecedor': fake.company(),
            'quantidade_atual': random.randint(0, 1000),
            'quantidade_minima': random.randint(10, 50),
            'preco_custo': round(random.uniform(5, 200), 2),
            'preco_venda': round(random.uniform(10, 400), 2),
            'data_ultima_entrada': fake.date_between(start_date='-6m', end_date='today'),
            'localizacao': f"Setor {random.choice(['A', 'B', 'C'])}-{random.randint(1, 20)}",
            'validade': fake.date_between(start_date='today', end_date='+1y') if random.choice([True, False]) else None
        }
        
        dados.append(registro)
    
    return pd.DataFrame(dados)

def gerar_dados_rh(num_funcionarios=150):
    """Gera dados simulados de RH"""
    dados = []
    
    for _ in range(num_funcionarios):
        data_admissao = fake.date_between(start_date='-5y', end_date='today')
        
        registro = {
            'id': fake.uuid4(),
            'nome': fake.name(),
            'email': fake.email(),
            'cargo': random.choice([
                'Gerente', 'Supervisor', 'Analista', 'Assistente', 
                'Coordenador', 'Especialista', 'Técnico'
            ]),
            'departamento': random.choice([
                'Vendas', 'Marketing', 'Financeiro', 'RH', 
                'TI', 'Operações', 'Produção'
            ]),
            'salario': round(random.uniform(2000, 15000), 2),
            'data_admissao': data_admissao,
            'status': random.choice(['Ativo', 'Férias', 'Licença']),
            'nivel': random.choice(['Júnior', 'Pleno', 'Sênior']),
            'avaliacao': round(random.uniform(1, 5), 1)
        }
        
        dados.append(registro)
    
    return pd.DataFrame(dados)

def gerar_dados_producao(num_registros=300):
    """Gera dados simulados de produção"""
    dados = []
    
    for _ in range(num_registros):
        data_producao = fake.date_between(start_date='-6m', end_date='today')
        
        registro = {
            'id': fake.uuid4(),
            'data_producao': data_producao,
            'produto': fake.catch_phrase(),
            'linha_producao': f"Linha {random.randint(1, 5)}",
            'quantidade_planejada': random.randint(100, 1000),
            'quantidade_produzida': random.randint(80, 1000),
            'tempo_producao_horas': round(random.uniform(2, 24), 2),
            'custo_producao': round(random.uniform(500, 5000), 2),
            'qualidade_nota': round(random.uniform(3, 5), 1),
            'responsavel': fake.name(),
            'turno': random.choice(['Manhã', 'Tarde', 'Noite']),
            'status': random.choice(['Concluído', 'Em Andamento', 'Pausado'])
        }
        
        dados.append(registro)
    
    return pd.DataFrame(dados)

def gerar_dados_empresas_grupo(num_empresas=8):
    """Gera dados simulados de outras empresas do grupo"""
    empresas_nomes = [
        'AirCatering São Paulo',
        'AirCatering Rio de Janeiro', 
        'AirCatering Brasília',
        'AirCatering Salvador',
        'AirCatering Recife',
        'AirCatering Porto Alegre',
        'AirCatering Manaus',
        'AirCatering Fortaleza'
    ]
    
    dados = []
    
    for i, empresa in enumerate(empresas_nomes[:num_empresas]):
        # Gerar dados para os últimos 12 meses
        for mes in range(12):
            data_base = datetime.now() - timedelta(days=mes*30)
            
            # Simular sazonalidade e crescimento
            fator_sazonalidade = 1 + 0.3 * np.sin(2 * np.pi * mes / 12)
            fator_crescimento = 1 + (i * 0.1)  # Empresas maiores baseadas no índice
            
            # Gerar vendas mensais
            vendas_base = random.uniform(500000, 2000000)
            vendas_mes = vendas_base * fator_sazonalidade * fator_crescimento
            
            # Gerar faturamento (um pouco maior que vendas devido a outros serviços)
            faturamento_mes = vendas_mes * random.uniform(1.05, 1.25)
            
            # Calcular margem (entre 15% e 35%)
            custo_mes = faturamento_mes * random.uniform(0.65, 0.85)
            margem_percentual = ((faturamento_mes - custo_mes) / faturamento_mes) * 100
            
            registro = {
                'empresa': empresa,
                'ano_mes': data_base.strftime('%Y-%m'),
                'data': data_base.strftime('%Y-%m-%d'),
                'vendas': round(vendas_mes, 2),
                'faturamento': round(faturamento_mes, 2),
                'custo': round(custo_mes, 2),
                'margem_valor': round(faturamento_mes - custo_mes, 2),
                'margem_percentual': round(margem_percentual, 2),
                'regiao': random.choice(['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']),
                'funcionarios': random.randint(50, 300),
                'clientes_ativos': random.randint(100, 500)
            }
            
            dados.append(registro)
    
    return pd.DataFrame(dados)

def salvar_todos_os_dados():
    """Gera e salva todos os datasets"""
    print("Gerando dados de vendas...")
    df_vendas = gerar_dados_vendas(1000)
    df_vendas.to_csv('data/vendas.csv', index=False)
    
    print("Gerando dados financeiros...")
    df_financeiro = gerar_dados_financeiro(500)
    df_financeiro.to_csv('data/financeiro.csv', index=False)
    
    print("Gerando dados de estoque...")
    df_estoque = gerar_dados_estoque(200)
    df_estoque.to_csv('data/estoque.csv', index=False)
    
    print("Gerando dados de RH...")
    df_rh = gerar_dados_rh(150)
    df_rh.to_csv('data/rh.csv', index=False)
    
    print("Gerando dados de produção...")
    df_producao = gerar_dados_producao(300)
    df_producao.to_csv('data/producao.csv', index=False)
    
    print("Gerando dados das empresas do grupo...")
    df_empresas = gerar_dados_empresas_grupo(8)
    df_empresas.to_csv('data/empresas_grupo.csv', index=False)
    
    print("✅ Todos os dados foram gerados e salvos!")

if __name__ == "__main__":
    salvar_todos_os_dados()