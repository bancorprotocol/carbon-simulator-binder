# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + tags=[] jupyter={"source_hidden": true}
import os
if not os.path.isfile("NOPIP"):
    print("Running pip installs. Create a file called 'NOPIP' to disable.")
    # %pip install carbon-simulator
    # %pip install ipywidgets
    # %pip install requests

# + tags=[] jupyter={"source_hidden": true}
from carbon.helpers.cryptocompare import CryptoCompare
from carbon.helpers.widgets import CheckboxManager, DropdownManager, PcSliderManager
import pandas as pd

print( "{0.__name__} v{0.__VERSION__} ({0.__DATE__})".format(CryptoCompare))
# -

# # Data Download
#
# **IMPORTANT -- THIS SHEET MAY NOT WORK IN THE JUPYTER LITE BROWSER ENVIRONMENT SO FOR IT TO RUN YOU MAY UNFORTUNATELY HAVE TO RUN IT ON A LOCAL INSTALL AND UPLOAD THE FILES.** If prefer to not install Carbon, you can directly download [cryptocompare.py][ccpy] and [widgets.py][wpy] from [carbon.helpers][ch].
#
# [ccpy]:https://github.com/bancorprotocol/carbon-simulator/blob/main/carbon/helpers/cryptocompare.py
# [wpy]:https://github.com/bancorprotocol/carbon-simulator/blob/main/carbon/helpers/widgets.py
# [ch]:https://github.com/bancorprotocol/carbon-simulator/tree/main/carbon/helpers

# ## Setup

# Please provide the following information in the variables below
# - `NAME`: the name of the data collection
# - `PAIRS`: the pairs that data collection will contain
# - `FREQ`: the data frequency (FREQ_DAILY, FREQ_HOURLY, FREQ_MINUTELY)
# - `APIKEY`: if you have a CryptoCompare API Key you can put it there; otherwise set to `True`
#
# **(click on the three dots if the cell below does not show)**

# + tags=[]
NAME      = "TESTCOLLECTION"
PAIRS     = "DOGE/USD, AVAX/USD"
FREQ      = CryptoCompare.FREQ_DAILY
APIKEY    = True
# -

# Please check that the above information is correct and check the `Correct` box. There will be no further confirmation, and any existing data will be overwritten.

# + tags=[] jupyter={"source_hidden": true}
DATAPATH = "../data"
FNAME = os.path.join(DATAPATH, f"{NAME}-{FREQ.upper()}.pickle")
print("NAME:", NAME)
print("PAIRS:", PAIRS)
print("FREQ:", FREQ)
print("DATAPATH:", DATAPATH)
print("FNAME:", FNAME)
print()
try:
    confirmation_w()
except:
    confirmation_w = CheckboxManager.from_idvdct(
        {f"Correct": False,})
    confirmation_w()
if not confirmation_w.values[0]:
    raise RuntimeError("Please verify the inputs and confirm that they are correct by checking the above box! Then Run All.")

# + [markdown] tags=[]
# ## API call and save

# + tags=[] jupyter={"source_hidden": true}
CC=CryptoCompare(apikey=APIKEY)
data_df = CC.aggr_query(
    pairs=PAIRS, 
    fields=CC.FIELD_CLOSE, 
    freq=FREQ,
    incl_raw=False,
    incl_raw_aggr=False,
    incl_grand_aggr=False,
)["aggr"][CC.FIELD_CLOSE]
data_df.to_pickle(FNAME)
print("="*80)
print(f"Wrote data to {FNAME}")
print("="*80)
data_df.head()
# -

# ## Check load works

# + tags=[] jupyter={"source_hidden": true}
pd.read_pickle(FNAME)

# + jupyter={"source_hidden": true} tags=[]

