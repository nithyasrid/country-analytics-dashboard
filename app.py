import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Country Analytics Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Country Analytics Dashboard")
st.write("Data Source: REST Countries API")

# API URL
URL = "https://restcountries.com/v3.1/all?fields=name,capital,population,region,currencies,languages,area,flags"

# Load Data
try:
    with st.spinner("Loading country data..."):

        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        data = response.json()

        countries = []

        for country in data:

            currency = ", ".join(
                country.get("currencies", {}).keys()
            )

            languages = ", ".join(
                country.get("languages", {}).values()
            )

            countries.append({
                "country": country["name"]["common"],
                "capital": (country.get("capital") or ["N/A"])[0],
                "population": country.get("population", 0),
                "region": country.get("region", "Unknown"),
                "area": country.get("area", 0),
                "currency": currency,
                "languages": languages,
                "flag_url": country.get("flags", {}).get("png", "")
            })

        df = pd.DataFrame(countries)

except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Sidebar Filters
st.sidebar.header("Filters")

search_country = st.sidebar.text_input(
    "Search Country"
)

regions = ["All"] + sorted(df["region"].dropna().unique())

selected_region = st.sidebar.selectbox(
    "Select Region",
    regions
)

sort_option = st.sidebar.selectbox(
    "Sort By",
    [
        "None",
        "Population (High to Low)",
        "Area (High to Low)"
    ]
)

# Apply Search Filter
if search_country:
    df = df[
        df["country"].str.contains(
            search_country,
            case=False,
            na=False
        )
    ]

# Apply Region Filter
if selected_region != "All":
    df = df[
        df["region"] == selected_region
    ]

# Apply Sorting
if sort_option == "Population (High to Low)":
    df = df.sort_values(
        by="population",
        ascending=False
    )

elif sort_option == "Area (High to Low)":
    df = df.sort_values(
        by="area",
        ascending=False
    )

# Summary Statistics
st.subheader("📊 Summary Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Countries",
        len(df)
    )

with col2:
    st.metric(
        "Average Population",
        f"{int(df['population'].mean()):,}"
        if len(df) > 0 else "0"
    )

with col3:
    st.metric(
        "Largest Population",
        f"{int(df['population'].max()):,}"
        if len(df) > 0 else "0"
    )

with col4:
    st.metric(
        "Average Area",
        f"{int(df['area'].mean()):,}"
        if len(df) > 0 else "0"
    )

# Data Table
st.subheader("🌎 Country Data")

st.dataframe(
    df,
    use_container_width=True
)

# Country Flag Viewer
st.subheader("🏳️ Country Flag")

if len(df) > 0:

    selected_country = st.selectbox(
        "Choose Country",
        df["country"]
    )

    selected_row = df[
        df["country"] == selected_country
    ].iloc[0]

    st.image(
        selected_row["flag_url"],
        width=250
    )

    st.write("Capital:", selected_row["capital"])
    st.write("Region:", selected_row["region"])
    st.write("Population:", f"{selected_row['population']:,}")
    st.write("Area:", f"{selected_row['area']:,}")
    st.write("Currency:", selected_row["currency"])
    st.write("Languages:", selected_row["languages"])

# Interactive Chart
st.subheader("📈 Top 10 Countries by Population")

if len(df) > 0:

    top10 = df.nlargest(
        min(10, len(df)),
        "population"
    )

    fig = px.bar(
        top10,
        x="country",
        y="population",
        hover_data=[
            "capital",
            "region"
        ],
        title="Top Countries by Population"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# Download CSV
st.subheader("⬇️ Download Data")

csv = df.to_csv(
    index=False
)

st.download_button(
    label="Download Filtered CSV",
    data=csv,
    file_name="countries.csv",
    mime="text/csv"
)

# Footer
st.markdown("---")
st.write(
    "Built with Streamlit, Pandas, Plotly and REST Countries API"
)