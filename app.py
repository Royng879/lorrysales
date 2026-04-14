import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="JAC 货车销售工具",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Brand CSS (JAC: red #D0021B, dark-grey #2C2C2C, light-grey #F5F5F5) ─────
st.markdown(
    """
    <style>
    /* ---- global ---- */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #F5F5F5;
        font-family: "Segoe UI", sans-serif;
    }

    /* ---- sidebar ---- */
    [data-testid="stSidebar"] {
        background-color: #2C2C2C;
    }
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    [data-testid="stSidebar"] .stRadio label {
        font-size: 1rem;
        padding: 6px 0;
    }

    /* ---- header banner ---- */
    .jac-header {
        background: linear-gradient(135deg, #D0021B 0%, #8B0000 100%);
        border-radius: 10px;
        padding: 20px 30px;
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        gap: 20px;
    }
    .jac-header h1 {
        color: #FFFFFF;
        margin: 0;
        font-size: 2rem;
        font-weight: 700;
        letter-spacing: 1px;
    }
    .jac-header p {
        color: #FFCCCC;
        margin: 4px 0 0;
        font-size: 0.95rem;
    }

    /* ---- spec card ---- */
    .spec-card {
        background: #FFFFFF;
        border-radius: 10px;
        padding: 24px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border-top: 4px solid #D0021B;
        height: 100%;
    }
    .spec-card h2 {
        color: #D0021B;
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .spec-card .subtitle {
        color: #888;
        font-size: 0.85rem;
        margin-bottom: 18px;
    }
    .spec-row {
        display: flex;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px solid #F0F0F0;
        font-size: 0.93rem;
    }
    .spec-row:last-child { border-bottom: none; }
    .spec-label { color: #555; font-weight: 500; }
    .spec-value { color: #2C2C2C; font-weight: 600; }

    /* ---- selling-point badge ---- */
    .badge {
        display: inline-block;
        background: #FFF0F0;
        border: 1px solid #D0021B;
        color: #D0021B;
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.82rem;
        font-weight: 600;
        margin: 4px 4px 4px 0;
    }

    /* ── comparison table ── */
    .cmp-table {
        width: 100%;
        border-collapse: collapse;
        background: #FFFFFF;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    .cmp-table th {
        background: #D0021B;
        color: #FFFFFF;
        padding: 14px 20px;
        font-size: 1rem;
        text-align: center;
    }
    .cmp-table th.feature-col {
        background: #2C2C2C;
        text-align: left;
    }
    .cmp-table td {
        padding: 12px 20px;
        font-size: 0.92rem;
        color: #2C2C2C;
        border-bottom: 1px solid #F0F0F0;
    }
    .cmp-table tr:last-child td { border-bottom: none; }
    .cmp-table tr:nth-child(even) td { background: #FAFAFA; }
    .cmp-table td.feature-col { font-weight: 600; color: #555; }
    .cmp-table td.highlight { color: #D0021B; font-weight: 700; }

    /* ── whatsapp button ── */
    .wa-box {
        background: #FFFFFF;
        border-radius: 10px;
        padding: 22px 28px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        margin-top: 10px;
    }
    .wa-preview {
        background: #F0FFF4;
        border-left: 4px solid #25D366;
        border-radius: 6px;
        padding: 16px 18px;
        font-family: "Courier New", monospace;
        font-size: 0.88rem;
        color: #1a1a1a;
        white-space: pre-wrap;
        word-break: break-word;
        margin-top: 14px;
    }

    /* hide default streamlit footer */
    footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Data ─────────────────────────────────────────────────────────────────────
MODELS = {
    "N50": {
        "name": "JAC N50",
        "tagline": "轻型城市货运首选",
        "gvw": "5,000 KG",
        "wheels": "4 轮",
        "engine": "HFC4DE1-1C (Euro 4)",
        "displacement": "2,746 cc",
        "horsepower": "122 ps",
        "torque": "285 Nm",
        "fuel_tank": "100 L",
    },
    "N80": {
        "name": "JAC N80",
        "tagline": "中型重载运输利器",
        "gvw": "7,500 KG",
        "wheels": "6 轮",
        "engine": "ISF3.8 (Euro 4)",
        "displacement": "3,760 cc",
        "horsepower": "154 ps",
        "torque": "500 Nm",
        "fuel_tank": "130 L",
    },
}

SELLING_POINTS = [
    "5年或300,000 KM 原厂质保",
    "高达 100,000 KM 免费保养计划",
    "AAM 美国车桥技术",
]

SPEC_LABELS = {
    "gvw": "总车重 (GVW)",
    "wheels": "车轮数量",
    "engine": "引擎型号",
    "displacement": "排量",
    "horsepower": "最大马力",
    "torque": "最大扭矩",
    "fuel_tank": "油箱容量",
}

COMPARISON_ROWS = [
    ("总车重 (GVW)", "gvw", True),
    ("车轮数量", "wheels", False),
    ("引擎型号", "engine", False),
    ("排量", "displacement", False),
    ("最大马力", "horsepower", True),
    ("最大扭矩", "torque", True),
    ("油箱容量", "fuel_tank", False),
]


# ── Helper: WhatsApp copy ─────────────────────────────────────────────────────
def generate_wa_text(model_key: str, salesperson_name: str, phone: str) -> str:
    m = MODELS[model_key]
    text = f"""🚛 *{m['name']} 货车报价单*
━━━━━━━━━━━━━━━━━━
您好！感谢您对 JAC 货车的关注 😊

📋 *车型规格*
• 总车重 (GVW)：{m['gvw']}（{m['wheels']}）
• 引擎型号：{m['engine']}
• 排量：{m['displacement']}
• 最大马力：{m['horsepower']}
• 最大扭矩：{m['torque']}
• 油箱容量：{m['fuel_tank']}

⭐ *购车优势*
✅ {SELLING_POINTS[0]}
✅ {SELLING_POINTS[1]}
✅ {SELLING_POINTS[2]}

💬 如需进一步了解价格、配置或安排试驾，欢迎随时联系我！

👤 销售顾问：{salesperson_name}
📱 WhatsApp / 电话：{phone}

*JAC 货车 — 可靠、耐用、高性价比*"""
    return text


# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        "<div style='text-align:center;padding:10px 0 18px;'>"
        "<span style='font-size:2.4rem;'>🚛</span>"
        "<div style='font-size:1.3rem;font-weight:700;letter-spacing:2px;margin-top:6px;'>JAC 货车</div>"
        "<div style='font-size:0.78rem;color:#aaa;margin-top:2px;'>Malaysia Sales Tool</div>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.divider()
    page = st.radio(
        "导航菜单",
        ["📋 规格查看", "🔍 型号对比"],
        label_visibility="collapsed",
    )
    st.divider()
    st.markdown(
        "<div style='font-size:0.78rem;color:#aaa;text-align:center;'>© 2025 JAC Malaysia</div>",
        unsafe_allow_html=True,
    )

# ── Header banner ─────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="jac-header">
        <div>
            <h1>🚛 JAC 货车销售工具</h1>
            <p>专业 · 可靠 · 高性价比 | JAC Trucks Malaysia</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — 规格查看
# ═══════════════════════════════════════════════════════════════════════════════
if page == "📋 规格查看":

    col_n50, col_n80 = st.columns(2, gap="large")

    for col, model_key in zip([col_n50, col_n80], ["N50", "N80"]):
        m = MODELS[model_key]
        spec_rows_html = "".join(
            f'<div class="spec-row">'
            f'<span class="spec-label">{SPEC_LABELS[k]}</span>'
            f'<span class="spec-value">{m[k]}</span>'
            f'</div>'
            for k in SPEC_LABELS
        )
        badges_html = "".join(f'<span class="badge">✓ {sp}</span>' for sp in SELLING_POINTS)

        with col:
            st.markdown(
                f"""
                <div class="spec-card">
                    <h2>{m['name']}</h2>
                    <div class="subtitle">{m['tagline']}</div>
                    {spec_rows_html}
                    <div style="margin-top:18px;">
                        <div style="font-size:0.8rem;color:#888;font-weight:600;margin-bottom:6px;">共同卖点</div>
                        {badges_html}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # ── WhatsApp generator ───────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 💬 生成 WhatsApp 报价文案")

    with st.container():
        wa_col1, wa_col2, wa_col3 = st.columns([1.5, 2, 2])
        with wa_col1:
            selected_model = st.selectbox("选择型号", ["N50", "N80"], key="spec_model")
        with wa_col2:
            salesperson = st.text_input("销售顾问姓名", value="Ahmad / 阿明", key="spec_name")
        with wa_col3:
            phone = st.text_input("联系电话 / WhatsApp", value="+60 12-345 6789", key="spec_phone")

        if st.button("📲 生成 WhatsApp 报价文案", type="primary", use_container_width=True):
            wa_text = generate_wa_text(selected_model, salesperson, phone)
            st.markdown(
                f'<div class="wa-preview">{wa_text}</div>',
                unsafe_allow_html=True,
            )
            st.text_area(
                "复制文案（点击框内 → Ctrl+A → Ctrl+C）",
                value=wa_text,
                height=300,
                key="wa_copy_spec",
            )
            st.success("✅ 文案已生成！请复制上方内容发送给客户。")

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — 型号对比
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "🔍 型号对比":

    st.markdown("### N50 vs N80 — 核心规格对比")

    rows_html = ""
    for label, key, highlight in COMPARISON_ROWS:
        n50_val = MODELS["N50"][key]
        n80_val = MODELS["N80"][key]
        cls = "highlight" if highlight else ""
        rows_html += (
            f"<tr>"
            f'<td class="feature-col">{label}</td>'
            f'<td style="text-align:center;" class="{cls}">{n50_val}</td>'
            f'<td style="text-align:center;" class="{cls}">{n80_val}</td>'
            f"</tr>"
        )

    st.markdown(
        f"""
        <table class="cmp-table">
            <thead>
                <tr>
                    <th class="feature-col">规格项目</th>
                    <th>N50</th>
                    <th>N80</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
        """,
        unsafe_allow_html=True,
    )

    # ── Selling points comparison ────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### ⭐ 共同卖点")
    sp_cols = st.columns(3)
    icons = ["🛡️", "🔧", "🇺🇸"]
    for i, (col, sp) in enumerate(zip(sp_cols, SELLING_POINTS)):
        with col:
            st.markdown(
                f"""
                <div style="background:#FFFFFF;border-radius:10px;padding:20px;
                            text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.08);
                            border-top:4px solid #D0021B;">
                    <div style="font-size:2rem;">{icons[i]}</div>
                    <div style="font-size:0.92rem;font-weight:600;color:#2C2C2C;
                                margin-top:10px;line-height:1.5;">{sp}</div>
                    <div style="font-size:0.75rem;color:#888;margin-top:4px;">N50 & N80 同享</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # ── Recommendation logic ─────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🎯 智能推荐")
    with st.expander("根据您的需求，帮我推荐合适的型号 ▸"):
        load = st.slider("预计货物重量 (KG)", 500, 7000, 3000, step=250)
        if load <= 4500:
            rec = "N50"
            reason = f"您的货物重量约 {load:,} KG，N50（GVW 5,000 KG）完全满足需求，体积更灵活，适合城市配送。"
        else:
            rec = "N80"
            reason = f"您的货物重量约 {load:,} KG，建议选择 N80（GVW 7,500 KG），载重更充裕，动力更强劲。"

        st.markdown(
            f"""
            <div style="background:#FFF0F0;border-radius:8px;padding:16px 20px;
                        border-left:4px solid #D0021B;margin-top:10px;">
                <span style="font-size:1.1rem;font-weight:700;color:#D0021B;">推荐型号：{rec}</span><br>
                <span style="color:#444;font-size:0.93rem;">{reason}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── WhatsApp generator (comparison page) ────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 💬 生成 WhatsApp 报价文案")

    cwa1, cwa2, cwa3 = st.columns([1.5, 2, 2])
    with cwa1:
        cmp_model = st.selectbox("选择型号", ["N50", "N80"], key="cmp_model")
    with cwa2:
        cmp_name = st.text_input("销售顾问姓名", value="Ahmad / 阿明", key="cmp_name")
    with cwa3:
        cmp_phone = st.text_input("联系电话 / WhatsApp", value="+60 12-345 6789", key="cmp_phone")

    if st.button("📲 生成 WhatsApp 报价文案", type="primary", use_container_width=True, key="cmp_wa_btn"):
        wa_text = generate_wa_text(cmp_model, cmp_name, cmp_phone)
        st.markdown(
            f'<div class="wa-preview">{wa_text}</div>',
            unsafe_allow_html=True,
        )
        st.text_area(
            "复制文案（点击框内 → Ctrl+A → Ctrl+C）",
            value=wa_text,
            height=300,
            key="wa_copy_cmp",
        )
        st.success("✅ 文案已生成！请复制上方内容发送给客户。")
