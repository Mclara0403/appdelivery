import streamlit as st
import pandas as pd
import os

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="DiNós Delivery",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "pedidos.csv"


# =========================================================
# IMAGENS
# =========================================================

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1504674900247-0877df9cc836"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_DELIVERY = (
    "https://images.unsplash.com/"
    "photo-1521305916504-4a1121188589"
    "?auto=format&fit=crop&w=1200&q=85"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap'
);

/* =========================================================
FONTE
========================================================= */

html,
body,
[class*="css"] {
    font-family: 'Poppins', sans-serif;
}


/* =========================================================
FUNDO PRINCIPAL
========================================================= */

.stApp {
    background:
        linear-gradient(
            135deg,
            #FFF4E6 0%,
            #FFE3C2 50%,
            #FFD6A3 100%
        );
}


/* =========================================================
ÁREA PRINCIPAL
========================================================= */

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #351A12,
            #54291B
        );

    border-right:
        2px solid #E77B36;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}


/* =========================================================
LOGO
========================================================= */

.logo-title {
    font-size: 28px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-bottom: 5px;
}

.logo-subtitle {
    font-size: 11px;
    font-weight: 700;
    color: #FFBD7A !important;
    letter-spacing: 1px;
}


/* =========================================================
TÍTULOS
========================================================= */

.page-title {
    font-size: 38px;
    font-weight: 800;
    color: #351A12 !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 17px;
    color: #70402D !important;
    margin-bottom: 30px;
}


/* =========================================================
HERO
========================================================= */

.hero-container {
    position: relative;
    height: 430px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;

    background-size: cover;
    background-position: center;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.22);
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            90deg,
            rgba(45,20,12,0.97) 0%,
            rgba(45,20,12,0.86) 45%,
            rgba(45,20,12,0.18) 100%
        );
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 7%;

    transform: translateY(-50%);

    max-width: 580px;
}

.hero-number {
    font-size: 70px;
    font-weight: 800;
    color: #FF9A4D !important;
    line-height: 1;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    color: #FFFFFF !important;

    margin-top: 12px;
    line-height: 1.1;
}

.hero-text {
    font-size: 17px;
    color: #FFF0E4 !important;

    margin-top: 20px;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;

    margin-top: 24px;

    padding: 10px 22px;

    border-radius: 30px;

    background: #E56B25;

    color: #FFFFFF !important;

    font-size: 14px;
    font-weight: 700;
}


/* =========================================================
CARDS
========================================================= */

.info-card {
    background: #FFFFFF;

    border-radius: 22px;

    padding: 28px;

    min-height: 170px;

    border:
        1px solid rgba(229,107,37,0.30);

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

.card-icon {
    font-size: 32px;
}

.card-number {
    font-size: 34px;
    font-weight: 800;

    color: #351A12 !important;

    margin-top: 10px;
}

.card-label {
    font-size: 14px;
    font-weight: 700;

    color: #70402D !important;

    margin-top: 5px;
}


/* =========================================================
CARD ESCURO
========================================================= */

.dark-card {
    background:
        linear-gradient(
            135deg,
            #351A12,
            #5B2C1C
        );

    border-radius: 24px;

    padding: 30px;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.16);
}

.dark-card h2 {
    color: #FFFFFF !important;
    margin-top: 0;
}

.dark-card p {
    color: #FFE7D3 !important;
    line-height: 1.7;
}


/* =========================================================
FORMULÁRIO
========================================================= */

[data-testid="stForm"] {
    background:
        rgba(255,255,255,0.88);

    padding: 30px;

    border-radius: 25px;

    border:
        1px solid #E8B88E;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.08);
}


/* =========================================================
LABELS
========================================================= */

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {
    color: #351A12 !important;

    opacity: 1 !important;

    font-size: 15px !important;

    font-weight: 700 !important;
}


/* =========================================================
INPUTS
========================================================= */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;

    color: #302019 !important;

    -webkit-text-fill-color:
        #302019 !important;

    border:
        2px solid #D58B5A !important;

    border-radius: 12px !important;

    font-size: 16px !important;

    font-weight: 500 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border:
        2px solid #D85B1F !important;

    box-shadow:
        0 0 0 3px rgba(216,91,31,0.15) !important;
}

input::placeholder,
textarea::placeholder {
    color: #76655B !important;
    opacity: 1 !important;
}


/* =========================================================
SELECTBOX
========================================================= */

[data-baseweb="select"] > div {
    background-color: #3B2922 !important;

    border:
        2px solid #C97843 !important;

    border-radius: 12px !important;
}

[data-baseweb="select"] > div * {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;

    opacity: 1 !important;
}

