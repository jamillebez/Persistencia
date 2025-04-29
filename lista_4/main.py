import json
import logging
import yaml

def carregar_config(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return yaml.safe_load(arquivo)

def configurar_logging(config):
    logging.basicConfig(
        level=getattr(logging, config['logging']['level']),
        format=config['logging']['format'],
        filename=config['logging']['file'],
        filemode='a',
        encoding='utf-8'
    )

def processar_dados(data_file):
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            logging.info(f"Arquivo JSON '{data_file}' carregado com sucesso.")
            return dados
    except Exception as e:
        logging.error(f"Erro ao carregar o arquivo JSON: {e}")
        return None

def processar_registros(dados):
    for registro in dados:
        if registro.get("age") is None:
            logging.warning(f"Erro no registro: Dado inválido: {registro}")
        else:
            logging.info(f"Processando registro: {registro}")

def main():
    config = carregar_config('config.yaml')
    configurar_logging(config)
    dados = processar_dados(config['data']['file'])
    if dados:
        processar_registros(dados)

if __name__ == "__main__":
    main()
