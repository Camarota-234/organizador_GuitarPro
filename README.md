# organizador_GuitarPro
##### Script para enviar direcionar arquivos guitar pro automáticamente para pasta correta

## Instalação e Configuração

#### 1. Clonar repositório

```sh
git clone https://github.com/seu-usuario/organizador_GuitarPro.git
cd organizador_GuitarPro
```

### 2. Instalar dependências

```sh
pip install watchdog
```

### 3. Configurar pasta de destino

Altere a pasta de destino em mover_arquivos.py de acordo com o destino desejado.
Você deve alterar esta linha de código:

```python
pasta_destino = os.path.join(user_home, "OneDrive", "Área de Trabalho", "JG backup1", "GUITARRA")
```

### 4. Executar o script

```sh
python mover_arquivos.py
```


## Como rodar o script ao inicializar o Windows

Em meu caso, criei um arquivo `.bat` para que o script seja inicializado sempre que ligar a máquina. 

### 1.  1. Criar o arquivo .bat

Crie um arquivo chamado `iniciar_mover_arquivos.bat` e adicione:

```bat
@echo off
cd /d "%USERPROFILE%\github\organizador_GuitarPro"
start /min pythonw.exe mover_arquivos.py
exit
```

### 2. Adicionar à inicialização do Windows

1. Pressione `Win + R` e digite:

```makefile
shell:startup
```

2. Copie o arquivo `iniciar_mover_arquivos.bat` para essa pasta.
   
3. Reinicie o PC e o script rodará automaticamente. 