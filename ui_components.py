"""
Enhanced UI Components for Streamlit App
Replaces inline styling throughout app.py with reusable, professional components
All improvements: KPI cards, status badges, enhanced forms, better tables, breadcrumbs, etc.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple

# Color palette - Professional LinkedIn Blue theme with enhancements
COLORS = {
    'primary': '#0A66C2',      # LinkedIn Blue
    'secondary': '#37B7C3',    # Teal
    'success': '#31A24C',      # Green
    'warning': '#F1C40F',      # Amber
    'danger': '#E74C3C',       # Red
    'info': '#3498DB',         # Light Blue
    'light_bg': '#F5F7FA',     # Very light gray
    'border': '#DDD',          # Light border
    'text_dark': '#1C2C3D',    # Dark text
    'text_light': '#666666',   # Light text
    'hover': '#F0F5FF'         # Hover background
}
# Add Lucide Icons CDN
st.markdown('''
<link rel="stylesheet" href="https://unpkg.com/lucide-static@latest/font/lucide.css">
''', unsafe_allow_html=True)

# ============================================================================
# 1. ENHANCED CSS STYLING - Global improvements
# ============================================================================

def apply_global_styling():
    """Apply enhanced global CSS styling to entire app"""
    css = f"""
    <style>
    /* Root variables */
    :root {{
        --primary-color: {COLORS['primary']};
        --secondary-color: {COLORS['secondary']};
        --success-color: {COLORS['success']};
        --warning-color: {COLORS['warning']};
        --danger-color: {COLORS['danger']};
        --info-color: {COLORS['info']};
        --light-bg: {COLORS['light_bg']};
        --text-dark: {COLORS['text_dark']};
        --text-light: {COLORS['text_light']};
    }}

    /* Improve overall font hierarchy */
    body, .stApp {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
        background-color: #F8FAFB;
        color: {COLORS['text_dark']};
    }}

    /* Better button styling */
    .stButton > button {{
        width: 100%;
        border-radius: 6px;
        font-weight: 600;
        border: none;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        padding: 10px 16px;
        font-size: 14px;
    }}

    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(10, 102, 194, 0.25);
    }}

    .stButton > button:active {{
        transform: translateY(0);
    }}

    /* Primary button (blue) */
    .stButton > button:nth-of-type(1) {{
        background-color: {COLORS['primary']} !important;
        color: white !important;
    }}

    .stButton > button:nth-of-type(1):hover {{
        background-color: #054399 !important;
    }}

    /* Better input styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select,
    .stNumberInput > div > div > input {{
        border: 1.5px solid #DDD !important;
        border-radius: 6px !important;
        padding: 10px 12px !important;
        font-size: 14px !important;
        transition: all 0.2s ease;
    }}

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus,
    .stNumberInput > div > div > input:focus {{
        border-color: {COLORS['primary']} !important;
        box-shadow: 0 0 0 3px rgba(10, 102, 194, 0.1) !important;
        outline: none !important;
    }}

    /* Better form labels */
    .stFormLabel, label {{
        font-weight: 600 !important;
        font-size: 14px !important;
        color: {COLORS['text_dark']} !important;
        margin-bottom: 6px !important;
    }}

    /* Radio button improvements */
    .stRadio > div {{
        flex-direction: row;
        gap: 10px;
    }}

    /* Checkbox improvements */
    .stCheckbox > div {{
        flex-direction: row;
        gap: 8px;
    }}

    /* Better tabs styling */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 2px;
        border-bottom: 2px solid {COLORS['border']};
    }}

    .stTabs [aria-selected="true"] {{
        border-bottom: 3px solid {COLORS['primary']} !important;
        color: {COLORS['primary']} !important;
    }}

    .stTabs [aria-selected="false"] {{
        color: {COLORS['text_light']};
    }}

    /* Better metric/info boxes */
    .metric-box {{
        background: linear-gradient(135deg, #FFFFFF 0%, {COLORS['light_bg']} 100%);
        padding: 20px;
        border-radius: 8px;
        border-left: 4px solid {COLORS['primary']};
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
    }}

    .metric-box:hover {{
        transform: translateY(-4px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.12);
    }}

    /* Status badges */
    .status-badge {{
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}

    .status-active {{ background-color: #E8F5E9; color: {COLORS['success']}; }}
    .status-pending {{ background-color: #FFF3E0; color: {COLORS['warning']}; }}
    .status-rejected {{ background-color: #FFEBEE; color: {COLORS['danger']}; }}
    .status-closed {{ background-color: #F5F5F5; color: #999; }}
    .status-info {{ background-color: #E3F2FD; color: {COLORS['info']}; }}
    .status-success {{ background-color: #E8F5E9; color: {COLORS['success']}; }}
    .status-warning {{ background-color: #FFF3E0; color: {COLORS['warning']}; }}

    /* Better dataframe styling */
    .stDataFrame {{
        border-radius: 8px !important;
        border: 1px solid {COLORS['border']} !important;
        overflow: hidden;
    }}

    /* Better sidebar */
    .stSidebar {{
        background-color: #FFFFFF;
        border-right: 1px solid {COLORS['border']};
    }}

    /* Breadcrumb styling */
    .breadcrumb {{
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 20px;
        font-size: 13px;
        color: {COLORS['text_light']};
    }}

    .breadcrumb-item {{
        color: {COLORS['primary']};
        text-decoration: none;
        cursor: pointer;
    }}

    .breadcrumb-separator {{
        color: {COLORS['text_light']};
    }}

    /* Empty state styling */
    .empty-state {{
        text-align: center;
        padding: 40px 20px;
        color: {COLORS['text_light']};
    }}

    .empty-state-icon {{
        font-size: 48px;
        margin-bottom: 16px;
    }}

    /* Loading spinner */
    .loading {{
        display: inline-block;
        animation: spin 1s linear infinite;
    }}

    @keyframes spin {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
    }}

    /* Mobile responsiveness */
    @media (max-width: 768px) {{
        .stColumn {{
            flex: 1 1 100% !important;
        }}

        .stButton > button {{
            padding: 12px 16px;
            font-size: 16px;
        }}

        .metric-box {{
            padding: 16px;
        }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# ============================================================================
# 2. KPI DASHBOARD CARDS
# ============================================================================

def render_kpi_card_old(title: str, value: Any, metric: str = "", 
                   icon: str = "📊", color: str = "primary", 
                   change_percent: Optional[float] = None):
    """
    Render an enhanced KPI card with metric box styling
    
    Args:
        title: Card title
        value: Main metric value
        metric: Secondary metric text
        icon: Emoji icon
        color: Color type (primary, success, warning, danger, info)
        change_percent: Optional percentage change for trend
    """
    color_map = {
        'primary': COLORS['primary'],
        'success': COLORS['success'],
        'warning': COLORS['warning'],
        'danger': COLORS['danger'],
        'info': COLORS['info']
    }
    
    border_color = color_map.get(color, COLORS['primary'])
    
    html_card = f"""
    <div class="metric-box" style="border-left-color: {border_color};">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div>
                <p style="margin: 0; color: {COLORS['text_light']}; font-size: 13px; font-weight: 500;">
                    {title}
                </p>
                <p style="margin: 8px 0 0 0; color: {COLORS['text_dark']}; font-size: 28px; font-weight: 700;">
                    {value}
                </p>
                {f'<p style="margin: 4px 0 0 0; color: {COLORS["text_light"]}; font-size: 12px;">{metric}</p>' if metric else ''}
                {f'<p style="margin: 8px 0 0 0; color: {border_color}; font-size: 12px; font-weight: 600;">↑ {change_percent}% this month</p>' if change_percent else ''}
            </div>
            <div style="font-size: 32px;">{icon}</div>
        </div>
    </div>
    """
    st.markdown(html_card, unsafe_allow_html=True)


def render_kpi_row(metrics: List[Dict[str, Any]], cols: int = 4):
    """
    Render a row of KPI cards
    
    Args:
        metrics: List of metric dicts with keys: title, value, metric, icon, color
        cols: Number of columns (2, 3, or 4)
    """
    columns = st.columns(cols)
    for i, metric in enumerate(metrics):
        with columns[i % cols]:
            render_kpi_card(
                title=metric.get('title', ''),
                value=metric.get('value', '0'),
                metric=metric.get('metric', ''),
                icon=metric.get('icon', '📊'),
                color=metric.get('color', 'primary'),
                change_percent=metric.get('change_percent')
            )
def render_kpi_card(title, value, icon="📊", delta=None):
    """Render a KPI metric card with inline styles"""
    
    delta_html = ""
    if delta:
        delta_color = "#c62828" if str(delta).startswith("-") else "#1e7e34"
        delta_html = f'<div style="font-size: 0.8rem; color: {delta_color}; margin-top: 0.3rem;">{delta}</div>'
    
    st.markdown(f'''
    <div style="
        background: #ffffff;
        border-radius: 12px;
        padding: 1.2rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        border: 1px solid #e0e0e0;
        text-align: center;
        transition: all 0.3s ease;
    ">
        <div style="font-size: 2rem; margin-bottom: 0.3rem;">{icon}</div>
        <div style="font-size: 2.2rem; font-weight: 800; color: #0a66c2; margin: 0.3rem 0;">{value}</div>
        <div style="font-size: 0.85rem; color: #666; font-weight: 500;">{title}</div>
        {delta_html}
    </div>
    ''', unsafe_allow_html=True)

# ============================================================================
# 3. STATUS BADGES & INDICATORS
# ============================================================================
def render_breadcrumb(items):
    """Render breadcrumb navigation"""
    breadcrumb_items = []
    for i, item in enumerate(items):
        if i == len(items) - 1:
            breadcrumb_items.append(f'<span style="color: #0a66c2; font-weight: 600;">{item}</span>')
        else:
            breadcrumb_items.append(f'<span style="color: #666;">{item}</span>')
    
    breadcrumb_html = ' <span style="color: #ccc; margin: 0 0.3rem;">›</span> '.join(breadcrumb_items)
    
    st.markdown(f'''
    <div style="font-size: 0.85rem; margin-bottom: 1rem;">
        {breadcrumb_html}
    </div>
    ''', unsafe_allow_html=True)

def render_status_badge(status: str) -> str:
    """Return HTML for status badge with proper coloring"""
    status_map = {
        'active': ('status-active', '✓ Active'),
        'pending': ('status-pending', '⏳ Pending'),
        'rejected': ('status-rejected', '✗ Rejected'),
        'closed': ('status-closed', '✗ Closed'),
        'completed': ('status-success', '✓ Completed'),
        'in_progress': ('status-info', '→ In Progress'),
        'approved': ('status-success', '✓ Approved'),
        'scheduled': ('status-info', '📅 Scheduled'),
    }
    
    class_name, display_text = status_map.get(status.lower(), ('status-info', status))
    return f'<span class="status-badge {class_name}">{display_text}</span>'


def render_status_column(df: pd.DataFrame, status_col: str) -> pd.DataFrame:
    """Apply status badge styling to a dataframe column"""
    df[status_col] = df[status_col].apply(render_status_badge)
    return df


# ============================================================================
# 4. ENHANCED FORMS
# ============================================================================

def render_form_section(title: str, description: str = ""):
    """Render a form section header with visual hierarchy"""
    st.markdown(f"""
    <div style="margin-top: 20px; margin-bottom: 16px;">
        <h3 style="margin: 0; color: {COLORS['text_dark']}; font-size: 18px; font-weight: 600;">
            {title}
        </h3>
        {f'<p style="margin: 4px 0 0 0; color: {COLORS["text_light"]}; font-size: 13px;">{description}</p>' if description else ''}
    </div>
    """, unsafe_allow_html=True)


def render_form_field(label: str, required: bool = False, help_text: str = ""):
    """Render a form field label with required indicator"""
    st.markdown(f"""
    <label style="font-weight: 600; color: {COLORS['text_dark']}; font-size: 14px;">
        {label} {' <span style="color: {COLORS["danger"]}; font-weight: 700;">*</span>' if required else ''}
    </label>
    {f'<p style="margin: 2px 0 8px 0; color: {COLORS["text_light"]}; font-size: 12px;">{help_text}</p>' if help_text else ''}
    """, unsafe_allow_html=True)


def render_validation_message(message: str, message_type: str = "error"):
    """Render validation message (error, success, warning, info)"""
    icon_map = {
        'error': '❌',
        'success': '✅',
        'warning': '⚠️',
        'info': 'ℹ️'
    }
    color_map = {
        'error': COLORS['danger'],
        'success': COLORS['success'],
        'warning': COLORS['warning'],
        'info': COLORS['info']
    }
    
    icon = icon_map.get(message_type, 'ℹ️')
    color = color_map.get(message_type, COLORS['info'])
    
    st.markdown(f"""
    <div style="padding: 12px 16px; border-radius: 6px; background-color: rgba({int(color.lstrip('#')[:2], 16)}, {int(color.lstrip('#')[2:4], 16)}, {int(color.lstrip('#')[4:], 16)}, 0.1); border-left: 4px solid {color}; margin: 12px 0;">
        <p style="margin: 0; color: {color}; font-size: 13px; font-weight: 500;">
            {icon} {message}
        </p>
    </div>
    """, unsafe_allow_html=True)


# ============================================================================
# 5. BREADCRUMB NAVIGATION
# ============================================================================

def _render_breadcrumb(items: List[str]):
    """Render breadcrumb navigation"""
    breadcrumb_html = '<div class="breadcrumb">'
    for i, item in enumerate(items):
        if i > 0:
            breadcrumb_html += '<span class="breadcrumb-separator">→</span>'
        breadcrumb_html += f'<span class="breadcrumb-item">{item}</span>'
    breadcrumb_html += '</div>'
    
    st.markdown(breadcrumb_html, unsafe_allow_html=True)


# ============================================================================
# 6. EMPTY STATES
# ============================================================================

def render_empty_state(icon: str = "📭", title: str = "No Data", 
                       description: str = ""):
    """Render an empty state placeholder"""
    st.markdown(f"""
    <div class="empty-state">
        <div class="empty-state-icon">{icon}</div>
        <h3 style="margin: 16px 0 8px 0; color: {COLORS['text_dark']}; font-size: 18px; font-weight: 600;">
            {title}
        </h3>
        {f'<p style="margin: 0; color: {COLORS["text_light"]}; font-size: 14px;">{description}</p>' if description else ''}
    </div>
    """, unsafe_allow_html=True)


# ============================================================================
# 7. ENHANCED DATAFRAME DISPLAY
# ============================================================================

def render_enhanced_dataframe(df: pd.DataFrame, key: str = "", 
                             searchable: bool = True, 
                             sortable: bool = True):
    """
    Render enhanced dataframe with optional search and sort
    
    Args:
        df: DataFrame to display
        key: Unique key for widgets
        searchable: Add search functionality
        sortable: Add sort functionality
    """
    if df.empty:
        render_empty_state(
            icon="📊",
            title="No Data Available",
            description="No records found matching your criteria."
        )
        return
    
    # Add search functionality
    if searchable and len(df) > 0:
        search_term = st.text_input(
            "🔍 Search records",
            key=f"{key}_search",
            placeholder="Type to filter..."
        )
        
        if search_term:
            mask = df.astype(str).apply(
                lambda x: x.str.contains(search_term, case=False, na=False).any(),
                axis=1
            )
            df = df[mask]
    
    # Display dataframe with enhanced styling
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        key=key
    )
    
    # Show record count
    st.caption(f"📌 Showing {len(df)} record(s)")


# ============================================================================
# 8. FEEDBACK COMPONENTS
# ============================================================================

def show_success(message: str, icon: str = "✅"):
    """Show success message"""
    render_validation_message(message, "success")


def show_error(message: str, icon: str = "❌"):
    """Show error message"""
    render_validation_message(message, "error")


def show_warning(message: str, icon: str = "⚠️"):
    """Show warning message"""
    render_validation_message(message, "warning")


def show_info(message: str, icon: str = "ℹ️"):
    """Show info message"""
    render_validation_message(message, "info")


# ============================================================================
# 9. HELPER UTILITIES
# ============================================================================

def format_metric(value: Any, metric_type: str = "number") -> str:
    """Format metric values for display"""
    if metric_type == "currency":
        return f"₹{value:,.2f}" if isinstance(value, (int, float)) else str(value)
    elif metric_type == "percentage":
        return f"{value:.1f}%" if isinstance(value, (int, float)) else str(value)
    elif metric_type == "number":
        return f"{value:,.0f}" if isinstance(value, (int, float)) else str(value)
    return str(value)


def create_two_column_form():
    """Helper to create responsive two-column form layout"""
    col1, col2 = st.columns(2)
    return col1, col2


# Initialize styling on import
apply_global_styling()