[data-baseweb="select"] input {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[data-baseweb="select"] [class*="singleValue"] {
    color: #FFFFFF !important;
}

[data-baseweb="select"] svg {
    fill: #FFFFFF !important;
    color: #FFFFFF !important;
}

[data-baseweb="select"] > div:hover {
    border-color: #FF9A4D !important;
}


/* =========================================================
MENU DO SELECTBOX
========================================================= */

[data-baseweb="popover"] {
    background-color: #3B2922 !important;
}

[data-baseweb="menu"] {
    background-color: #3B2922 !important;
}

[role="option"] {
    background-color: #3B2922 !important;

    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[role="option"]:hover {
    background-color: #B94F1C !important;

    color: #FFFFFF !important;
}


/* =========================================================
BOTÕES
========================================================= */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background:
        linear-gradient(
            135deg,
            #D9571F,
            #F0803C
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 14px !important;

    min-height: 54px;

    font-family:
        'Poppins', sans-serif !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 18px rgba(217,87,31,0.25);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background:
        linear-gradient(
            135deg,
            #B94112,
            #D96424
        ) !important;

    color: #FFFFFF !important;

    transform:
        translateY(-1px);
}


/* =========================================================
TABELA
========================================================= */

[data-testid="stDataFrame"] {
    background: #FFFFFF;

    border-radius: 18px;

    overflow: hidden;

    border:
        1px solid #E5B187;
}


/* =========================================================
RODAPÉ
========================================================= */

.footer {
    margin-top: 50px;

    text-align: center;

    color: #70402D !important;

    font-size: 14px;

    font-weight: 600;
}


/* =========================================================
RESPONSIVO
========================================================= */

@media (max-width: 768px) {

    .hero-container {
        height: 500px;
    }

    .hero-content {
        left: 8%;
        right: 8%;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-number {
        font-size: 55px;
    }

    .page-title {
        font-size: 30px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES
# =========================================================

def carregar_dados():

    colunas = [
        "Cliente",
        "Restaurante",
        "Pedido",
        "Categoria",
        "Quantidade",
        "Valor",
        "Endereço",
        "Status",
        "Observações"
    ]

    if os.path.exists(ARQUIVO):

        try:

            dados = pd.read_csv(ARQUIVO)

            for coluna in colunas:

                if coluna not in dados.columns:
                    dados[coluna] = ""

            return dados[colunas]

        except Exception:

            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False
    )


# =========================================================
# CARREGAR DADOS
# =========================================================

df = carregar_dados()


# Converter valores

df["Valor"] = pd.to_numeric(
    df["Valor"],
    errors="coerce"
).fillna(0)

df["Quantidade"] = pd.to_numeric(
    df["Quantidade"],
    errors="coerce"
).fillna(0)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
"""
<div class="logo-title">
 🍔 DiNós
</div>

<div class="logo-subtitle">
DELIVERY RÁPIDO E INTELIGENTE
</div>
""",
    unsafe_allow_html=True
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)


menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Dashboard",
        "➕ Novo Pedido",
        "🍔 Pedidos Cadastrados"
    ]
)


st.sidebar.markdown("---")

st.sidebar.caption(
    "DiNós Delivery • 2026"
)


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Dashboard":

    st.markdown(
f"""
<div class="hero-container"
style="background-image: url('{IMAGEM_HERO}');">

<div class="hero-overlay"></div>

<div class="hero-content">

<div class="hero-number">
DiNós
</div>

<div class="hero-title">
Sua comida<br>
do seu jeito
</div>

<div class="hero-text">
Peça suas comidas favoritas, acompanhe seus pedidos
e tenha tudo organizado em um só lugar.
</div>

<div class="hero-badge">
🍔 DELIVERY RÁPIDO
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )


    st.markdown(
"""
<div class="page-title">
📊 Visão geral dos pedidos
</div>

<div class="page-subtitle">
Acompanhe os pedidos realizados no seu delivery
</div>
""",
        unsafe_allow_html=True
    )


    total_pedidos = len(df)

    valor_total = df["Valor"].sum()

    total_itens = df["Quantidade"].sum()


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
🍔
</div>

<div class="card-number">
{total_pedidos}
</div>

<div class="card-label">
PEDIDOS REALIZADOS
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
💰
</div>

<div class="card-number">
R$ {valor_total:,.2f}
</div>

<div class="card-label">
VALOR TOTAL DOS PEDIDOS
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
🍟
</div>

<div class="card-number">
{total_itens:,.0f}
</div>

<div class="card-label">
ITENS PEDIDOS
</div>

</div>
""",
            unsafe_allow_html=True
        )


    st.markdown("<br>", unsafe_allow_html=True)


    coluna1, coluna2 = st.columns([1.1, 1])


    with coluna1:

        st.markdown(
"""
<div class="dark-card">

<h2>
🚀 Delivery na palma da mão
</h2>

<p>
O DiNós Delivery permite organizar seus pedidos
de comida em um único lugar.
</p>

<p>
Cadastre pedidos, consulte clientes, pesquise pedidos
e acompanhe o status de cada entrega de maneira simples,
moderna e profissional.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    with coluna2:

        st.image(
            IMAGEM_DELIVERY,
            use_container_width=True
        )


# =========================================================
# NOVO PEDIDO
# =========================================================

elif menu == "➕ Novo Pedido":

    st.markdown(
"""
<div class="page-title">
➕ Novo pedido
</div>

<div class="page-subtitle">
Registre um novo pedido no DiNós Delivery.
</div>
""",
        unsafe_allow_html=True
    )


    with st.form(
        "cadastro_pedido",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)


        with col1:

            cliente = st.text_input(
                "👤 Nome do cliente"
            )

            restaurante = st.text_input(
                "🏪 Restaurante"
            )

            pedido = st.text_input(
                "🍔 Pedido"
            )

            categoria = st.selectbox(
                "🍴 Categoria",
                [
                    "Hambúrguer",
                    "Pizza",
                    "Comida Brasileira",
                    "Japonesa",
                    "Açaí",
                    "Lanches",
                    "Sobremesa",
                    "Bebidas",
                    "Outro"
                ]
            )


        with col2:

            quantidade = st.number_input(
                "🔢 Quantidade de itens",
                min_value=1,
                value=1,
                step=1
            )

            valor = st.number_input(
                "💰 Valor do pedido",
                min_value=0.0,
                value=0.0,
                step=5.0
            )

            endereco = st.text_input(
                "📍 Endereço de entrega"
            )

            status = st.selectbox(
                "🚴 Status do pedido",
                [
                    "Recebido",
                    "Em preparo",
                    "Saiu para entrega",
                    "Entregue",
                    "Cancelado"
                ]
            )


        observacoes = st.text_area(
            "📝 Observações",
            placeholder="Ex.: Sem cebola, adicionar molho, tocar campainha..."
        )


        cadastrar = st.form_submit_button(
            "🍔 CADASTRAR PEDIDO"
        )


    if cadastrar:

        if (
            cliente.strip()
            and restaurante.strip()
            and pedido.strip()
            and endereco.strip()
        ):

            novo_pedido = pd.DataFrame(
                [{
                    "Cliente": cliente.strip(),
                    "Restaurante": restaurante.strip(),
                    "Pedido": pedido.strip(),
                    "Categoria": categoria,
                    "Quantidade": int(quantidade),
                    "Valor": float(valor),
                    "Endereço": endereco.strip(),
                    "Status": status,
                    "Observações": observacoes.strip()
                }]
            )


            df = pd.concat(
                [
                    df,
                    novo_pedido
                ],
                ignore_index=True
            )


            salvar_dados(df)


            st.success(
                "🍔 Pedido cadastrado com sucesso!"
            )


            st.rerun()


        else:

            st.warning(
                "⚠️ Preencha Cliente, Restaurante, Pedido e Endereço."
            )


# =========================================================
# PEDIDOS CADASTRADOS
# =========================================================

elif menu == "🍔 Pedidos Cadastrados":

    st.markdown(
"""
<div class="page-title">
🍔 Pedidos cadastrados
</div>

<div class="page-subtitle">
Consulte, pesquise e gerencie todos os pedidos.
</div>
""",
        unsafe_allow_html=True
    )


    if df.empty:

        st.markdown(
"""
<div class="dark-card">

<h2>
🍔 Nenhum pedido cadastrado
</h2>

<p>
Ainda não existem pedidos registrados.
Cadastre o primeiro pedido para começar.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    else:

        busca = st.text_input(
            "🔎 Pesquisar pedido",
            placeholder="Digite cliente, restaurante, pedido, endereço ou status..."
        )


        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:

            df_filtrado = df


        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )


        st.markdown("<br>", unsafe_allow_html=True)


        opcoes_pedidos = df.index.tolist()


        pedido_excluir = st.selectbox(
            "🗑️ Selecione um pedido para excluir",
            options=opcoes_pedidos,
            format_func=lambda indice:
                f"{df.loc[indice, 'Cliente']} - "
                f"{df.loc[indice, 'Pedido']} - "
                f"R$ {df.loc[indice, 'Valor']:.2f}"
        )


        if st.button(
            "🗑️ EXCLUIR PEDIDO"
        ):

            df = df.drop(
                pedido_excluir
            )

            df = df.reset_index(
                drop=True
            )


            salvar_dados(df)


            st.success(
                "🍔 Pedido excluído com sucesso!"
            )


            st.rerun()


# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
"""
<div class="footer">

🍔 DiNós Delivery<br>
Comida boa, pedido fácil, entrega rápida.

</div>
""",
    unsafe_allow_html=True
)
