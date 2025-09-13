
#!/usr/bin/env python3
"""
MDRM Data Analysis Script

This script analyzes the MDRM_CSV.csv file and generates statistics and insights
about the Micro Data Reference Manual (MDRM) data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os

def load_data():
    """Load the MDRM data from CSV file."""
    print("Loading MDRM data...")
    df = pd.read_csv('/workspace/MDRM_CSV.csv', skiprows=1, encoding='utf-8')
    print(f"Loaded {len(df)} rows of data")
    return df

def basic_stats(df):
    """Generate basic statistics about the dataset."""
    print("\n=== BASIC STATISTICS ===")
    print(f"Total number of records: {len(df)}")
    print(f"Number of unique Mnemonics: {df['Mnemonic'].nunique()}")
    print(f"Number of unique Item Codes: {df['Item Code'].nunique()}")
    print(f"Number of unique Reporting Forms: {df['Reporting Form'].nunique()}")
    
    # Convert date columns to datetime
    df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')
    df['End Date'] = pd.to_datetime(df['End Date'], errors='coerce')
    
    # Calculate the date range
    min_date = df['Start Date'].min()
    max_date = df['End Date'].max()
    print(f"Date range: {min_date.strftime('%Y-%m-%d')} to {max_date.strftime('%Y-%m-%d')}")
    
    # Calculate active items (end date is 9999-12-31)
    active_items = df[df['End Date'].dt.year == 9999]
    print(f"Number of currently active items: {len(active_items)} ({len(active_items)/len(df)*100:.2f}%)")

def analyze_mnemonics(df):
    """Analyze the distribution of Mnemonics."""
    print("\n=== MNEMONIC ANALYSIS ===")
    mnemonic_counts = df['Mnemonic'].value_counts()
    print(f"Top 20 most common Mnemonics:")
    print(mnemonic_counts.head(20))
    
    # Calculate statistics
    print(f"\nMnemonic distribution statistics:")
    print(f"Mean items per Mnemonic: {mnemonic_counts.mean():.2f}")
    print(f"Median items per Mnemonic: {mnemonic_counts.median():.2f}")
    print(f"Min items per Mnemonic: {mnemonic_counts.min()}")
    print(f"Max items per Mnemonic: {mnemonic_counts.max()}")
    
    # Plot the distribution of top 10 Mnemonics
    plt.figure(figsize=(12, 6))
    mnemonic_counts.head(10).plot(kind='bar')
    plt.title('Top 10 Most Common Mnemonics')
    plt.xlabel('Mnemonic')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('mnemonic_distribution.png')
    print("Saved mnemonic distribution chart to 'mnemonic_distribution.png'")

def analyze_item_types(df):
    """Analyze the distribution of Item Types."""
    print("\n=== ITEM TYPE ANALYSIS ===")
    item_type_counts = df['ItemType'].value_counts()
    print("Item Type distribution:")
    print(item_type_counts)
    
    # Calculate percentages
    item_type_pct = item_type_counts / len(df) * 100
    print("\nItem Type percentages:")
    for item_type, pct in item_type_pct.items():
        print(f"{item_type}: {pct:.2f}%")
    
    # Plot the distribution
    plt.figure(figsize=(10, 6))
    item_type_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Distribution of Item Types')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('item_type_distribution.png')
    print("Saved item type distribution chart to 'item_type_distribution.png'")

def analyze_confidentiality(df):
    """Analyze the confidentiality distribution."""
    print("\n=== CONFIDENTIALITY ANALYSIS ===")
    conf_counts = df['Confidentiality'].value_counts()
    print("Confidentiality distribution:")
    print(conf_counts)
    
    # Calculate percentages
    conf_pct = conf_counts / len(df) * 100
    print("\nConfidentiality percentages:")
    for conf, pct in conf_pct.items():
        print(f"{conf}: {pct:.2f}%")
    
    # Plot the distribution
    plt.figure(figsize=(8, 6))
    conf_counts.plot(kind='pie', autopct='%1.1f%%', colors=['green', 'red', 'yellow'])
    plt.title('Distribution of Confidentiality')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('confidentiality_distribution.png')
    print("Saved confidentiality distribution chart to 'confidentiality_distribution.png'")

def analyze_item_codes(df):
    """Analyze the distribution of Item Codes."""
    print("\n=== ITEM CODE ANALYSIS ===")
    item_code_counts = df['Item Code'].value_counts()
    print(f"Top 20 most common Item Codes:")
    print(item_code_counts.head(20))
    
    # Find items that appear across many mnemonics
    print("\nItem Codes that appear across the most Mnemonics:")
    item_cross_mnemonic = df.groupby('Item Code')['Mnemonic'].nunique().sort_values(ascending=False)
    print(item_cross_mnemonic.head(10))
    
    # For the top 5 cross-mnemonic items, show their names
    print("\nDetails of top 5 cross-mnemonic items:")
    for item_code in item_cross_mnemonic.head(5).index:
        item_names = df[df['Item Code'] == item_code]['Item Name'].unique()
        print(f"Item Code {item_code} appears in {item_cross_mnemonic[item_code]} mnemonics")
        print(f"Item Name(s): {', '.join(item_names)}")
        print()

def analyze_reporting_forms(df):
    """Analyze the distribution of Reporting Forms."""
    print("\n=== REPORTING FORM ANALYSIS ===")
    form_counts = df['Reporting Form'].value_counts()
    print(f"Top 20 most common Reporting Forms:")
    print(form_counts.head(20))
    
    # Calculate statistics
    print(f"\nReporting Form distribution statistics:")
    print(f"Mean items per Reporting Form: {form_counts.mean():.2f}")
    print(f"Median items per Reporting Form: {form_counts.median():.2f}")
    print(f"Min items per Reporting Form: {form_counts.min()}")
    print(f"Max items per Reporting Form: {form_counts.max()}")

def generate_summary_report(df):
    """Generate a summary report of the MDRM data."""
    print("\n=== GENERATING SUMMARY REPORT ===")
    
    # Create a summary report file
    with open('mdrm_summary_report.txt', 'w') as f:
        f.write("MDRM DATA SUMMARY REPORT\n")
        f.write("=======================\n\n")
        f.write(f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("DATASET OVERVIEW\n")
        f.write("-----------------\n")
        f.write(f"Total number of records: {len(df)}\n")
        f.write(f"Number of unique Mnemonics: {df['Mnemonic'].nunique()}\n")
        f.write(f"Number of unique Item Codes: {df['Item Code'].nunique()}\n")
        f.write(f"Number of unique Reporting Forms: {df['Reporting Form'].nunique()}\n\n")
        
        # Convert date columns to datetime if not already
        if not pd.api.types.is_datetime64_dtype(df['Start Date']):
            df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')
        if not pd.api.types.is_datetime64_dtype(df['End Date']):
            df['End Date'] = pd.to_datetime(df['End Date'], errors='coerce')
        
        min_date = df['Start Date'].min()
        max_date = df['End Date'].max()
        f.write(f"Date range: {min_date.strftime('%Y-%m-%d')} to {max_date.strftime('%Y-%m-%d')}\n\n")
        
        active_items = df[df['End Date'].dt.year == 9999]
        f.write(f"Number of currently active items: {len(active_items)} ({len(active_items)/len(df)*100:.2f}%)\n\n")
        
        f.write("MNEMONIC DISTRIBUTION\n")
        f.write("---------------------\n")
        mnemonic_counts = df['Mnemonic'].value_counts()
        f.write("Top 10 most common Mnemonics:\n")
        for mnemonic, count in mnemonic_counts.head(10).items():
            f.write(f"{mnemonic}: {count} items\n")
        f.write("\n")
        
        f.write("ITEM TYPE DISTRIBUTION\n")
        f.write("---------------------\n")
        item_type_counts = df['ItemType'].value_counts()
        for item_type, count in item_type_counts.items():
            f.write(f"{item_type}: {count} items ({count/len(df)*100:.2f}%)\n")
        f.write("\n")
        
        f.write("CONFIDENTIALITY DISTRIBUTION\n")
        f.write("---------------------------\n")
        conf_counts = df['Confidentiality'].value_counts()
        for conf, count in conf_counts.items():
            f.write(f"{conf}: {count} items ({count/len(df)*100:.2f}%)\n")
        f.write("\n")
        
        f.write("CROSS-MNEMONIC ITEMS\n")
        f.write("-------------------\n")
        item_cross_mnemonic = df.groupby('Item Code')['Mnemonic'].nunique().sort_values(ascending=False)
        f.write("Top 10 Item Codes that appear across the most Mnemonics:\n")
        for item_code, count in item_cross_mnemonic.head(10).items():
            item_names = df[df['Item Code'] == item_code]['Item Name'].unique()
            f.write(f"{item_code} ({', '.join(item_names[:1])}): appears in {count} mnemonics\n")
        f.write("\n")
        
        f.write("REPORTING FORM DISTRIBUTION\n")
        f.write("--------------------------\n")
        form_counts = df['Reporting Form'].value_counts()
        f.write("Top 10 most common Reporting Forms:\n")
        for form, count in form_counts.head(10).items():
            if pd.notna(form):
                f.write(f"{form}: {count} items\n")
        f.write("\n")
    
    print(f"Summary report saved to 'mdrm_summary_report.txt'")

def main():
    """Main function to run the analysis."""
    df = load_data()
    basic_stats(df)
    analyze_mnemonics(df)
    analyze_item_types(df)
    analyze_confidentiality(df)
    analyze_item_codes(df)
    analyze_reporting_forms(df)
    generate_summary_report(df)
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
