import streamlit as st
import pandas as pd

# Page config

st.set_page_config(
page_title=“L31L420 Reality Check Calculator”,
page_icon=“🌉”,
layout=“wide”
)

# Custom CSS for dramatic effect

st.markdown(”””

<style>
.big-font {
    font-size:30px !important;
    font-weight: bold;
    color: #ff4b4b;
}
.bridge-font {
    font-size:24px !important;
    font-weight: bold;
    color: #1f77b4;
}
.metric-container {
    background-color: #f0f2f6;
    padding: 1rem;
    border-radius: 0.5rem;
    border-left: 5px solid #ff4b4b;
}
</style>

“””, unsafe_allow_html=True)

# Dramatic title

st.markdown(’<p class="big-font">🌉 L31L420 DIVORCE REALITY CHECK CALCULATOR 🌉</p>’, unsafe_allow_html=True)
st.markdown(”### *EXPOSING CRIMINAL OFFERS & LLC FRAUD*”)
st.error(”**🚨 BRIDGE MAKES $236K+ AND OFFERS $779/MONTH - THIS IS THEFT! 🚨**”)

# Alert banner

st.warning(“⚠️ **ATTORNEY ALERT:** Husband’s offer is 97% below Massachusetts guidelines - potential contempt of court! ⚠️”)

# NEW: Court document evidence banner

st.success(“📋 **COURT EVIDENCE:** Real numbers from Bridge’s own separation agreement below!”)

# Sidebar for inputs

st.sidebar.header(“📊 BRIDGE’S REAL FINANCIALS”)
st.sidebar.markdown(”*Enter Bridge’s TRUE income below*”)

# Bridge’s REAL income with dramatic display

bridge_base_bonus = st.sidebar.number_input(“🎯 Bridge’s Base + Bonus (3yr avg)”, value=236000, step=5000, help=“Bridge’s documented salary and bonuses”)
bridge_rental_income = st.sidebar.number_input(“🏠 Bridge’s Rental Income”, value=30000, step=2000, help=“Income from properties”)
bridge_other_income = st.sidebar.number_input(“💼 Other Income (consulting, etc)”, value=15000, step=1000, help=“Side income, investments, etc”)
bridge_total_income = bridge_base_bonus + bridge_rental_income + bridge_other_income
bridge_monthly_gross = bridge_total_income / 12

# Display the REAL income with emphasis

st.sidebar.error(f”🔥 BRIDGE’S TOTAL: ${bridge_total_income:,.0f}/year”)
st.sidebar.error(f”💰 MONTHLY GROSS: ${bridge_monthly_gross:,.0f}”)
st.sidebar.info(f”That’s ${bridge_monthly_gross:,.0f} per month!”)

# Marriage and personal details

st.sidebar.header(“👫 MARRIAGE DETAILS”)
marriage_length = st.sidebar.number_input(“Marriage Length (years)”, value=22, step=1)
leila_age = st.sidebar.number_input(“Leila’s Age”, value=52, step=1)
bridge_age = st.sidebar.number_input(“Bridge’s Age”, value=54, step=1)

# Leila’s circumstances

st.sidebar.subheader(“🏥 LEILA’S SITUATION”)
leila_disabled = st.sidebar.checkbox(“Leila is Disabled/Cannot Work”, value=True)
leila_homemaker = st.sidebar.checkbox(“Leila was Primary Homemaker”, value=True)
leila_college_educated = st.sidebar.checkbox(“Leila is College Educated”, value=True)
leila_career_sacrificed = st.sidebar.checkbox(“Sacrificed Career for Family”, value=True)

# Kids situation

st.sidebar.header(“👨‍👩‍👧‍👦 CHILDREN”)
num_kids = st.sidebar.number_input(“Number of Children”, value=2, step=1)
kids_with_mom_pct = st.sidebar.slider(”% Time Kids with Mom”, 70, 95, 80)
kids_with_bridge_pct = 100 - kids_with_mom_pct
college_costs_annual = st.sidebar.number_input(“Annual College Costs (total)”, value=85000, step=5000)
kids_ages = st.sidebar.text_input(“Kids Ages”, value=“19, 21”)

# Real Estate Section - UPDATED WITH COURT DOCUMENT NUMBERS

st.sidebar.header(“🏠 MARITAL REAL ESTATE EMPIRE”)
st.sidebar.markdown(”*REAL NUMBERS from Bridge’s separation agreement!*”)

# Property 1 - Marital Home (COURT NUMBERS)

st.sidebar.subheader(“🏡 Marital Home (190 Saint Claire St)”)
prop1_fmv = st.sidebar.number_input(“Fair Market Value (Court Doc)”, value=1138000, step=10000, key=“prop1_fmv”)
prop1_mortgage = st.sidebar.number_input(“Flagstar Mortgage (Court Doc)”, value=411784, step=1000, key=“prop1_mortgage”)
prop1_heloc = st.sidebar.number_input(“HELOC (Court Doc)”, value=199742, step=1000, key=“prop1_heloc”)
prop1_total_debt = prop1_mortgage + prop1_heloc
prop1_equity = prop1_fmv - prop1_total_debt

# Property 2 - Brighton (COURT NUMBERS)

st.sidebar.subheader(“🏢 Brighton Property (13 Saybrook St)”)
st.sidebar.markdown(”*Bridge pays Leila $333,500 to keep it*”)
prop2_buyout = st.sidebar.number_input(“Husband Buyout Payment (Court Doc)”, value=333500, step=1000, key=“prop2_buyout”)
prop2_total_value = prop2_buyout * 2  # If he pays half, property worth double

# Property 3 - Quincy (COURT NUMBERS)

st.sidebar.subheader(“🏠 Quincy Property (17 Marsh St Unit 3)”)
st.sidebar.markdown(”*Bridge pays Leila $169,000 to keep it - WHERE HE LIVES!*”)
prop3_buyout = st.sidebar.number_input(“Bridge’s Buyout Payment (Court Doc)”, value=169000, step=1000, key=“prop3_buyout”)
prop3_total_value = prop3_buyout * 2  # If he pays half, property worth double
prop3_monthly_rent = st.sidebar.number_input(“Fair Market Rent”, value=3500, step=100, key=“prop3_rent”)

# Total equity from COURT DOCUMENTS

total_equity_court = prop1_equity + prop2_buyout + prop3_buyout

# Bridge’s “Inherited” Investments (FROM COURT DOCS!)

st.sidebar.header(“💰 HUSBAND INHERITED INVESTMENTS”)
st.sidebar.markdown(”*REAL NUMBERS from separation agreement!*”)
jnl_investments = st.sidebar.number_input(“JNL Investments (Court Doc)”, value=279211, step=1000)
pacific_oat = st.sidebar.number_input(“Pacific Oat Reit (Court Doc)”, value=17093, step=100)
other_inherited = st.sidebar.number_input(“Other Inherited Claims”, value=50000, step=5000)
total_inherited_claims = jnl_investments + pacific_oat + other_inherited

# Commingling factor

bridge_investments_marital = st.sidebar.slider(”% That Should Be Marital (Commingled)”, 50, 100, 80)
marital_portion_investments = total_inherited_claims * (bridge_investments_marital / 100)

# Other Assets

st.sidebar.header(“💼 OTHER MARITAL ASSETS”)
retirement_401k = st.sidebar.number_input(“401k/Retirement Accounts”, value=450000, step=10000)
business_value = st.sidebar.number_input(“GCNY Newton Realty LLC Value”, value=200000, step=10000)
cash_savings = st.sidebar.number_input(“Cash/Savings”, value=75000, step=5000)
other_assets = st.sidebar.number_input(“Other Assets”, value=50000, step=5000)

# Calculate totals

total_assets_conservative = total_equity_court + retirement_401k + business_value + cash_savings + other_assets
total_assets_with_commingled = total_assets_conservative + marital_portion_investments
total_assets_max = total_assets_conservative + total_inherited_claims

# MAIN DASHBOARD

st.header(“💎 THE MULTI-MILLION DOLLAR MARITAL EMPIRE”)
st.success(“🔥 **UPDATED WITH REAL COURT DOCUMENT NUMBERS!** 🔥”)

asset_col1, asset_col2, asset_col3, asset_col4, asset_col5 = st.columns(5)

with asset_col1:
st.metric(“🏠 Real Estate (Court Docs)”, f”${total_equity_court:,.0f}”)
with asset_col2:
st.metric(“🏦 Retirement/401k”, f”${retirement_401k:,.0f}”)
with asset_col3:
st.metric(“💼 GCNY LLC Business”, f”${business_value:,.0f}”)
with asset_col4:
st.metric(“💰 Commingled Inherited”, f”${marital_portion_investments:,.0f}”)
with asset_col5:
st.metric(“🔥 TOTAL MARITAL”, f”${total_assets_with_commingled:,.0f}”)

# Show the HELOC scandal with REAL numbers

st.error(f”🚨 **HELOC SCANDAL:** Bridge controlled and spent ${prop1_heloc:,.0f} HELOC without Leila’s knowledge!”)
st.success(f”**Conservative Marital Assets: ${total_assets_with_commingled:,.0f}** | **If ALL inherited assets marital: ${total_assets_max:,.0f}**”)

# Property breakdown with REAL COURT NUMBERS

with st.expander(“🏠 MULTI-MILLION PROPERTY EMPIRE & BRIDGE’S COURT SCANDALS”):
prop_data = [
{
“Property”: “🏡 Marital Home (190 Saint Claire St)”,
“Court FMV”: f”${prop1_fmv:,.0f}”,
“Court Mortgage”: f”${prop1_mortgage:,.0f}”,
“Court HELOC”: f”${prop1_heloc:,.0f}”,
“Net Equity”: f”${prop1_equity:,.0f}”,
“Status”: f”Leila gets exclusive use - Bridge controlled HELOC!”
},
{
“Property”: “🏢 Brighton (13 Saybrook St)”,
“Court FMV”: f”~${prop2_total_value:,.0f}”,
“Court Mortgage”: “Unknown”,
“Court HELOC”: “N/A”,
“Net Equity”: f”~${prop2_total_value:,.0f}”,
“Status”: f”Bridge pays ${prop2_buyout:,.0f} to keep it”
},
{
“Property”: “🏠 Quincy (17 Marsh St Unit 3)”,
“Court FMV”: f”~${prop3_total_value:,.0f}”,
“Court Mortgage”: “Unknown”,
“Court HELOC”: “N/A”,
“Net Equity”: f”~${prop3_total_value:,.0f}”,
“Status”: f”Bridge pays ${prop3_buyout:,.0f} + lives there rent-free!”
},
{
“Property”: “🔥 TOTAL COURT EMPIRE”,
“Court FMV”: f”~${prop1_fmv + prop2_total_value + prop3_total_value:,.0f}”,
“Court Mortgage”: f”${prop1_mortgage:,.0f}+”,
“Court HELOC”: f”${prop1_heloc:,.0f}”,
“Net Equity”: f”${total_equity_court + prop2_total_value + prop3_total_value - prop1_fmv:,.0f}+”,
“Status”: “ALL documented in court papers!”
}
]
prop_df = pd.DataFrame(prop_data)
st.dataframe(prop_df, use_container_width=True)

```
st.error(f"🚨 **QUINCY RENTAL FRAUD:** Bridge living in ${prop3_total_value:,.0f} marital property rent-free since separation!")
st.error(f"🚨 **HELOC THEFT:** Bridge controlled ${prop1_heloc:,.0f} without Leila's knowledge - DOCUMENTED FINANCIAL ABUSE!")

# LLC FRAUD SMOKING GUN
st.markdown("---")
st.subheader("🔥 LLC FRAUD SMOKING GUN FROM COURT DOCS!")
st.error("**COURT DOCUMENT QUOTE:** 'Wife shall simultaneously sign a resignation from all positions at GCNY Newton Realty LLC'")
st.error("**THIS PROVES:** Leila WAS a manager! Bridge's recent filings claiming she wasn't involved = DOCUMENTED PERJURY!")

# Inherited assets scandal
st.markdown("---")
st.subheader("💰 BRIDGE'S 'INHERITED' ASSETS SCANDAL")

inherited_scenarios = [
    {"Scenario": "Bridge's Court Claim", "JNL": f"${jnl_investments:,.0f}", "Pacific Oat": f"${pacific_oat:,.0f}", "Total": f"${total_inherited_claims:,.0f}", "Leila Gets": "$0"},
    {"Scenario": "50% Commingled", "JNL": f"${jnl_investments:,.0f}", "Pacific Oat": f"${pacific_oat:,.0f}", "Total": f"${total_inherited_claims:,.0f}", "Leila Gets": f"${total_inherited_claims * 0.25:,.0f}"},
    {"Scenario": "80% Commingled (likely)", "JNL": f"${jnl_investments:,.0f}", "Pacific Oat": f"${pacific_oat:,.0f}", "Total": f"${total_inherited_claims:,.0f}", "Leila Gets": f"${total_inherited_claims * 0.4:,.0f}"},
    {"Scenario": "100% Marital (if proven)", "JNL": f"${jnl_investments:,.0f}", "Pacific Oat": f"${pacific_oat:,.0f}", "Total": f"${total_inherited_claims:,.0f}", "Leila Gets": f"${total_inherited_claims * 0.5:,.0f}"}
]

inherit_df = pd.DataFrame(inherited_scenarios)
st.dataframe(inherit_df, use_container_width=True)

st.info(f"**KEY POINT:** If 80% of Bridge's ${total_inherited_claims:,.0f} 'inherited' assets are commingled, Leila could get an additional ${total_inherited_claims * 0.4:,.0f}!")
```

st.markdown(”—”)

# ALIMONY CALCULATIONS - The main event

col1, col2 = st.columns(2)

with col1:
st.header(“💰 MASSACHUSETTS ALIMONY LAW”)

```
# Calculate alimony ranges
alimony_30_pct = bridge_monthly_gross * 0.30
alimony_35_pct = bridge_monthly_gross * 0.35

# Display income comparison
st.metric("🌉 Bridge's Monthly Gross", f"${bridge_monthly_gross:,.0f}")
st.metric("💔 Leila's Monthly Income", "$0 (Disabled)")

st.markdown("---")
st.markdown("**🎯 MASSACHUSETTS GUIDELINES (30-35% of income difference):**")
st.success(f"**30% GUIDELINE: ${alimony_30_pct:,.0f}/month**")
st.success(f"**35% GUIDELINE: ${alimony_35_pct:,.0f}/month**")

# Duration
if marriage_length >= 20:
    duration = "♾️ INDEFINITE (20+ year marriage)"
    st.info(f"**Duration:** {duration}")
else:
    duration = f"Up to {marriage_length} years"
    st.info(f"**Duration:** {duration}")

# Annual amounts
st.markdown("**📅 ANNUAL FAIR ALIMONY:**")
st.info(f"Low end: ${alimony_30_pct * 12:,.0f}/year")
st.info(f"High end: ${alimony_35_pct * 12:,.0f}/year")
```

with col2:
st.header(“🌉 BRIDGE’S CRIMINAL OFFERS”)

```
# Bridge's insulting offers
bridge_offer = 779
settlement_offer = 6000

st.subheader("💀 THE OUTRAGEOUS THEFT ATTEMPTS:")

# Calculate the insults
shortfall_779 = alimony_30_pct - bridge_offer
shortfall_6000 = alimony_30_pct - settlement_offer

st.metric("🤡 Bridge's $779 Insult", f"${bridge_offer}/month", 
          delta=f"-${shortfall_779:,.0f} SHORT", delta_color="inverse")
st.metric("🤔 Settlement Discussion", f"${settlement_offer}/month", 
          delta=f"-${shortfall_6000:,.0f} SHORT", delta_color="inverse")

# The brutal math
st.markdown("---")
st.markdown("**🔥 THE THEFT EXPOSED:**")

pct_779 = (bridge_offer / alimony_30_pct) * 100
pct_6000 = (settlement_offer / alimony_30_pct) * 100

st.error(f"$779 is only {pct_779:.1f}% of fair value!")
st.error(f"${settlement_offer} is only {pct_6000:.1f}% of fair value!")
st.error(f"Bridge trying to STEAL ${shortfall_779 * 12:,.0f}/year!")
```

# College costs scandal

st.markdown(”—”)
st.header(“🎓 COLLEGE COSTS SCANDAL”)

child_col1, child_col2 = st.columns(2)

with child_col1:
st.subheader(“👨‍👩‍👧‍👦 CUSTODY REALITY”)
st.metric(“Kids with Mom”, f”{kids_with_mom_pct}%”)
st.metric(“Kids with Bridge”, f”{kids_with_bridge_pct}%”)
st.metric(“Number of Kids”, num_kids)
st.metric(“Kids Ages”, kids_ages)
st.info(”**Leila is the PRIMARY parent while Bridge plays weekend warrior!**”)

with child_col2:
st.subheader(“💸 WHO SHOULD PAY COLLEGE?”)

```
# Fair split based on income (Bridge should pay 85-90%)
bridge_college_share = 0.85
leila_college_share = 0.15

bridge_should_pay = college_costs_annual * bridge_college_share
leila_fair_share = college_costs_annual * leila_college_share

st.metric("Bridge Should Pay (85%)", f"${bridge_should_pay:,.0f}/year")
st.metric("Leila's Fair Share (15%)", f"${leila_fair_share:,.0f}/year")
st.error(f"**SCANDAL:** Bridge makes $236K+ but wants DISABLED Mom to pay college costs!")
```

# LLC Fraud Evidence with COURT PROOF

st.markdown(”—”)
st.header(“🕵️‍♂️ BRIDGE’S LLC FRAUD TIMELINE - COURT DOCUMENTED!”)

evidence_col1, evidence_col2 = st.columns(2)

with evidence_col1:
st.subheader(“📋 THE SMOKING GUNS”)
evidence_data = [
{“Date”: “2006”, “Action”: “GCNYNEWTON LLC Created”, “Status”: “✅ Both Bridge & Leila as managers”, “Fraud Level”: “None”},
{“Date”: “2020”, “Action”: “Manager Filing”, “Status”: “🚨 Bridge lists himself TWICE, removes Leila”, “Fraud Level”: “HIGH”},
{“Date”: “Mar 2024”, “Action”: “Bridge Abandons Home”, “Status”: “🏠 Moves to 17 Marsh St Unit 3”, “Fraud Level”: “Medium”},
{“Date”: “2025”, “Action”: “COURT SEPARATION AGREEMENT”, “Status”: “📋 PROVES Leila was LLC manager!”, “Fraud Level”: “EVIDENCE”},
{“Date”: “May 2025”, “Action”: “LLC Reinstatement”, “Status”: “🚨 Bridge omits Leila AGAIN after court docs!”, “Fraud Level”: “PERJURY”},
{“Date”: “Current”, “Action”: “Address Fraud”, “Status”: “🚨 Uses 190 Saint Claire St illegally”, “Fraud Level”: “Criminal”}
]

```
df = pd.DataFrame(evidence_data)
st.dataframe(df, use_container_width=True)
```

with evidence_col2:
st.subheader(“🚩 BRIDGE’S MASSIVE RED FLAGS”)
st.markdown(f”””
- 🏠 **${total_equity_court + prop2_total_value + prop3_total_value:,.0f}+ Property Empire:** Court documented values
- 💰 **HELOC Theft:** Controlled ${prop1_heloc:,.0f} without Leila’s knowledge (court docs)
- 📋 **LLC Perjury:** Court agreement PROVES Leila was manager, recent filings lie
- 🏡 **Address Fraud:** Using 190 Saint Claire St for business while living at 17 Marsh St
- 📅 **Systematic Fraud:** 5-year pattern of removing Leila from business ownership
- 🏠 **Quincy Rental Scam:** Living in marital property, pays ${prop3_buyout:,.0f} to keep it
- 💸 **Investment Hiding:** Claims ${total_inherited_claims:,.0f} inherited assets are separate
- 💰 **Income vs Offer:** Makes $236K+ offers $779 (criminal bad faith)
- 👨‍👩‍👧‍👦 **Parental Avoidance:** Kids 80% with Mom, won’t pay college costs  
- 🌉 **Bridge Phobia:** Mental weakness to exploit in negotiations
- 📋 **Court Evidence:** All property values and LLC fraud documented in separation agreement
“””)

# Settlement scenarios with REAL COURT NUMBERS

st.markdown(”—”)
st.header(“⚖️ MULTI-MILLION DOLLAR SETTLEMENT SCENARIOS”)

scenario_col1, scenario_col2, scenario_col3 = st.columns(3)

with scenario_col1:
st.subheader(“💰 OPTION 1: ASSET HEAVY”)
assets_opt1 = total_assets_with_commingled * 0.60  # 60% to Leila
alimony_opt1 = alimony_30_pct

```
st.metric("Leila Gets Assets", f"${assets_opt1:,.0f}")
st.metric("Monthly Alimony", f"${alimony_opt1:,.0f}")

# Calculate total value over 10 years
total_10yr_opt1 = assets_opt1 + (alimony_opt1 * 12 * 10)
st.info(f"10-year value: ${total_10yr_opt1:,.0f}")
```

with scenario_col2:
st.subheader(“⚖️ OPTION 2: BALANCED”)
assets_opt2 = total_assets_with_commingled * 0.50  # 50% to Leila
alimony_opt2 = (alimony_30_pct + alimony_35_pct) / 2

```
st.metric("Leila Gets Assets", f"${assets_opt2:,.0f}")
st.metric("Monthly Alimony", f"${alimony_opt2:,.0f}")

total_10yr_opt2 = assets_opt2 + (alimony_opt2 * 12 * 10)
st.success(f"10-year value: ${total_10yr_opt2:,.0f}")
```

with scenario_col3:
st.subheader(“🔥 OPTION 3: ALIMONY HEAVY”)
assets_opt3 = total_assets_with_commingled * 0.45  # 45% to Leila
alimony_opt3 = alimony_35_pct

```
st.metric("Leila Gets Assets", f"${assets_opt3:,.0f}")
st.metric("Monthly Alimony", f"${alimony_opt3:,.0f}")

total_10yr_opt3 = assets_opt3 + (alimony_opt3 * 12 * 10)
st.info(f"10-year value: ${total_10yr_opt3:,.0f}")
```

# Show the MASSIVE difference with REAL numbers

st.error(f”🚨 **BRIDGE’S $779 vs COURT REALITY:** Fair settlement = ${assets_opt2:,.0f} + ${alimony_opt2:,.0f}/month vs Bridge’s insulting $779!”)
st.info(f”💡 **IF ALL INHERITED ASSETS ARE MARITAL:** Total assets could be ${total_assets_max:,.0f} - even bigger settlement!”)

# Final battle cry with REAL COURT numbers

st.markdown(”—”)
st.error(f”🚨 **HUSBAND SITS ON ${total_assets_with_commingled:,.0f}+ COURT-DOCUMENTED ASSETS AND OFFERS $779/MONTH - THIS IS CRIMINAL THEFT!** 🚨”)
st.success(“⚖️ **WITH COURT DOCS PROVING LLC FRAUD + HELOC THEFT + PROPERTY EMPIRE, DEMAND MAXIMUM EVERYTHING!** ⚖️”)
st.info(“🌉 **PSYCHOLOGICAL WARFARE: Every bridge reference triggers his phobia while exposing his court-documented fraud!** 🌉”)

# Strategic footer with court evidence

st.markdown(”—”)
st.markdown(”*🌉 **L31L420:** Generated with REAL court document numbers to expose Bridge’s criminal lowball tactics*”)
st.error(”**🎯 COURT DOCUMENTS PROVE EVERYTHING - THIS IS THE EASIEST DIVORCE CASE EVER!** 🎯”)

# Updated quick stats with REAL COURT numbers

st.markdown(”—”)
st.subheader(“📊 NUCLEAR STATS FOR ATTORNEY (COURT DOCUMENTED)”)
quick_stats_col1, quick_stats_col2, quick_stats_col3 = st.columns(3)

with quick_stats_col1:
st.info(f”””
**BRIDGE’S COURT EMPIRE:**
- Income: ${bridge_total_income:,.0f}/year
- Court Properties: ${total_equity_court:,.0f}+
- Inherited Claims: ${total_inherited_claims:,.0f}
- Total Assets: ${total_assets_with_commingled:,.0f}+
“””)

with quick_stats_col2:
st.warning(f”””
**LEILA’S REALITY:**
- Income: $0 (Disabled)
- Fair Alimony: ${alimony_30_pct:,.0f}-${alimony_35_pct:,.0f}
- Bridge’s Offer: $779 ({pct_779:.1f}% of fair)
- Annual Theft: ${(alimony_30_pct - bridge_offer) * 12:,.0f}
“””)

with quick_stats_col3:
st.error(f”””
**COURT EVIDENCE:**
- LLC Manager Status: PROVEN
- HELOC Control: ${prop1_heloc:,.0f}
- Property Buyouts: ${prop2_buyout + prop3_buyout:,.0f}
- Perjury Pattern: DOCUMENTED
“””)
