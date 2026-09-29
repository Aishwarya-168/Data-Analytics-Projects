"""
Bank Term Deposit Campaign Conversion Analysis — Streamlit Dashboard
Run with: streamlit run app.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from pathlib import Path

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Bank Marketing Campaign Analysis",
    page_icon="🏦",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --bg: #071b2b;
        --bg-2: #0d2339;
        --panel: #112d46;
        --panel-2: #163a5b;
        --card: #0f243b;
        --card-soft: #163a5b;
        --text: #eaf6ff;
        --text-soft: #bcd3e6;
        --muted: #9bb6d0;
        --label: #8ecae6;
        --label-strong: #7dd3fc;
        --accent: #7dd3fc;
        --accent-2: #8dd7c7;
        --border: rgba(125, 211, 252, 0.22);
        --navy: #112d46;
        --ink: #071b2b;
        --paper: #f5f9ff;
    }

    /* ---------------------------------------------------------------
       Base background (unchanged colour) + animated aurora layers
       --------------------------------------------------------------- */
    .stApp {
        position: relative;
        isolation: isolate;
        background: linear-gradient(180deg, var(--bg) 0%, var(--bg-2) 100%);
        color: var(--text);
    }

    .stApp > div {
        position: relative;
        z-index: 1;
    }

    .stApp::before,
    .stApp::after {
        content: '';
        position: fixed;
        pointer-events: none;
        z-index: 0;
    }

    /* Layer 1: large, soft colour blooms that slowly drift and rotate */
    .stApp::before {
        inset: -25%;
        background:
            radial-gradient(38% 38% at 18% 24%, rgba(125, 211, 252, 0.34) 0%, transparent 70%),
            radial-gradient(34% 34% at 82% 18%, rgba(141, 215, 199, 0.26) 0%, transparent 70%),
            radial-gradient(44% 44% at 72% 82%, rgba(56, 132, 196, 0.38) 0%, transparent 70%),
            radial-gradient(30% 30% at 24% 80%, rgba(125, 211, 252, 0.24) 0%, transparent 70%);
        will-change: transform;
        animation: aurora-flow 26s ease-in-out infinite alternate;
    }

    /* Layer 2: faint particles + a slow light sweep */
    .stApp::after {
        inset: 0;
        background:
            linear-gradient(
                115deg,
                transparent 0%,
                transparent 42%,
                rgba(125, 211, 252, 0.10) 50%,
                transparent 58%,
                transparent 100%
            ),
            radial-gradient(circle at 15% 20%, rgba(125, 211, 252, 0.08) 0 1px, transparent 2px),
            radial-gradient(circle at 75% 70%, rgba(141, 215, 199, 0.07) 0 1px, transparent 2px);
        background-size: 220% 220%, 180px 180px, 240px 240px;
        animation: dashboard-drift 24s ease-in-out infinite alternate;
    }

    @keyframes aurora-flow {
        0%   { transform: translate3d(0, 0, 0) rotate(0deg) scale(1); }
        33%  { transform: translate3d(12%, -9%, 0) rotate(14deg) scale(1.15); }
        66%  { transform: translate3d(-10%, 11%, 0) rotate(-10deg) scale(1.06); }
        100% { transform: translate3d(9%, 6%, 0) rotate(8deg) scale(1.2); }
    }

    @keyframes dashboard-drift {
        from { background-position: 120% 0, 0 0, 0 0; }
        to   { background-position: -20% 100%, 180px 120px, -240px 160px; }
    }

    @keyframes glass-shine {
        0%   { background-position: 160% 0; }
        100% { background-position: -60% 0; }
    }

    @media (prefers-reduced-motion: reduce) {
        .stApp::before,
        .stApp::after,
        .hero::before {
            animation: none !important;
        }
    }

    [data-testid="stHeader"] {
        background: rgba(7, 27, 43, 0.9);
        border-bottom: 1px solid var(--border);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #091f31 0%, var(--panel) 100%);
        border-right: 1px solid var(--border);
    }

    [data-testid="stSidebar"] * {
        color: var(--text);
    }

    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .stCaptionContainer,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: var(--text);
    }

    [data-testid="stSidebar"] [data-baseweb="select"] > div,
    [data-testid="stSidebar"] [data-baseweb="base-input"],
    [data-testid="stSidebar"] [data-testid="stMultiSelect"] > div,
    [data-testid="stSidebar"] [data-testid="stSlider"] > div,
    [data-testid="stSidebar"] [data-testid="stRadio"] > div,
    [data-testid="stSidebar"] [role="button"],
    [data-testid="stSidebar"] .stSelectbox,
    [data-testid="stSidebar"] .stMultiSelect,
    [data-testid="stSidebar"] .stSlider,
    [data-testid="stSidebar"] .stRadio {
        background: rgba(11, 29, 45, 0.9);
        border: 1px solid var(--border);
        border-radius: 10px;
        color: var(--text);
    }

    [data-testid="stSidebar"] [data-baseweb="select"] span,
    [data-testid="stSidebar"] [data-baseweb="base-input"] input,
    [data-testid="stSidebar"] [role="button"],
    [data-testid="stSidebar"] .stSlider label,
    [data-testid="stSidebar"] .stRadio label,
    [data-testid="stSidebar"] .stCheckbox label {
        color: var(--text);
    }

    [data-testid="stSidebar"] [data-baseweb="tag"] {
        background: #7dd3fc !important;
        color: #071b2b !important;
        border: 1px solid rgba(125, 211, 252, 0.9) !important;
    }

    [data-testid="stSidebar"] [data-baseweb="tag"] span,
    [data-testid="stSidebar"] [data-baseweb="tag"] button,
    [data-testid="stSidebar"] [data-baseweb="tag"] svg,
    [data-testid="stSidebar"] [data-baseweb="tag"] path {
        color: #071b2b !important;
        fill: #071b2b !important;
    }

    [data-testid="stSidebar"] .stRadio input[type="radio"],
    [data-testid="stSidebar"] .stRadio input[type="radio"]:checked,
    [data-testid="stSidebar"] input[type="radio"] {
        accent-color: #7dd3fc !important;
    }

    [data-testid="stSidebar"] button[aria-label*="Clear"],
    [data-testid="stSidebar"] button[title*="clear"],
    [data-testid="stSidebar"] [data-baseweb="select"] svg,
    [data-testid="stSidebar"] [data-baseweb="select"] path,
    [data-testid="stSidebar"] [data-testid="stMultiSelect"] svg,
    [data-testid="stSidebar"] [data-testid="stMultiSelect"] path {
        color: #7dd3fc !important;
        fill: #7dd3fc !important;
    }

    [data-testid="stMetric"] {
        background: linear-gradient(180deg, #112d46 0%, #0c1f31 100%) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 16px !important;
        box-shadow: 0 10px 22px rgba(3, 12, 20, 0.28) !important;
        padding: 20px 18px 18px !important;
        min-height: 120px !important;
        color: #ffffff !important;
    }

    [data-testid="stMetric"] > div,
    [data-testid="stMetric"] > div > div,
    [data-testid="stMetric"] > div > div > div {
        background: transparent !important;
    }

    [data-testid="stMetricLabel"] {
        color: #ffffff !important;
        font-size: 0.76rem !important;
        letter-spacing: 0.12em !important;
        line-height: 1.4 !important;
        text-transform: uppercase !important;
        opacity: 1 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 700 !important;
    }

    [data-testid="stMetricValue"] {
        color: #dfeaf5 !important;
        font-size: 2.1rem !important;
        line-height: 1.1 !important;
        font-family: 'Space Grotesk', 'Aptos Display', sans-serif !important;
        font-weight: 700 !important;
        margin-top: 10px !important;
    }

    h1, h2, h3 {
        color: var(--text);
    }

    .hero {
        background: linear-gradient(135deg, #0d2340 0%, #153a5d 52%, #1a456b 100%);
        box-shadow: 0 16px 32px rgba(3, 9, 15, 0.38);
    }

    .hero-side {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(126, 200, 234, 0.3);
    }

    button[data-baseweb="tab"] {
        color: var(--muted);
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: var(--accent);
    }

    h1, h2, h3, [data-testid="stMetricLabel"] {
        font-family: 'Space Grotesk', 'Aptos Display', sans-serif;
        color: var(--ink);
    }

    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.75);
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 18px 20px;
        box-shadow: 0 8px 22px rgba(23, 34, 54, 0.06);
    }

    [data-testid="stMetricValue"] {
        color: var(--navy);
        font-family: 'Space Grotesk', 'Aptos Display', sans-serif;
    }

    [data-testid="stMetricLabel"] {
        color: var(--muted);
        font-size: 0.78rem;
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }

    .hero {
        position: relative;
        overflow: hidden;
        display: flex;
        justify-content: space-between;
        gap: 28px;
        margin: 22px 0 24px;
        padding: 34px 38px;
        border-radius: 22px;
        background:
            linear-gradient(116deg, rgba(23, 44, 73, 0.98), rgba(27, 59, 83, 0.95)),
            var(--navy);
        box-shadow: 0 18px 38px rgba(23, 44, 73, 0.18);
    }

    .hero::after {
        content: '';
        position: absolute;
        width: 360px;
        height: 360px;
        right: -120px;
        top: -170px;
        border: 1px solid rgba(184, 223, 211, 0.35);
        border-radius: 50%;
        box-shadow: 0 0 0 28px rgba(184, 223, 211, 0.07), 0 0 0 56px rgba(184, 223, 211, 0.05);
    }

    .hero-copy {
        position: relative;
        z-index: 1;
        max-width: 720px;
    }

    .eyebrow {
        margin-bottom: 14px;
        color: var(--mint);
        font-family: 'DM Sans', sans-serif;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
    }

    .hero h1 {
        margin: 0;
        color: #ffffff;
        font-family: 'Space Grotesk', 'Aptos Display', sans-serif;
        font-size: clamp(2rem, 4vw, 3.65rem);
        line-height: 0.98;
        letter-spacing: -0.03em;
    }

    .hero p {
        max-width: 580px;
        margin: 18px 0 0;
        color: #d9e5e8;
        font-family: 'DM Sans', sans-serif;
        font-size: 1rem;
        line-height: 1.55;
    }

    .hero-side {
        position: relative;
        z-index: 1;
        align-self: flex-end;
        min-width: 190px;
        padding: 16px 18px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 14px;
        background: rgba(255, 255, 255, 0.08);
        color: #ffffff;
        font-family: 'DM Sans', sans-serif;
    }

    .hero-side strong {
        display: block;
        margin-top: 6px;
        color: #ffffff;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.25rem;
    }

    .hero-side span {
        color: #b9ced3;
        font-size: 0.76rem;
    }

    .campaign-note {
        margin-top: 26px;
        padding: 22px 24px;
        border-left: 4px solid #7ec8ea;
        border-radius: 0 16px 16px 0;
        background: linear-gradient(135deg, rgba(11, 31, 48, 0.96), rgba(18, 43, 67, 0.96));
        box-shadow: 0 12px 28px rgba(5, 13, 21, 0.28);
    }

    .campaign-note .title {
        font-family: 'Space Grotesk', sans-serif;
        color: #edf6ff;
        font-size: 1.15rem;
        font-weight: 700;
        letter-spacing: -0.02em;
    }

    .campaign-note .body {
        margin-top: 7px;
        color: #dfeaf5;
        font-family: 'DM Sans', sans-serif;
        line-height: 1.6;
    }

    .campaign-note .body strong {
        color: #7ec8ea;
    }

    div[data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid var(--border);
    }

    button[data-baseweb="tab"] {
        color: #dfeaf5 !important;
        font-family: 'DM Sans', sans-serif;
        font-weight: 600;
        background: transparent;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #ffffff !important;
        border-bottom: 2px solid #7dd3fc;
    }

    /* ---------------------------------------------------------------
       Glassmorphism surfaces (translucent + frosted, same palette).
       Placed after the rules above so these take precedence.
       --------------------------------------------------------------- */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(9, 31, 49, 0.80) 0%, rgba(17, 45, 70, 0.74) 100%);
        -webkit-backdrop-filter: blur(22px) saturate(140%);
        backdrop-filter: blur(22px) saturate(140%);
        border-right: 1px solid rgba(255, 255, 255, 0.10);
        box-shadow: inset -1px 0 0 rgba(125, 211, 252, 0.08);
    }

    [data-testid="stMetric"] {
        background: linear-gradient(145deg, rgba(22, 58, 91, 0.58) 0%, rgba(12, 31, 49, 0.46) 100%) !important;
        -webkit-backdrop-filter: blur(18px) saturate(160%);
        backdrop-filter: blur(18px) saturate(160%);
        border: 1px solid rgba(255, 255, 255, 0.14) !important;
        box-shadow:
            0 14px 34px rgba(3, 12, 20, 0.34),
            inset 0 1px 0 rgba(255, 255, 255, 0.14),
            inset 0 -1px 0 rgba(125, 211, 252, 0.05) !important;
    }

    .hero {
        background:
            linear-gradient(135deg, rgba(13, 35, 64, 0.72) 0%, rgba(21, 58, 93, 0.60) 52%, rgba(26, 69, 107, 0.52) 100%);
        -webkit-backdrop-filter: blur(20px) saturate(150%);
        backdrop-filter: blur(20px) saturate(150%);
        border: 1px solid rgba(255, 255, 255, 0.14);
        box-shadow:
            0 18px 40px rgba(3, 9, 15, 0.38),
            inset 0 1px 0 rgba(255, 255, 255, 0.16);
    }

    /* Light sweep across the hero glass */
    .hero::before {
        content: '';
        position: absolute;
        inset: 0;
        pointer-events: none;
        background: linear-gradient(
            110deg,
            transparent 30%,
            rgba(255, 255, 255, 0.13) 48%,
            transparent 66%
        );
        background-size: 250% 100%;
        animation: glass-shine 9s ease-in-out infinite;
    }

    .hero-side {
        background: rgba(255, 255, 255, 0.07);
        -webkit-backdrop-filter: blur(14px);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.12);
    }

    .campaign-note {
        background: linear-gradient(135deg, rgba(11, 31, 48, 0.62), rgba(18, 43, 67, 0.52));
        -webkit-backdrop-filter: blur(16px) saturate(150%);
        backdrop-filter: blur(16px) saturate(150%);
        border-top: 1px solid rgba(255, 255, 255, 0.10);
        border-right: 1px solid rgba(255, 255, 255, 0.08);
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow:
            0 12px 28px rgba(5, 13, 21, 0.30),
            inset 0 1px 0 rgba(255, 255, 255, 0.10);
    }

    [data-testid="stImage"] img {
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.10);
        box-shadow: 0 10px 26px rgba(3, 12, 20, 0.30);
    }

    @media (max-width: 700px) {
        .hero {
            display: block;
            padding: 28px 24px;
        }

        .hero-side {
            margin-top: 24px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

PROJECT_DIR = Path(__file__).parent
DATA_PATH = next(
    (
        path
        for path in (
            PROJECT_DIR / "data" / "bank-full.csv",
            PROJECT_DIR / "bank-full.csv",
        )
        if path.exists()
    ),
    PROJECT_DIR / "data" / "bank-full.csv",
)

AGE_BINS = [17, 30, 45, 60, 100]
AGE_LABELS = ["18-30", "31-45", "46-60", "60+"]

CAMPAIGN_BINS = [0, 1, 3, 6, 100]
CAMPAIGN_LABELS = ["1", "2-3", "4-6", "7+"]


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    # The UCI file is semicolon-delimited. Fall back to comma if needed.
    try:
        df = pd.read_csv(path, sep=";")
        if df.shape[1] == 1:
            raise ValueError("wrong delimiter")
    except Exception:
        df = pd.read_csv(path, sep=",")

    df.columns = [c.strip().lower() for c in df.columns]
    df = df.replace("unknown", "others")

    df["y_flag"] = (df["y"].str.lower() == "yes").astype(int)

    df["age_group"] = pd.cut(df["age"], bins=AGE_BINS, labels=AGE_LABELS)

    df["campaign_group"] = pd.cut(
        df["campaign"], bins=CAMPAIGN_BINS, labels=CAMPAIGN_LABELS
    )

    df["previously_contacted"] = np.where(df["pdays"] == -1, "Never", "Yes")

    # Keep month in calendar order rather than alphabetical
    month_order = [
        "jan", "feb", "mar", "apr", "may", "jun",
        "jul", "aug", "sep", "oct", "nov", "dec",
    ]
    df["month"] = pd.Categorical(
        df["month"].str.lower(), categories=month_order, ordered=True
    )

    return df


def conversion_rate(df: pd.DataFrame, group_col: str) -> pd.Series:
    return (
        df.groupby(group_col, observed=True)["y_flag"]
        .mean()
        .sort_values(ascending=False)
        * 100
    )


def bar_chart(series: pd.Series, title: str, xlabel: str, sort_index=False, horizontal=False):
    if sort_index:
        series = series.sort_index()
    fig, ax = plt.subplots(figsize=(6, 3.5))
    fig.patch.set_facecolor("#081823")
    ax.set_facecolor("#0c1f30")
    if horizontal:
        ax.barh(series.index.astype(str), series.values, color="#8ecae6")
        ax.set_xlabel("Conversion rate (%)")
        ax.invert_yaxis()
    else:
        ax.bar(series.index.astype(str), series.values, color="#8ecae6")
        ax.set_ylabel("Conversion rate (%)")
        ax.set_xlabel(xlabel)
        plt.xticks(rotation=40, ha="right")
    ax.set_title(title, color="#edf6ff")
    ax.xaxis.label.set_color("#bcd3e6")
    ax.yaxis.label.set_color("#bcd3e6")
    ax.tick_params(axis='x', colors="#dfeaf5")
    ax.tick_params(axis='y', colors="#dfeaf5")
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Load data (with friendly error if the file isn't there yet)
# ---------------------------------------------------------------------------
if not DATA_PATH.exists():
    st.title("🏦 Bank Term Deposit Campaign Analysis")
    st.error(
        f"Dataset not found at `{DATA_PATH}`.\n\n"
        "Download **bank-full.csv** from the UCI Bank Marketing dataset "
        "(https://archive.ics.uci.edu/dataset/222/bank+marketing) and place it "
        "inside the `data/` folder next to `app.py`, then rerun the app."
    )
    st.stop()

df = load_data(DATA_PATH)

# ---------------------------------------------------------------------------
# Page navigation
# ---------------------------------------------------------------------------
st.sidebar.markdown("### Workspace")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Campaign analysis"],
    label_visibility="collapsed",
)

if page == "Home":
    st.markdown(
        """
        <section class="hero">
            <div class="hero-copy">
                <div class="eyebrow">Bank marketing / campaign intelligence</div>
                <h1>Make every campaign conversation count.</h1>
                <p>Start with the big picture, then move into the filtered analysis to understand who converts and where campaign effort pays off.</p>
            </div>
            <div class="hero-side">
                <span>DATASET STATUS</span>
                <strong>Ready to explore</strong>
                <span>UCI Bank Marketing dataset</span>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### Campaign snapshot")
    home_k1, home_k2, home_k3, home_k4 = st.columns(4)
    home_k1.metric("Total clients", f"{len(df):,}")
    home_k2.metric("Subscriptions", f"{int(df['y_flag'].sum()):,}")
    home_k3.metric("Overall conversion", f"{df['y_flag'].mean() * 100:.1f}%")
    home_k4.metric("Average balance", f"€{df['balance'].mean():,.0f}")

    st.markdown(
        """
        <div class="campaign-note">
            <div class="title">Your analysis workspace is ready.</div>
            <div class="body">Choose <strong>Campaign analysis</strong> in the sidebar to open the filters, conversion trends, customer segments, campaign effectiveness, and downloadable data explorer.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.stop()

# ---------------------------------------------------------------------------
# Sidebar filters
# ---------------------------------------------------------------------------
st.sidebar.header("Filters")

job_options = sorted(df["job"].unique())
selected_jobs = st.sidebar.multiselect("Role", job_options, default=job_options)

edu_options = sorted(df["education"].unique())
selected_edu = st.sidebar.multiselect("Education", edu_options, default=edu_options)

marital_options = sorted(df["marital"].unique())
selected_marital = st.sidebar.multiselect(
    "Marital status", marital_options, default=marital_options
)

age_range = st.sidebar.slider(
    "Age range", int(df["age"].min()), int(df["age"].max()),
    (int(df["age"].min()), int(df["age"].max())),
)

contact_options = sorted(df["contact"].unique())
selected_contact = st.sidebar.multiselect(
    "Contact channel", contact_options, default=contact_options
)

filtered = df[
    df["job"].isin(selected_jobs)
    & df["education"].isin(selected_edu)
    & df["marital"].isin(selected_marital)
    & df["contact"].isin(selected_contact)
    & df["age"].between(age_range[0], age_range[1])
]

st.sidebar.markdown("---")
st.sidebar.caption(f"{len(filtered):,} of {len(df):,} clients match the current filters")

# ---------------------------------------------------------------------------
# Header + KPIs
# ---------------------------------------------------------------------------
st.markdown(
    f"""
    <section class="hero">
        <div class="hero-copy">
            <div class="eyebrow">Bank marketing / campaign intelligence</div>
            <h1>Find the signals behind every conversation.</h1>
            <p>Explore who converts, when momentum builds, and where campaign effort pays off across the filtered audience.</p>
        </div>
        <div class="hero-side">
            <span>LIVE FILTERED VIEW</span>
            <strong>{len(filtered):,} clients</strong>
            <span>updating across all tabs</span>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

if filtered.empty:
    st.warning("No clients match the current filter combination. Adjust the sidebar filters.")
    st.stop()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Clients contacted", f"{len(filtered):,}")
k2.metric("Conversions", f"{int(filtered['y_flag'].sum()):,}")
k3.metric("Conversion rate", f"{filtered['y_flag'].mean() * 100:.1f}%")
k4.metric("Avg. account balance", f"€{filtered['balance'].mean():,.0f}")

st.markdown("---")

# ---------------------------------------------------------------------------
# Tabs
# ---------------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["Overview", "Segment Deep-Dive", "Campaign Effectiveness", "Data Explorer"]
)

