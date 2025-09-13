# MDRM Explorer

## Overview

This tool provides an interactive web interface for exploring the Micro Data Reference Manual (MDRM) data. The MDRM is a comprehensive catalog of micro and macro data collected from depository institutions and other respondents by the Federal Reserve System.

## About the MDRM System

The Micro Data Reference Manual (MDRM) is a catalog of micro and macro data collected from depository institutions and other respondents. The data are organized into reports, or data series, and consist primarily of financial and structure data. The MDRM documents the labels and values associated with each data item and is designed to assist end users of the microdata.

### Key Concepts

1. **MDRM Identifier**: An eight-character combination consisting of:
   - **Mnemonic** (first 4 characters): Indicates the Reporting Form or overall name of the data collection
   - **Item Code** (second 4 characters): Indicates what the specific item is

2. **Example**: SVGL2170 refers to total assets on the Thrift Financial Report of Condition

3. **Cross-Series Consistency**: The same data item always has the same Item Code across different series. For example, Total Assets is always assigned the number 2170 across different series (RCON2170, SVGL2170, BHCK2170).

### Item Types

- **F** = Financial/reported: Item is submitted by the reporter
- **D** = Derived: Item is derived from other stored variables
- **P** = Percentage: Item is stored as a percentage value (e.g., 28% is stored as 28)
- **R** = Rate: Item is stored as a decimal value (e.g., 28% is stored as .28)
- **S** = Structure: Item describes an institution
- **J** = Projected: Item is a projected value with an associated projection period
- **E** = Examination/supervision: Item pertains to banking supervision data

### Confidentiality

Items are marked as either:
- **N** = Public (can be shared publicly)
- **Y** = Confidential (restricted access)

## Using the MDRM Explorer

The MDRM Explorer provides an interactive interface to search, filter, and explore the MDRM data.

### Features

1. **Search and Filter**:
   - Filter by Mnemonic, Item Code, Item Type, Reporting Form, and Confidentiality
   - Reset filters to start a new search

2. **Results Table**:
   - View filtered results in a paginated table
   - Sort and filter results directly in the table
   - Click on a row to view detailed information

3. **Item Details**:
   - View comprehensive information about a selected item
   - See full descriptions and glossary information

4. **Statistics**:
   - View distribution charts for Mnemonics, Item Types, and Confidentiality

### Running the Explorer

To run the MDRM Explorer:

```bash
python mdrm_explorer.py
```

Then open your web browser and navigate to:
- http://localhost:50008

## Data Structure

The MDRM data is stored in the `MDRM_CSV.csv` file with the following columns:

1. **Mnemonic**: First four characters of the MDRM Identifier
2. **Item Code**: Second four characters of the MDRM Identifier
3. **Start Date**: Initial calendar date on which the collection of a data item begins
4. **End Date**: Final calendar date on which the collection of a data item ends
5. **Item Name**: Label used for an Item Number or Item Code
6. **Confidentiality**: Binary setting (Y/N) for whether or not a data item can be shared publicly
7. **ItemType**: Categorizes the type of item (F, D, P, R, S, J, E)
8. **Reporting Form**: Presentation of a specific collection of data for financial regulatory reporting
9. **Description**: An explanation of what should be reported for a specific item
10. **SeriesGlossary**: Information related to all items which is provided at the mnemonic level

## Additional Resources

For more information about the MDRM system, visit:
- [Federal Reserve MDRM Series](https://www.federalreserve.gov/apps/mdrm/series)
