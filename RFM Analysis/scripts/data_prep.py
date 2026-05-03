import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_excel(os.path.join(BASE_DIR, "data", "raw", "online_retail_II.xlsx"), sheet_name="Year 2009-2010")

df["Invoice"] = df["Invoice"].astype(str)
df = df[~df["Invoice"].str.startswith("C")]
df = df.dropna(subset=["Customer ID"])


df["Revenue"] = df["Quantity"] * df["Price"]
df = df[df["Revenue"] > 0]