# --- Tab 1: Overview ---------------------------------------------------
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        monthly = conversion_rate(filtered, "month")
        fig, ax = plt.subplots(figsize=(6, 3.5))
        monthly_sorted = monthly.sort_index()
        ax.plot(monthly_sorted.index.astype(str), monthly_sorted.values, marker="o", color="#2E86AB")
        ax.set_title("Monthly conversion rate")
        ax.set_ylabel("Conversion rate (%)")
        plt.xticks(rotation=40, ha="right")
        fig.tight_layout()
        st.pyplot(fig)

    with col2:
        channel = conversion_rate(filtered, "contact")
        st.pyplot(bar_chart(channel, "Conversion rate by contact channel", "Channel"))

    col3, col4 = st.columns(2)
    with col3:
        job_conv = conversion_rate(filtered, "job")
        st.pyplot(bar_chart(job_conv, "Conversion rate by job", "", horizontal=True))
    with col4:
        edu_conv = conversion_rate(filtered, "education")
        st.pyplot(bar_chart(edu_conv, "Conversion rate by education", "Education"))

# --- Tab 2: Segment Deep-Dive -------------------------------------------
with tab2:
    col1, col2 = st.columns(2)

    with col1:
        age_conv = conversion_rate(filtered, "age_group")
        st.pyplot(bar_chart(age_conv, "Conversion rate by age group", "Age group", sort_index=True))

    with col2:
        loan_status = filtered.assign(
            loan_status=lambda d: np.where(
                (d["housing"] == "yes") | (d["loan"] == "yes"), "Has a loan", "No loan"
            )
        )
        loan_conv = conversion_rate(loan_status, "loan_status")
        st.pyplot(bar_chart(loan_conv, "Conversion rate by loan status", "Loan status"))

    st.subheader("Account balance by outcome")
    fig, ax = plt.subplots(figsize=(8, 3.5))
    data_to_plot = [
        filtered.loc[filtered["y"] == "no", "balance"],
        filtered.loc[filtered["y"] == "yes", "balance"],
    ]
    ax.boxplot(
        data_to_plot,
        tick_labels=["Did not subscribe", "Subscribed"],
        showfliers=False,
    )
    ax.set_ylabel("Balance (€)")
    ax.set_title("Balance distribution by subscription outcome (outliers hidden)")
    fig.tight_layout()
    st.pyplot(fig)

    st.subheader("Top converting job × month combinations")
    combo = (
        filtered.groupby(["job", "month"], observed=True)["y_flag"]
        .agg(["mean", "count"])
        .rename(columns={"mean": "conversion_rate", "count": "n_clients"})
    )
    combo = combo[combo["n_clients"] >= 20]  # ignore tiny, noisy groups
    combo["conversion_rate"] = (combo["conversion_rate"] * 100).round(1)
    combo = combo.sort_values("conversion_rate", ascending=False).head(10)
    st.dataframe(combo.reset_index(), use_container_width=True)

# --- Tab 3: Campaign Effectiveness --------------------------------------
with tab3:
    col1, col2 = st.columns(2)

    with col1:
        camp_conv = conversion_rate(filtered, "campaign_group")
        st.pyplot(
            bar_chart(camp_conv, "Conversion rate vs. number of contacts", "Contacts made", sort_index=True)
        )

    with col2:
        poutcome_conv = conversion_rate(filtered, "poutcome")
        st.pyplot(bar_chart(poutcome_conv, "Conversion rate by previous campaign outcome", "Previous outcome"))

    prev_contact_conv = conversion_rate(filtered, "previously_contacted")
    st.pyplot(
        bar_chart(
            prev_contact_conv,
            "Conversion rate: previously contacted vs. never",
            "Previously contacted",
        )
    )

# --- Tab 4: Data Explorer -------------------------------------------------
with tab4:
    st.subheader("Filtered raw data")
    st.dataframe(filtered.drop(columns=["y_flag"]), use_container_width=True)
    st.download_button(
        "Download filtered data as CSV",
        filtered.drop(columns=["y_flag"]).to_csv(index=False).encode("utf-8"),
        file_name="filtered_bank_marketing.csv",
        mime="text/csv",
    )