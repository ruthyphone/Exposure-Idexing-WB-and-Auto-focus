import re
import streamlit as st

st.set_page_config(page_title="Exposure Indexing + FX6 Guide", page_icon="🎥", layout="wide")
st.title("Exposure Indexing (EI) & Sony FX6 Advanced Settings")
st.caption("Numbered/lettered/roman lines are checkboxes. Wrapped lines now keep the correct hanging indent.")

# ---------- YOUR TEXT (VERBATIM) ----------
FULL_TEXT = """Exposure Indexing (EI) Guide:
EI stands for Exposure Indexing. It is an advanced feature of cinema cameras that is used in
very specific situations but is particularly useful in low light with a lot of shadows and contrast.
For example, a single light source with a lot of dark shadows around the edges of the frame.
Its numbering system is similar to ISO, but the two are very different. ISO is simply your
camera’s sensitivity to light. Exposure Indexing is a fancy term for intentionally overexposing or
underexposing your image (shifting the camera’s dynamic range to favor bright or shadowy areas
of a scene) while maintaining a comfortable brightness level on your monitor for viewing.
Even though exposure indexing can be used to intentionally overexpose or underexpose an
image, it is often used to creatively overexpose in low lighting situations with a lot of shadows
and contrast to maintain image detail in shadowy scenes while avoiding image “noise” or
graininess. We will eventually adjust the exposure back down in post-production to achieve a
“normal” image.
To use Exposure Indexing in extreme low-light situations to bring out more image detail in
shadow areas:
1. First, it can help to use an external monitor.
2. Press and release the Menu button to access the quick menu on the LCD touch screen.
3. Use the multi-dial to scroll to Monitoring (page 5/10)
4. Set the VF to SG3C/Slog3. This will route the SLog signal to the LCD screen.
5. Set the HDMI/SDI to MLUT. This will put a LUT on your external monitor.
6. Set the Base Look / LUT to s709. This is the LUT for standard viewing (as set in the
previous step, the s709 LUT will only appear on your external monitor).
7. Exit the LCD touch screen menu and then press and hold the Menu button to enter the
camera’s full menu.
a. Scroll to Shooting > LUT On/Off
b. You will see your settings from the touch screen menu reflected here.
c. Make sure Internal Rec is set to MLUT Off (this ensures that you are only
viewing the s709 LUT and not recording it “baked in” to your footage on the
media card where it can’t be undone).
8. Exit the menu. Your LCD screen should now be in SLog and your external monitor
should be in s709.
a. Press the Assign button on the side of the LCD screen to activate the Waveform
Monitor on the LCD screen. When using an external monitor, the waveform
monitor will display the signal being sent to the external monitor (either s709
or SLog) and not the LCD screen on the camera. In this case, we have
assigned the s709 LUT to the external monitor, so you should see “LUT s709”
immediately above the waveform monitor on the LCD screen.
9. Setting exposure indexing for extreme low-light conditions:
a. Press and hold the Menu button to access the full menu.
b. Scroll to Shooting > ISO/Gain/EI >
ii. Set Exposure Index<H> to 800EI / 6.0E
iii. Set Exposure Index<M> to 400EI / 5.0E
iv. Set Exposure Index<L> to 200EI / 4.0E
It is important to note at this point that when we are in Cine EI mode to film in SLog but are not
using exposure indexing for a specific lighting situation, we should always have the EI setting
equal to the camera’s base ISO. In the majority of lighting situations, we are using base 800 ISO
(indicated on the right sight of the camera’s viewfinder). This means that the EI should also be
set to 800 (indicated at the bottom center of the viewfinder). This maximizes the camera’s
dynamic range for the majority of our filming needs.
10. Because you have already set your H, M, L Exposure Index levels in the previous step,
you are now ready to use exposure indexing in low-light, shadowy conditions. In such
situations, you will intentionally but creatively overexpose by 1 or 2 stops, depending on
how dark the shadow areas are in the scene.
Remember, 1 stop brighter means the camera is seeing twice as much light; 2 stops
brighter means the camera is seeing 4 times as much light (each stop increase is double
the amount of light from the previous stop; each stop decrease is half as much light from
the previous stop).
a. To overexpose by 1 stop: Set the H, M, L toggle switch on the side of the camera
to M. In the bottom middle part of the LCD screen, you should see the EI change
from 800 EI to 400 EI. Notice how this change does not affect the SLog image.
Exposure indexing only affects LUTs. Therefore, you should see your external
monitor get darker by 1 stop of light. You’ll also see the light levels in your
waveform monitor drop because they represent the s709 LUT on the external
monitor.
b. Next, because we darkened the external monitor by 1 stop, we need to open up the
aperture by 1 stop to compensate and to bring the brightness of the external
monitor image back up to the original brightness level.
i. Open the aperture on the lens by 1 stop (for example, f/4 to f2.8)
ii. You will notice that the external monitor brightened back up by 1 stop and
the SLog image on the LCD screen brightened by 1 stop. Remember, the
EI setting only affects the LUT; but changing the aperture affects both the
SLog and the LUT.
iii. Now, the recorded SLog footage will be 1 stop brighter, bringing out more
detail in the shadow areas. Remember, we are still in Base ISO 800. EI
is not the same as ISO, even though it uses the same number system.
We have simply overexposed by 1 stop in Base ISO 800 in order to
bring out more detail in dark shadowy areas.
iv. When we get into post-production, we can bring the exposure back down
by 1 stop to normal brightness levels, but we will now have less noise and
graininess in the shadows than if we hadn’t used exposure indexing at all.
c. Repeat this process if you need to overexpose by 2 stops in really dark shadowy
conditions (set the EI toggle switch to L, which is now 200EI, and then open up
the aperture 2 stops to compensate).
NOTE: You don’t have to use an external monitor with exposure indexing. You can put
the s709 LUT on the LCD screen and use the waveform monitor to display the SLog3
signal. Using the same EI steps above, you will achieve the same creative effect.
"""

