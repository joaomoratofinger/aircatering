@echo off
echo 🛫 AirCatering BI - Setup e Execução
echo ====================================

REM Navegar para o diretório correto
cd python_dashboard

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não encontrado. Por favor, instale o Python 3.8 ou superior.
    pause
    exit /b 1
)

echo 📦 Instalando dependências...
pip install -r requirements.txt

echo 🔄 Gerando dados de exemplo...
python utils/gerar_dados.py

echo 🚀 Iniciando aplicação...
echo 📱 Acesse: http://localhost:8501
echo 🛑 Para parar: Ctrl+C
echo.

streamlit run app.py