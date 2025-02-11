from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MeuHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Arquivo criado: {event.src_path}")

# Teste para ver se o Observer inicia corretamente
observer = Observer()
observer.schedule(MeuHandler(), ".", recursive=False)

print("🚀 Iniciando o Observer...")
observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()

observer.join()
