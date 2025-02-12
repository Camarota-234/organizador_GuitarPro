# organizador_GuitarPro
##### Script para enviar direcionar arquivos guitar pro automáticamente para pasta correta

## Instalação e Configuração

#### Clonar repositório

```sh
git clone https://github.com/seu-usuario/organizador_GuitarPro.git
cd organizador_GuitarPro
```

### Instalar dependências

```sh
pip install watchdog
```

### Configurar pasta de destino

Altere a pasta de destino em mover_arquivos.py de acordo com o destino desejado.

```python
pasta_destino = os.path.join(user_home, "OneDrive", "Área de Trabalho", "JG backup1", "GUITARRA")

```