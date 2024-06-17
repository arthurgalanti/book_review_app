@echo off
cls
:menu
echo Book Sentiment Analyzer
echo =============================
echo 1. Configurar e Inicializar
echo 2. Inicializar
echo 3. Sair
echo =============================
set /p choice=Escolha uma opcao: 

if "%choice%"=="1" goto setup_and_run
if "%choice%"=="2" goto run_only
if "%choice%"=="3" goto exit

echo Escolha invalida, tente novamente.
goto menu

:setup_and_run
cls
echo Configurando Book Sentiment Analyzer

REM Step 1: Creando banco de dados
echo Crando banco de dados...
python init_db.py
if %errorlevel% neq 0 (
    echo Falha ao criar banco de dados.
    pause
    cls
    goto menu
)

REM Step 2: Instalando dependências
echo Instalando dependencias...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Falha ao instalar dependencias.
    pause
    cls
    goto menu
)

goto run_only

:run_only
cls
REM Step 3: Inicializando Book Sentiment Analyzer
echo Inicializando Book Sentiment Analyzer...
python main.py
if %errorlevel% neq 0 (
    echo Falha ao iniciar Book Sentiment Analyzer.
    pause
    cls
    goto menu
)

goto menu

:exit
cls
echo Saindo...
pause
cls
exit
