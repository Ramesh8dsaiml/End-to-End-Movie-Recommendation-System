import requests
import streamlit as st
import json
import os
import pandas as pd

# =============================
# LOGIN SYSTEM
# =============================
USER_FILE = "users.json"

def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            json.dump({}, f)
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:
    st.title("🔐 Login / Signup")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    users = load_users()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            if username in users and users[username] == password:
                st.session_state.user = username
                st.rerun()
            else:
                st.error("Invalid login")

    with col2:
        if st.button("Signup"):
            if username in users:
                st.error("User exists")
            else:
                users[username] = password
                save_users(users)
                st.success("Account created")

    st.stop()

# =============================
# CONFIG
# =============================
API_BASE = "https://movie-rec-466x.onrender.com"
TMDB_IMG = "https://image.tmdb.org/t/p/w500"

st.set_page_config(page_title="Movie Recommendation system", page_icon="🎬", layout="wide")

# =============================
# STATE
# =============================
if "view" not in st.session_state:
    st.session_state.view = "home"
if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None
if "watchlist" not in st.session_state:
    st.session_state.watchlist = []
if "analytics" not in st.session_state:
    st.session_state.analytics = {}

# =============================
# ROUTING
# =============================
def goto_home():
    st.session_state.view = "home"
    st.rerun()

def goto_details(tmdb_id):
    st.session_state.selected_tmdb_id = tmdb_id
    st.session_state.view = "details"

    # analytics tracking
    st.session_state.analytics[tmdb_id] = st.session_state.analytics.get(tmdb_id, 0) + 1

    st.rerun()

# =============================
# API
# =============================
def api_get_json(path, params=None):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params, timeout=20)
        return r.json(), None
    except Exception as e:
        return None, str(e)

# =============================
# GRID UI
# =============================
def poster_grid(cards, cols=6):
    if not cards:
        st.info("No movies")
        return

    rows = (len(cards) + cols - 1) // cols
    idx = 0

    for r in range(rows):
        cols_ui = st.columns(cols)
        for c in range(cols):
            if idx >= len(cards):
                break

            m = cards[idx]
            idx += 1

            with cols_ui[c]:
                if m.get("poster_url"):
                    st.image(m.get("poster_url"), use_container_width=True)

                if st.button("Open", key=f"{r}_{c}_{idx}_{m.get('tmdb_id')}"):
                    goto_details(m.get("tmdb_id"))

                st.caption(m.get("title"))

# =============================
# SIDEBAR
# =============================
with st.sidebar:
    st.write(f"👤 {st.session_state.user}")

    if st.button("🏠 Home"):
        goto_home()

    if st.button("⭐ Watchlist"):
        st.session_state.view = "watchlist"

    if st.button("📊 Dashboard"):
        st.session_state.view = "dashboard"

    if st.button("🚪 Logout"):
        st.session_state.user = None
        st.rerun()

    st.markdown("---")

    home_category = st.selectbox(
        "Category",
        ["trending", "popular", "top_rated", "now_playing", "upcoming"]
    )

    grid_cols = st.slider("Columns", 4, 8, 6)

# =============================
# HOME
# =============================
if st.session_state.view == "home":

    st.title("🎬 Movie Recommendation system") 

    typed = st.text_input("Search Movie")

    if typed:
        data, _ = api_get_json("/tmdb/search", {"query": typed})

        cards = []
        if data and "results" in data:
            for m in data["results"]:
                cards.append({
                    "tmdb_id": m["id"],
                    "title": m["title"],
                    "poster_url": TMDB_IMG + m["poster_path"] if m["poster_path"] else None
                })

        poster_grid(cards, grid_cols)

    else:
        data, _ = api_get_json("/home", {"category": home_category})
        if data:
            poster_grid(data, grid_cols)

# =============================
# DETAILS
# =============================
elif st.session_state.view == "details":

    tmdb_id = st.session_state.selected_tmdb_id

    if st.button("← Back"):
        goto_home()

    data, _ = api_get_json(f"/movie/id/{tmdb_id}")

    if not data:
        st.error("Error loading movie")
        st.stop()

    col1, col2 = st.columns([1,2])

    with col1:
        st.image(data.get("poster_url"), use_container_width=True)

    with col2:
        st.title(data.get("title"))
        st.write(data.get("overview"))

        if st.button("⭐ Add to Watchlist"):
            movie = {
                "tmdb_id": tmdb_id,
                "title": data.get("title"),
                "poster_url": data.get("poster_url")
            }
            if movie not in st.session_state.watchlist:
                st.session_state.watchlist.append(movie)
                st.success("Added!")

    # =============================
    # RECOMMENDATIONS
    # =============================
    st.divider()
    st.markdown("### 🎯 Recommended Movies")

    title = data.get("title")

    if title:
        bundle, _ = api_get_json(
            "/movie/search",
            {
                "query": title,
                "tfidf_top_n": 12,
                "genre_limit": 12
            }
        )

        if bundle:
            st.markdown("#### 🔎 Similar Movies")

            tfidf_cards = []
            for x in bundle.get("tfidf_recommendations", []):
                tmdb = x.get("tmdb") or {}
                if tmdb.get("tmdb_id"):
                    tfidf_cards.append({
                        "tmdb_id": tmdb["tmdb_id"],
                        "title": tmdb.get("title"),
                        "poster_url": tmdb.get("poster_url")
                    })

            poster_grid(tfidf_cards, cols=6)

            st.markdown("#### 🎭 More Like This")
            poster_grid(bundle.get("genre_recommendations", []), cols=6)

        else:
            st.warning("No recommendations found")

# =============================
# WATCHLIST
# =============================
elif st.session_state.view == "watchlist":

    st.title("⭐ Watchlist")
    poster_grid(st.session_state.watchlist)

# =============================
# DASHBOARD
# =============================
elif st.session_state.view == "dashboard":

    st.title("📊 Analytics Dashboard")

    if st.session_state.analytics:
        df = pd.DataFrame(
            list(st.session_state.analytics.items()),
            columns=["Movie ID", "Views"]
        ).sort_values(by="Views", ascending=False)

        st.dataframe(df)
        st.bar_chart(df.set_index("Movie ID"))
    else:
        st.info("No data yet")
    