# ---------- DETECTION PATTERNS ----------
TOKEN_RE = re.compile(r'^\s*((?:\d+|[A-Za-z]|[ivxlcdmIVXLCDM]+)\.)\s+(.*)$')
NUM_RE   = re.compile(r'^\d+\.')                 # level 0
ALPHA_RE = re.compile(r'^[A-Za-z]\.')            # level 1
ROMAN_RE = re.compile(r'^(?=[ivxlcdmIVXLCDM]+\.)[ivxlcdmIVXLCDM]+\.')  # level 2

def level_for_token(token: str) -> int:
    if NUM_RE.match(token):
        return 0
    if ALPHA_RE.match(token):
        return 1
    if ROMAN_RE.match(token):
        return 2
    return 0

# ---------- RENDER FUNCTIONS ----------
def render_step_with_hanging_indent(token, text, level, key):
    """Render a checkbox with proper hanging indent for wrapped lines."""
    indent_em = 1.5 * level
    html = f"""
    <div style="display:flex; align-items:flex-start;">
        <div style="margin-right:0.5em;">
            <input type="checkbox" style="width:1em; height:1em;">
        </div>
        <div style="flex:1; margin-left:{indent_em}em; text-indent:-1.5em; padding-left:1.5em;">
            <strong>{token}</strong> {text}
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_lines(body: str):
    for idx, raw in enumerate(body.splitlines(), start=1):
        line = raw.rstrip()
        if not line:
            st.write("")
            continue
        m = TOKEN_RE.match(line)
        if m:
            token, rest = m.groups()
            lvl = level_for_token(token)
            render_step_with_hanging_indent(token, rest, lvl, key=f"cb_{idx}")
        else:
            st.markdown(line)

# ---------- MAIN RENDER ----------
render_lines(FULL_TEXT)
