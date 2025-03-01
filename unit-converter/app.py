import streamlit as st

# Conversion factors dictionary
conversion_factors = {
    "Length": {"Meter": 1, "Kilometer": 0.001, "Mile": 0.000621371, "Foot": 3.28084, "Inch": 39.3701},
    "Weight": {"Gram": 1, "Kilogram": 0.001, "Pound": 0.00220462, "Ounce": 0.035274},
    "Temperature": {"Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15},
    "Time": {"Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400},
    "Speed": {"m/s": 1, "km/h": 3.6, "mph": 2.23694}
}

# Unit conversion function
def convert_units(category, unit_from, unit_to, value):
    if category not in conversion_factors:
        return None
    if unit_from not in conversion_factors[category] or unit_to not in conversion_factors[category]:
        return None
    
    if category == "Temperature":
        return conversion_factors[category][unit_to](conversion_factors[category][unit_from](value))
    else:
        return value * (conversion_factors[category][unit_to] / conversion_factors[category][unit_from])

# Streamlit UI
st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("🌟 Professional Unit Converter")

# ✅ Correcting categories extraction
categories = list(conversion_factors.keys())  # Now it's correctly fetching dictionary keys

category = st.selectbox("Select a category", categories, index=0)

units = list(conversion_factors[category].keys()) if category else []
unit_from = st.selectbox("Convert from", units) if units else None
unit_to = st.selectbox("Convert to", units) if units else None
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

if st.button("Convert") and unit_from and unit_to:
    result = convert_units(category, unit_from, unit_to, value)
    if result is not None:
        st.success(f"{value} {unit_from} = {result:.2f} {unit_to}")
    else:
        st.error("Conversion failed! Please check selected units.")
