import streamlit as st
import requests

st.set_page_config(page_title="Buscador de Livros", page_icon="📚", layout="centered")

# Título do app
st.title("📚 Buscador de Livros – Google Books API")

# Campo de entrada
nome_livro = st.text_input("Digite o nome do livro:")

# Botão de busca
if st.button("🔍 Buscar"):
    if nome_livro.strip():
        # Faz a requisição à API do Google Books
        url = f"https://www.googleapis.com/books/v1/volumes?q={nome_livro}"
        resposta = requests.get(url)
        dados = resposta.json()

        # Verifica se há resultados
        if "items" in dados and len(dados["items"]) > 0:
            livro = dados["items"][0]["volumeInfo"]

            # Extrai informações
            titulo_livro = livro.get("title", "Título não encontrado")
            autores = livro.get("authors", ["Autor desconhecido"])
            autor_livro = ", ".join(autores)
            sinopse_livro = livro.get("description", "Sinopse não encontrada.")
            imagem = livro.get("imageLinks", {}).get("thumbnail", None)

            # Exibe os resultados
            st.subheader(f"📝 {titulo_livro}")
            st.markdown(f"**👤 Autor(es):** {autor_livro}")

            if imagem:
                st.image(imagem, width=150)

            st.write("### 📖 Sinopse:")
            st.write(sinopse_livro)
        else:
            st.warning("Nenhum livro encontrado com esse nome.")
    else:
        st.error("Por favor, digite o nome de um livro.")
