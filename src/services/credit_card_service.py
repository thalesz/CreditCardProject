import re
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from utils.Config import Config

def analyze_credit_card(card_url):
    try:
        # Configurações do cliente Azure
        credential = AzureKeyCredential(Config.KEY)
        document_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)
        
        # Inicia a análise do documento com o URL da imagem do cartão de crédito
        card_info = document_client.begin_analyze_document(
            "prebuilt-creditCard", {"urlSource": card_url}
        )
        
        # Aguarda o resultado da análise
        result = card_info.result()
        
        # # Verificar e exibir o resultado completo para depuração
        # print("content:", result.content)

        if result.content:
            content = result.content

            # Expressões regulares para encontrar os dados no texto
            card_number = re.search(r'\d{4} \d{4} \d{4} \d{4}', content)  # Número do cartão
            expiration_date = re.search(r'\d{2}/\d{2}', content)  # Data de expiração
            card_holder_name = re.search(r'([A-Za-z]+\s[A-Za-z]+)', content)  # Nome do titular
            card_type = re.search(r'(mastercard|visa|amex|discover)', content, re.IGNORECASE)  # Tipo do cartão

            # Se os dados forem encontrados, extrair seus valores
            card_number_value = card_number.group(0) if card_number else "Não encontrado"
            expiration_date_value = expiration_date.group(0) if expiration_date else "Não encontrado"
            card_holder_name_value = card_holder_name.group(0) if card_holder_name else "Não encontrado"
            card_type_value = card_type.group(0).capitalize() if card_type else "Não encontrado"
            
            # Exibindo os valores extraídos
            print("Campos extraídos do documento:")
            print(f" Número do Cartão: {card_number_value}")
            print(f" Titular do Cartão: {card_holder_name_value}")
            print(f" Data de Expiração: {expiration_date_value}")
            print(f" Tipo de Cartão: {card_type_value}")
            
            return {
                'card_number': card_number_value,
                'card_holder_name': card_holder_name_value,
                'expiration_date': expiration_date_value,
                'card_type': card_type_value
            }
        else:
            print("Nenhum conteúdo encontrado na resposta.")
            return None
            
    except Exception as e:
        print(f"Erro ao analisar o cartão de crédito: {e}")
        return None

# Exemplo de chamada da função com um URL de imagem
card_url = "URL_da_imagem_do_cartao_aqui"
result = analyze_credit_card(card_url)

if result:
    # Utilize os dados extraídos do cartão de crédito, conforme necessário
    print(f"Dados extraídos: {result}")
else:
    print("Falha na análise do cartão.")
