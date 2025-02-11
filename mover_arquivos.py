import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ===================== ⚙️ CONFIGURAÇÕES SEGURAS =====================

# 📂 Obtém automaticamente o diretório do usuário
user_home = os.path.expanduser("~")

# 📂 PASTAS QUE SERÃO MONITORADAS (Downloads e Desktop)
pastas_origem = [
    os.path.join(user_home, "Downloads"),
    os.path.join(user_home, "Desktop"),
]

# 📂 PASTA DE DESTINO NO ONEDRIVE
pasta_destino = os.path.join(user_home, "OneDrive", "Área de Trabalho", "JG backup1", "GUITARRA")

# 📜 EXTENSÕES QUE O SCRIPT VAI MONITORAR
extensoes_monitoradas = [".gp", ".gpx", ".gp3", ".gp4", ".gp5"]

# ====================================================================

# 🔧 Criar a pasta de destino se não existir
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

class MoverArquivosHandler(FileSystemEventHandler):
    """Classe que detecta novos arquivos e move automaticamente"""

    def on_created(self, event):
        if event.is_directory:
            return

        arquivo = event.src_path
        _, extensao = os.path.splitext(arquivo)

        if extensao in extensoes_monitoradas:
            print(f"🔄 Arquivo detectado: {arquivo}. Aguardando para garantir que esteja completo...")

            # Espera até que o arquivo esteja completamente salvo
            tempo_espera = 5
            while not os.path.exists(arquivo) or os.path.getsize(arquivo) == 0:
                print(f"⏳ Aguardando o arquivo terminar de ser salvo: {arquivo}")
                time.sleep(tempo_espera)

            time.sleep(3)  # Pequena espera extra para evitar erros

            # Verifica se o arquivo ainda está sendo usado pelo sistema antes de mover
            while True:
                try:
                    with open(arquivo, "rb"):
                        break  # Se conseguir abrir, o arquivo está pronto
                except PermissionError:
                    print(f"⏳ Arquivo ainda em uso. Aguardando...")
                    time.sleep(2)

            # Move o arquivo para o destino
            destino_arquivo = os.path.join(pasta_destino, os.path.basename(arquivo))
            try:
                shutil.move(arquivo, destino_arquivo)
                print(f"✅ Movido: {arquivo} → {pasta_destino}")
            except Exception as e:
                print(f"⚠️ Erro ao mover {arquivo}: {e}")

# 🔍 Configuração do watchdog para múltiplas pastas
observer = Observer()
for pasta in pastas_origem:
    if os.path.exists(pasta):  # Verifica se a pasta existe antes de monitorar
        observer.schedule(MoverArquivosHandler(), pasta, recursive=False)
    else:
        print(f"⚠️ Atenção: A pasta {pasta} não existe!")

observer.start()

print(f"🚀 Monitorando {pastas_origem} para arquivos: {extensoes_monitoradas}...")

try:
    while True:
        time.sleep(1)  # Mantém o script rodando de forma eficiente
except KeyboardInterrupt:
    observer.stop()

observer.join()
