import subprocess
import time

#Esse script foi feito para usar o AWSCLI instalado na maquina e com as credentials e configs já setadas na pasta .aws

work_rad = input('Qual a Work do médico?  ')

#aqui você coloca o caminho do bucket
bucket_name = f"nomedobucket/{work_rad}/"

def checar_arquivos(bucket_name):
    try:
        result = subprocess.run(
            ['aws', 's3', 'ls', f's3://{bucket_name}', '--recursive'],
            capture_output=True, text=True, check=True 
        )

        output = result.stdout

        if output.strip():  # Se a saída não estiver vazia
            print(f'O bucket "{bucket_name}" contém os seguintes arquivos:')
            print(output)
        else:
            print(f'O bucket "{bucket_name}" está vazio ou não contém arquivos.')

    except subprocess.CalledProcessError as e:
        print(f'Ocorreu um erro ao executar o comando AWS CLI: {e}')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

def main():
    while True:
        checar_arquivos(bucket_name)
        time.sleep(0.5)

main()