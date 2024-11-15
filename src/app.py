import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card

def configure_interface():
    st.title("Upload de arquivos DIO - Desafio 1 - Azure Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        file_name = uploaded_file.name
        blob_url = upload_blob(uploaded_file, file_name)
    
        if blob_url:
            st.write(f'Arquivo {file_name} enviado com sucesso para o Azure Blob Storage')
            credit_card_info = analyze_credit_card(blob_url)
            
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f'Falha ao enviar o arquivo {file_name} para o Azure Blob Storage')

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada", use_container_width=True)
    st.write("Resultado da validação:")
    if credit_card_info:
        print(credit_card_info)
        st.markdown("<h1 style='color: green;'>Cartão válido</h1>", unsafe_allow_html=True)
        # Corrigido para os campos que são retornados pela função analyze_credit_card
        st.write(f"Nome do Titular: {credit_card_info['card_holder_name']}")
        st.write(f"Número do Cartão: {credit_card_info['card_number']}")
        st.write(f"Data de Validade: {credit_card_info['expiration_date']}")
        st.write(f"Tipo de Cartão: {credit_card_info['card_type']}")
    else:
        st.markdown("<h1 style='color: red;'>Cartão inválido</h1>", unsafe_allow_html=True)
        st.write("Por favor, verifique os dados fornecidos.")

if __name__ == "__main__":
    configure_interface()
