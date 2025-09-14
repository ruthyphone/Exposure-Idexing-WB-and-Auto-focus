import re
import streamlit as st

st.set_page_config(page_title="Exposure Indexing + FX6 Guide", page_icon="🎥", layout="wide")
st.title("Exposure Indexing (EI) & Sony FX6 Advanced Settings")
st.caption("Numbered/lettered/roman lines are checkboxes. Wrapped/continued lines keep the correct hanging indent.")

# ---------- CSS for Hanging Indents ----------
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

# ---------- FULL TEXT ----------
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

Sony FX6 Advanced Settings Guide: White Balance and Autofocus
White balance A and B (Auto White Balance)
In most filming situations, particularly verité/observational, using white balance presets such as
3200K, 4300K, 5600K, is recommended. Presets will be close enough the majority of the time.
When using all artificial lighting, you can manually set your white balance to match the color
temperature you have chosen for your lights using the white balance button and multi-dial.
However, there are times when an interview may have mixed lighting from a window, a practical
light, and/or your own artificial lights. This is where the “A” and “B” white balance (auto white
balance) settings and the use of a white/gray balance card come in handy. These tools will
enable you to set a perfectly accurate white balance setting (color temperature) so that skin tones
are represented accurately. Keep in mind that this is useful mainly in interviews with mixed
lighting. It is not useful in verité/observational filming because lighting is changing all the time
and therefore you would be white balancing constantly.
For review, the reason it’s called “white balance” is because plain white cards are used as a
baseline for the reflection of light. Essentially, we are showing the camera what plain white
looks like in any given lighting situation. All people and objects reflect light; that’s how we are
able to see the world around us. Plain white reflects the most light, which is why it is used for
color balancing and hence the term “white balance.” In other words, if a camera’s color
temperature is balanced to a white card, then all colors will be represented accurately.
1. For review, to use a WB preset for most situations indoors and outdoors:
a. Press the White Balance button on the side of the camera
b. Use the Multi-Dial to adjust white balance.
2. To set perfectly accurate white balance in mixed lighting with a white card, toggle the white
balance switch to either A or B. Basically, these are two “slots” that allow you to save a custom
white balance setting.
a. Next, hold your white card in front of the lens so that it fills most of the frame. It is very
important to make sure that the white card is reflecting as much light in the scene as
possible. Otherwise, the white balance reading will be inaccurate.
b. While holding the white balance card in front of the lens, press the “WB Set” button on
the front of the camera body. The camera will now get an exact color temperature
reading of the light “falling” on your participant’s face. This will now be saved to switch
A or B, whichever you selected.
(Continued on back)
AUTO FOCUS: Sony cinema cameras have incredible auto focus / eye tracking capabilities.
This feature only works with lenses that can electronically communicate with the camera. In
most cases, this means a lens of the same brand. The Sony 28-135 cinema zoom works perfectly
for this feature. We have two in the graduate equipment room.
To engage this feature when using the Sony 28-135 cinema zoom, first adjust the focus
ring to the proper position. The focus ring has two positions: The forward position (“AF/MF”)
and the rearward position (“FULL MF”). For full autofocus functionality, adjust the focus ring
to the forward position.
1. You can toggle the “Focus Auto” switch on the front of the camera body to the auto
position, and the camera will automatically reach peak focus on what it thinks is the
most important part of the frame.
a. You can also use the touchscreen to tap anywhere in the frame to engage the
auto focusing tracking on a person or object. You will see a box appear
around the person or object.
b. To disengage the auto focus tracking, you can do one of three things:
i. Slightly rotate the focus ring
ii. Toggle the “Focus Auto” switch to the manual position
iii. Press the “Push Auto” button once (on the front of the camera body)
2. Having the “Focus Auto” switch toggled to the manual position is most useful and
therefore recommended because you can both manually focus and engage and
disengage the autofocus tracking as needed.
a. When in this mode, use the touchscreen to tap anywhere in the frame to
engage the auto focusing tracking on a person or object. You will see a box
appear around the person or object. This is highly useful during interviews
with people who move a lot in the chair.
b. To disengage the auto focus tracking, you can do one of three things:
i. Slightly rotate the focus ring
ii. Toggle the “Focus Auto” switch to the auto position
iii. Press the “Push Auto” button once (on the front of the camera body)
c. Finally, when the “Focus Auto” switch is toggled to the manual position, and
the lens is out of focus, you can press and hold the “Push Auto” button to
quickly reach peak focus without engaging the autofocus tracking feature.
"""

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

# ---------- PARSER ----------
def parse_blocks(text: str):
    """Merge continuation lines under the previous step."""
    blocks = []
    current = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.strip() == "":
            if current:
                blocks.append(current)
                current = None
            blocks.append(("prose", None, None, ""))
            continue
        m = TOKEN_RE.match(line)
        if m:
            if current:
                blocks.append(current)
            token, rest = m.groups()
            lvl = level_for_token(token)
            current = ("step", token, lvl, rest)
        else:
            if current:
                current = (current[0], current[1], current[2], current[3] + " " + line.lstrip())
            else:
                blocks.append(("prose", None, None, line))
    if current:
        blocks.append(current)
    return blocks

# ---------- RENDER ----------
def render_blocks(blocks):
    for kind, token, lvl, text in blocks:
        if kind == "prose":
            if text == "":
                st.write("")
            else:
                st.markdown(text)
            continue
        st.markdown(f"""
        <div class="step-row">
            <div class="cb-col"><input type="checkbox"></div>
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
