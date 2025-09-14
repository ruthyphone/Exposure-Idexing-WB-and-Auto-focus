import re
import streamlit as st

st.set_page_config(page_title="Exposure Indexing + FX6 Guide", page_icon="🎥", layout="wide")
st.title("Exposure Indexing (EI) & Sony FX6 Advanced Settings")
st.caption("Numbered/lettered/roman lines are checkboxes. Wrapped/continued lines keep the correct hanging indent.")

# ---------- YOUR TEXT (VERBATIM) ----------
FULL_TEXT = """<PASTE YOUR SAME VERBATIM TEXT HERE>"""

# ---------- CSS (marker + text grid with hanging indent) ----------
st.markdown("""
<style>
.step-row { display:flex; align-items:flex-start; gap:.5rem; margin:.15rem 0; }
.step-row .cb-col { flex:0 0 auto; width:1.6rem; padding-top:.15rem; }
.step-row .text-col { flex:1 1 auto; }

/* marker+content grid so wraps align under the first line */
.step { display:grid; grid-template-columns: 2.2em 1fr; column-gap:.5em; }
.step .marker { font-weight:700; }
.step .content { line-height:1.5; }

/* logical indent levels for subitems */
.level-0 { margin-left: 0; }
.level-1 { margin-left: 1.5em; }  /* a., b., c. */
.level-2 { margin-left: 3.0em; }  /* i., ii., iii. */
</style>
""", unsafe_allow_html=True)

# ---------- DETECTION ----------
TOKEN_RE = re.compile(r'^\s*((?:\d+|[A-Za-z]|[ivxlcdmIVXLCDM]+)\.)\s+(.*)$')
NUM_RE   = re.compile(r'^\d+\.')                 # level 0
ALPHA_RE = re.compile(r'^[A-Za-z]\.')            # level 1
ROMAN_RE = re.compile(r'^(?=[ivxlcdmIVXLCDM]+\.)[ivxlcdmIVXLCDM]+\.')  # level 2

def level_for_token(token: str) -> int:
    if NUM_RE.match(token): return 0
    if ALPHA_RE.match(token): return 1
    if ROMAN_RE.match(token): return 2
    return 0

# ---------- PARSER (merge continuation lines) ----------
def parse_blocks(text: str):
    """
    Return a list of blocks.
    Each block is either:
      ("step", token, level, full_text)  -> checkbox row
      ("prose", None, None, full_text)  -> plain paragraph line
    We merge continuation lines to the previous 'step' until a new token or blank line appears.
    """
    blocks = []
    current = None  # holds ("step", token, level, text_so_far)

    for raw in text.splitlines():
        line = raw.rstrip()

        # blank line: close any open step and output a blank as prose
        if line.strip() == "":
            if current:
                blocks.append(current)
                current = None
            blocks.append(("prose", None, None, ""))  # preserve spacing
            continue

        m = TOKEN_RE.match(line)
        if m:
            # starting a new step
            if current:
                blocks.append(current)
            token, rest = m.groups()
            lvl = level_for_token(token)
            current = ("step", token, lvl, rest)
        else:
            # continuation line
            if current:
                # join with a space so wrapped text stays inside the same block
                if current[3].endswith("-"):
                    # handle hyphenated line breaks: drop trailing hyphen
                    current = (current[0], current[1], current[2], current[3][:-1] + line.lstrip())
                else:
                    current = (current[0], current[1], current[2], current[3] + " " + line.lstrip())
            else:
                # prose not part of a step
                blocks.append(("prose", None, None, line))

    if current:
        blocks.append(current)
    return blocks

# ---------- RENDER ----------
def render_blocks(blocks, key_prefix="blk"):
    for i, (kind, token, lvl, text) in enumerate(blocks, start=1):
        if kind == "prose":
            # blank line or paragraph
            if text == "":
                st.write("")
            else:
                st.markdown(text)
            continue

        # kind == "step"
        with st.container():
            st.markdown(f"""
            <div class="step-row">
                <div class="cb-col">{'<input type="checkbox">'}</div>
                <div class="text-col">
                    <div class="step level-{lvl}">
                        <div class="marker">{token}</div>
                        <div class="content">{text}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

blocks = parse_blocks(FULL_TEXT)
render_blocks(blocks)
