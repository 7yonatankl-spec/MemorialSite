"""
מהעיזבון – לעשייה · אב טיפוס להדגמה, מוגש דרך Streamlit.

האתר עצמו נמצא ב-site.html (קובץ אחד שכולל עיצוב, קוד, נתונים ותמונות).
כדי לעדכן תוכן: עורכים את data.js בתיקיית האתר המקורית, ומריצים שם:
    node build-single-file.js --demo <נתיב לתיקייה הזו>\\site.html
ואז מעלים את site.html המעודכן ל-GitHub.

הרצה מקומית לבדיקה:   streamlit run app.py
"""
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="מהעיזבון – לעשייה",
    page_icon="🕯️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# האתר תופס את כל המסך: מסתירים את המסגרת של Streamlit ומותחים את האתר לגובה החלון
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"],
      #MainMenu, footer { display: none !important; }
      [data-testid="stMainBlockContainer"], .block-container { padding: 0 !important; max-width: 100% !important; }
      [data-testid="stAppViewContainer"], [data-testid="stMain"] { padding: 0 !important; overflow: hidden; }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      iframe { height: 100vh !important; width: 100% !important; display: block; border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

site = (Path(__file__).parent / "site.html").read_text(encoding="utf-8")

# האתר רץ בתוך מסגרת (iframe). קישורים פנימיים כמו "#/people" היו נפתחים מול הכתובת של Streamlit
# וטוענים את כל העמוד מחדש בתוך המסגרת — לכן מנתבים אותם ידנית בתוך האתר.
NAV_FIX = """
<script>
document.addEventListener("click", (e) => {
  const a = e.target.closest('a[href^="#"]');
  if (!a) return;
  e.preventDefault();
  const href = a.getAttribute("href");
  if (href === "#main") { document.getElementById("main")?.focus(); return; }
  location.hash = href.slice(1);
}, true);
</script>
"""

st.iframe(NAV_FIX + site, height=900)
