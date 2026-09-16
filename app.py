import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
import os

# ---------- Page setup ----------
st.set_page_config(
    page_title="PolicyPal — policies, minus the boring",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

DOCS_DIR = "docs"
if not os.path.exists(DOCS_DIR):
    os.makedirs(DOCS_DIR, exist_ok=True)

# ---------- HR contact ----------
HR_PHONE = "+91 8125713172"
HR_EMAIL = "nsaipranavvarma@gmail.com"
HR_CONTACT = f"📞 **{HR_PHONE}**\n\n📧 **{HR_EMAIL}**"

# ---------- Design system (dark neon) ----------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">

<style>
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    #MainMenu, footer, header {visibility: hidden;}

    /* ---- Hero ---- */
    .hero {
        background: linear-gradient(120deg, #7C3AED 0%, #EC4899 45%, #F59E0B 100%);
        border-radius: 24px;
        padding: 2.4rem 2rem;
        text-align: center;
        color: white;
        margin-bottom: 1.2rem;
    }
    .hero h1 {
        font-size: 2.6rem; font-weight: 900; margin: 0;
        color: white !important; letter-spacing: -1px;
    }
    .hero .tag {
        display: inline-block; background: rgba(255,255,255,0.22);
        padding: 4px 14px; border-radius: 999px; font-size: 0.8rem;
        font-weight: 700; margin-bottom: 0.7rem; letter-spacing: 1px;
    }
    .hero p { font-size: 1.05rem; opacity: 0.95; margin: 0.5rem 0 0 0; }

    /* ---- Feature cards (dark neon) ---- */
    .feature-row { display: flex; gap: 0.75rem; margin: 1rem 0 1.4rem 0; }
    .feature {
        flex: 1; border-radius: 18px; padding: 1rem 0.7rem;
        text-align: center; font-size: 0.82rem; font: 600;
    }
    .feature .ico { font-size: 1.7rem; display: block; margin-bottom: 6px; }
    .f1 { background: #2A2140; border: 2px solid #7C3AED; color: #E9D5FF !important; }
    .f2 { background: #3B1D2E; border: 2px solid #EC4899; color: #FBCFE8 !important; }
    .f3 { background: #3A2B10; border: 2px solid #F59E0B; color: #FDE68A !important; }

    /* ---- Values banner ---- */
    .values-title {
        text-align: center; font-size: 1.4rem; font-weight: 800;
        color: #F1F5F9; margin: 1.2rem 0 0.8rem 0;
    }
    .values-row { display: flex; gap: 0.75rem; margin-bottom: 1.6rem; }
    .value-card {
        flex: 1; border-radius: 20px; padding: 1.4rem 1rem;
        color: white; text-align: center;
    }
    .value-card .emo { font-size: 2.2rem; display: block; margin-bottom: 8px; }
    .value-card h3 { margin: 0 0 6px 0; font-size: 1rem; font-weight: 800; color: white !important; }
    .value-card p { margin: 0; font-size: 0.8rem; opacity: 0.95; line-height: 1.4; }
    .v1 { background: linear-gradient(135deg, #059669, #34D399); }
    .v2 { background: linear-gradient(135deg, #2563EB, #60A5FA); }
    .v3 { background: linear-gradient(135deg, #D97706, #FBBF24); }
    .v4 { background: linear-gradient(135deg, #DB2777, #F472B6); }

    /* ---- Chat ---- */
    .stChatMessage {
        border-radius: 18px; border: 1px solid #26263A;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }

    /* ---- Footer ---- */
    .site-footer {
        margin-top: 2.5rem; padding: 1.4rem; text-align: center;
        background: #161622; color: #94A3B8; border-radius: 20px; font-size: 0.82rem;
        border: 1px solid #26263A;
    }
    .site-footer b { color: #E2E8F0; }
</style>
""", unsafe_allow_html=True)

# ---------- Hero ----------
st.markdown("""
<div class="hero">
    <div class="tag">✦ MEET YOUR WORK BESTIE</div>
    <h1>PolicyPal ✨</h1>
    <p>👋 Company policies, minus the boring PDFs.<br>Ask anything — leave, HR, security — get instant answers with receipts.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature-row">
    <div class="feature f1"><span class="ico">⚡</span>Answers in seconds<br>no PDF scrolling</div>
    <div class="feature f2"><span class="ico">🧾</span>Receipts included<br>cites the exact policy</div>
    <div class="feature f3"><span class="ico">🫶</span>Zero judgment<br>ask anything, anytime</div>
</div>
""", unsafe_allow_html=True)

# ---------- Values banner ----------
st.markdown('<div class="values-title">Our people are our roots 🌱</div>', unsafe_allow_html=True)
st.markdown("""
<div class="values-row">
    <div class="value-card v1">
        <span class="emo">🌱</span>
        <h3>Growth</h3>
        <p>Learning budget & real mentorship for every employee. We grow together.</p>
    </div>
    <div class="value-card v2">
        <span class="emo">🤝</span>
        <h3>Trust</h3>
        <p>Flexible hours, hybrid work, and a culture built on ownership.</p>
    </div>
    <div class="value-card v3">
        <span class="emo">🏆</span>
        <h3>Recognition</h3>
        <p>Great work never goes unnoticed — bonuses, shout-outs & perks.</p>
    </div>
    <div class="value-card v4">
        <span class="emo">💚</span>
        <h3>Wellbeing</h3>
        <p>Mental health days, family insurance & zero burnout culture.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("### 🚀 About PolicyPal")
    st.caption("PolicyPal reads your official HR, Leave & Security policies "
               "so you don't have to scroll through PDFs.")
    st.divider()
    st.markdown("### 📞 Need a human?")
    st.caption("If I can't answer your question, connect with HR directly:")
    st.write("📞 " + HR_PHONE)
    st.write("📧 " + HR_EMAIL)
    st.divider()
    st.markdown("### 📚 What I know")
    for fname in sorted(os.listdir(DOCS_DIR)):
        if fname.endswith(".txt"):
            st.write("• " + fname.replace("sop_", "").replace(".txt", "").replace("_", " ").title())
    st.divider()
    if st.button("🔄 Fresh start", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ---------- Knowledge base ----------
@st.cache_resource
def build_index():
    documents = []
    for fname in os.listdir(DOCS_DIR):
        if fname.endswith(".txt"):
            with open(os.path.join(DOCS_DIR, fname), "r", encoding="utf-8") as f:
                text = f.read()
            for i in range(0, len(text), 500):
                chunk = text[i:i+500].strip()
                if chunk:
                    documents.append({"id": f"{fname}_{i}", "text": chunk, "source": fname})
    return documents

@st.cache_resource
def get_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_resource
def get_collection():
    client = chromadb.Client()
    try:
        client.delete_collection("sops")
    except Exception:
        pass
    col = client.get_or_create_collection("sops")
    docs = build_index()
    model = get_model()
    embeddings = model.encode([d["text"] for d in docs]).tolist()
    col.add(
        ids=[d["id"] for d in docs],
        documents=[d["text"] for d in docs],
        embeddings=embeddings,
        metadatas=[{"source": d["source"]} for d in docs],
    )
    return col

def get_llm_response(system_prompt, user_prompt):
    try:
        groq_key = st.secrets["GROQ_API_KEY"]
        from groq import Groq
        client = Groq(api_key=groq_key)
        resp = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return resp.choices[0].message.content
    except (KeyError, FileNotFoundError):
        try:
            import ollama
            resp = ollama.chat(
                model="llama3.2",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
            )
            return resp["message"]["content"]
        except Exception:
            return ("Sorry, I ran into a technical issue. Please connect with HR directly:\n\n" + HR_CONTACT)
    except Exception:
        return ("Sorry, I couldn't fetch an answer just now. Please connect with HR directly:\n\n" + HR_CONTACT)

collection = get_collection()
model = get_model()

# ---------- Chat ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

SYSTEM_PROMPT = (
    "You are PolicyPal, a warm, professional company policy assistant with friendly energy. "
    "Answer ONLY using the provided policy context. Be concise, human and helpful — "
    "like a cool HR friend, never robotic. "
    "If the answer is not in the context, or you are unsure, say so honestly and tell the user "
    f"to connect with HR directly at {HR_PHONE} (mobile) or {HR_EMAIL} (email) for further assistance."
)

# Quick-start chips for first-time users
if not st.session_state.messages:
    st.markdown("**Popular questions 👇**")
    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("🌴 Leave days?"):
            st.session_state.pending_q = "How many paid leave days do I get?"
    with b2:
        if st.button("🕒 Late policy?"):
            st.session_state.pending_q = "What happens if I'm late to work?"
    with b3:
        if st.button("🎣 Phishing?"):
            st.session_state.pending_q = "What should I do about a suspicious email?"

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=("🙋" if msg["role"] == "user" else "✨")):
        st.markdown(msg["content"])
        if "sources" in msg and msg["sources"]:
            with st.expander("🧾 Receipts (sources)"):
                for s in msg["sources"]:
                    st.write("• " + s)

# ---------- Input ----------
question = st.chat_input("Drop your question here... 💬")
if not question and st.session_state.get("pending_q"):
    question = st.session_state.pop("pending_q")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user", avatar="🙋"):
        st.markdown(question)

    q_emb = model.encode([question]).tolist()
    results = collection.query(query_embeddings=q_emb, n_results=3)
    context = "\n\n".join(results["documents"][0])
    sources = []
    for s in results["metadatas"][0]:
 if s and "source" in s and s["source"] not in sources:
            sources.append(s["source"])

    with st.chat_message("assistant", avatar="✨"):
        with st.spinner("Digging through the docs..."):
            answer = get_llm_response(
                SYSTEM_PROMPT,
                f"Context:\n{context}\n\nQuestion: {question}",
            )
            st.markdown(answer)
            if sources:
                with st.expander("🧾 Receipts (sources)"):
                    for s in sources:
                        st.write("• " + s)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer, "sources": sources}
    )

# ---------- Footer ----------
st.markdown(f"""
<div class="site-footer">
    <b>PolicyPal ✨</b> — for official matters contact HR: 📞 {HR_PHONE} · 📧 {HR_EMAIL}<br>
    Made with 💜, caffeine ☕, and very few bugs
</div>
""", unsafe_allow_html=True)

