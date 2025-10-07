#!/bin/bash

echo "🛫 AirCatering BI - Setup e Execução"
echo "===================================="

# Navegar para o diretório correto
cd python_dashboard

# Verificar se Python está instalado
if ! command -v python &> /dev/null; then
    echo "❌ Python não encontrado. Por favor, instale o Python 3.8 ou superior."
    exit 1
fi

echo "📦 Instalando dependências..."
pip install -r requirements.txt

echo "🔄 Gerando dados de exemplo..."
python utils/gerar_dados.py

echo "🚀 Iniciando aplicação..."
echo "📱 Acesse: http://localhost:8501"
echo "🛑 Para parar: Ctrl+C"
echo ""

streamlit run app.py