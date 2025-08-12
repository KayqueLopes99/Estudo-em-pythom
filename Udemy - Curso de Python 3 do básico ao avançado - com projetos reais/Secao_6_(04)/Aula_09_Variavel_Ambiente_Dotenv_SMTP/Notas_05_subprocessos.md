## Usando subprocess para executar e comandos externos
- Um exemplo aqui é usa-lo para converter ppms (juntos) em gif ou video.

> subprocess é um módulo do Python para executar  processos e comandos externos no seu programa.
> O método mais simples para atingir o objetivo é usando subprocess.run().
* Argumentos principais de subprocess.run():
> - stdout, stdin e stderr -> Redirecionam saída, entrada e erros
> - capture_output -> captura a saída e erro para uso posterior
> - text -> Se True, entradas e saídas serão tratadas como texto e automaticamente codificadas ou decodificadas com o conjunto de caracteres padrão da plataforma (geralmente UTF-8).
> - shell -> Se True, terá acesso ao shell do sistema. Ao usar
> shell (True), recomendo enviar o comando e os argumentos juntos.
> - executable -> pode ser usado para especificar o caminho do executável que iniciará o subprocesso.

* Retorno:
> stdout, stderr, returncode e args
: Importante: a codificação de caracteres do Windows pode ser diferente. Tente usar cp1252, cp852, cp850 (ou outros). 
- Linux e  mac, use utf_8.
- Comando de exemplo:
- Windows: ping 127.0.0.1
- Linux/Mac: ping 127.0.0.1 -c 4
> Ex do conceito de ping : ping pong 

## Exemplo de uso do subprocess.run() para executar um comando externo
```python
import subprocess

# Junta todos os arquivos .ppm numerados (frame_001.ppm, frame_002.ppm, ...)
subprocess.run([
    "ffmpeg",
    "-framerate", "30",       # 30 frames por segundo
    "-i", "frame_%03d.ppm",   # padrão dos nomes dos arquivos
    "-c:v", "libx264",        # codec de vídeo
    "-pix_fmt", "yuv420p",    # formato de pixels
    "video.mp4"               # nome do arquivo final
])

# Exemplo de uso do subprocess.run() para executar um comando externo com shell
subprocess.run("ffmpeg -framerate 30 -i frame_%03d.ppm -c:v libx264 -pix_fmt yuv420p video.mp4", shell=True)
```
