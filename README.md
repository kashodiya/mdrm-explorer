# MDRM Explorer

## About the MDRM System
The Micro Data Reference Manual (MDRM) is a catalog of micro and macro data collected from depository institutions and other respondents by the Federal Reserve System. The data are organized into reports, or data series, and consist primarily of financial and structure data. The MDRM documents the labels and values associated with each data item and is designed to assist end users of the microdata.

This repository contains tools for exploring and analyzing the MDRM data.

## Key Concepts

### MDRM Identifier
An MDRM Identifier is an eight-character combination consisting of:
- **Mnemonic** (first 4 characters): Indicates the Reporting Form or overall name of the data collection
- **Item Code** (second 4 characters): Indicates what the specific item is

**Example:** `SVGL2170` refers to total assets on the Thrift Financial Report of Condition.

### Cross-Series Consistency
The same data item always has the same Item Code across different series. For example, Total Assets is always assigned the number `2170` across different series (`RCON2170`, `SVGL2170`, `BHCK2170`).

## Item Types
- **F** = Financial/reported (86.71%): Item is submitted by the reporter
- **D** = Derived (10.13%): Item is derived from other stored variables
- **P** = Percentage (1.12%): Item is stored as a percentage value (e.g., 28% is stored as 28)
- **R** = Rate (1.06%): Item is stored as a decimal value (e.g., 28% is stored as .28)
- **S** = Structure (0.94%): Item describes an institution
- **J** = Projected (0.04%): Item is a projected value with an associated projection period

## Dataset Statistics
- **Total records:** 87,067
- **Unique Mnemonics:** 846
- **Unique Item Codes:** 47,079
- **Unique Reporting Forms:** 181
- **Date range:** 1913-12-23 to 2025-04-30

### Confidentiality Distribution
- **Confidential (Y):** 55.27%
- **Public (N):** 44.73%

## Tools in this Repository

### 1. MDRM Explorer Web Application
The `mdrm_explorer.py` file provides an interactive web interface for exploring the MDRM data. It allows you to:
- Search and filter MDRM data by Mnemonic, Item Code, Item Type, Reporting Form, and Confidentiality
- View detailed information about specific MDRM items
- Visualize statistics about the MDRM data

To run the MDRM Explorer:
```bash
python mdrm_explorer.py
```
Then open your web browser and navigate to http://localhost:56085

### 2. MDRM Analysis Script
The `mdrm_analysis.py` script analyzes the MDRM data and generates statistics and insights. It produces:
- Basic statistics about the dataset
- Analysis of Mnemonics distribution
- Analysis of Item Types distribution
- Analysis of Confidentiality distribution
- Analysis of Item Codes that appear across multiple Mnemonics
- Analysis of Reporting Forms distribution
- A comprehensive summary report

To run the analysis:
```bash
python mdrm_analysis.py
```

### 3. MDRM Summary HTML
The `mdrm_summary.html` file provides a static HTML summary of the MDRM system, including key concepts, statistics, and visualizations.

## Top Mnemonics and Reporting Forms

### Top Mnemonics
1. FXDM: 16,120 items
2. RCON: 10,747 items
3. DERV: 4,995 items
4. RCFD: 4,378 items
5. SVGL: 3,280 items

### Top Reporting Forms
1. FR 3036: 16,120 items
2. FR 2436: 4,995 items
3. FFIEC 031: 4,763 items
4. FR Y-14A: 4,144 items
5. OTS 1313: 3,796 items

## Cross-Mnemonic Items
These Item Codes appear across the most Mnemonics, indicating their importance across different reporting forms:

1. J035 (TOTAL -- RISK-BASED CAPITAL REPORTING): appears in 162 mnemonics
2. J034 (100 DEFAULT): appears in 162 mnemonics
3. 2170 (TOTAL ASSETS): appears in 117 mnemonics

## Microdata Overview
The Federal Reserve System collects various types of data. Individual respondents are provided reporting forms and instructions (either electronically or hard copy) that define the data to be submitted to the Federal Reserve. The forms are each given a number that is preceded by either FR or FFIEC depending on whether they are a Federal Reserve or interagency data collection. Generally speaking, the data are collected by the Federal Reserve Banks and transmitted to the Board via the Federal Reserve’s STAR system. Some data are received from other agencies.

In addition to a reporting form number, each data series is given a four-letter mnemonic, which is used for data transmission and storage. Each variable, within a data series, is assigned a number (usually 4 digits).Combining the series mnemonic and number references a specific data item on a specific series and is known as the MDRM number. For example, SVGL2170 refers to total assets on the Thrift Financial Report of Condition.

Although series mnemonics are unique for each data series, numbers are used across data series to facilitate comparisons between data series. For example, Total Assets is reported on many data series and is always assigned the number 2170. Therefore, RCON2170, SVGL2170, and BHCK2170 all refer to total assets, but on different series.

Some series have sub series and segmented mnemonics. That is, the series itself has one mnemonic for transmission and storage but several mnemonics (prefixes) may be assigned to the various data items. This is done when the same data item is maintained more than one way. For example, on the Bank Call report, RCFD, RCON, and RCFN refer to consolidated data, domestic data, and foreign data, respectively. RCON2170 is domestic total assets and RCFN2170 is total assets of foreign offices. RCFD2170 is total assets of the entire institution, i.e., taking all the domestic and foreign offices as a group. The Report of Deposits (EDDS) is another good example of segmented mnemonics because the same data items are collected as weekly averages and daily values. The weekly average of total deposits (MDRM #2200) is EDD02200 while EDD12200 is the first day of the week's value, EDD22200 is the second day of the week's value, etc. Although segmented mnemonics add some complexity to the data retrieval process, they streamline the numbering methodology and make it easier for end users since the same data item always has the same number.

## Description of the MDRM Manual
The MDRM is broken into two sections. The first is the Reporting Forms and Mnemonics section which includes links to the reporting forms and a brief description of each reporting series. This section also provides a link between the reporting forms public name and the MDRM mnemonic. The second section is the Data Dictionary which defines each data item and shows all of the reporting series on which that item appears.

## Reporting Forms and Mnemonics:
The Reporting Forms and Mnemonics section lists all of the data series defined in the MDRM. Clicking on the 'Main Series' or 'Sub Series' mnemonic displays a series description as a PDF file, which is read by Acrobat Reader. The series description briefly tells about each series and provides a history of changes and other significant information. Clicking on "reporting forms" will provide a link to the list of Agency's websites for the available forms. This section also provides an excellent way to identify which mnemonic goes with a reporting form or vice versa.

- URL for downloading Reporting Forms and Mnemonics: https://www.federalreserve.gov/apps/mdrm/series

## Data Dictionary:
This is the most heavily used portion of the MDRM. The Data Dictionary defines each data item, i.e., each financial or other item that appears on one or more series, and shows all series on which the item appears. It also provides information regarding when the items were available and item descriptions for the item. Additionally there are optional items that can be displayed; item types (financial/reported, structure, rate, examination, percentage or derived), and a short (36 character) title called the data stub. You can also select a check box that will only display confidential items.

The "Reporting Status" section includes radio buttons to allow you to limit your search to only currently opened items or search for opened or closed items during a specific time period.


## What is in the MDRM_CSV.csv file?
The MDRM_CSV.csv file is a machine-readable file of the following metadata elements found in the MDRM Data Dictionary:
 Mnemonic (1st 4 characters)
 Item Code or Item Number (2nd 4 characters)
 Start Date
 End Date
 Item Name
 Confidentiality
 ItemType or Item Type
 Reporting Form
 Description or Item Description
 SeriesGlossary or Mnemonic Glossary

## What is the definition of each of the column headers?

* Mnemonic  First four characters of the MDRM Identifier that indicates the Reporting Form or overall name of the data collection. The MDRM Identifier is an eight character combination of Mnemonic (4 letters) and Item Code or Item Number (4 numbers) assigned to a specific reporting series or reporting form (e.g. SVGL2170 = Total Assets on the Thrift Call Report)

* Item Code or Item Number  Second four characters of the MDRM Identifier that indicates what the specific item is.  If the description of the item is the same across report forms the Item Code or Item Number is used with all those collections. The MDRM Identifier is an eight character combination of Mnemonic (4 letters) and Item Code or Item Number (4 numbers) assigned to a specific reporting series or reporting form (e.g. SVGL2170 = Total Assets on the Thrift Call Report)

* Start Date  Initial calendar date on which the collection of a data item or data collection begins

* End Date  Final calendar date on which the collection of a data item or data collection ends

* Item Name  Label used for an Item Number or Item Code (e.g. Total Assets is the Item Name for Item Number or Item Code 2170) 

* Confidentiality  Binary setting (Y/N) for whether or not a data item can be shared publically 

* Item Type: 
J = Projected; Item is a projected value with an associated projection period.
D = Derived; Item is derived from other stored variables.
F = Financial/reported; Item is submitted by the reporter.
R = Rate; Item is stored as a decimal value. E.g. 28% is stored as .28.
S = Structure; Item describes an institution.
E = Examination/supervision; Item pertains to banking supervision data.
P = Percentage; Item is stored as a percentage value. E.g. 28% is stored as 28. 

* Reporting Form  Presentation of a specific collection of data for financial regulatory reporting

* Description or Item Description  An explanation of what should be reported for a specific item.  This information is generally taken from the reporting form instructions.

* SeriesGlossary or Mnemonic Glossary  Information related to all items which is provided at the mnemonic level rather than the MDRM Identifier level.

How do I open the .csv file using my spreadsheet software?
1. Click on the link to generate the file MDRM_CSV.csv
2. Save the MDRM_CSV.csv file to your own disk
3. Open your spreadsheet software
4. Use the sequence of commands that are the equivalent of FILE > OPEN in your software
5. Browse to find the MDRM_CSV.csv where you saved it on your own disk
6. Choose the MDRM_CSV.csv file and click the equivalent of OPEN in your software

What if I have never, ever opened a .csv file with my spreadsheet software?
1. Click on the link to generate the file MDRM_CSV.csv
2. Save the MDRM_CSV.csv file to your own disk
3. Open your spreadsheet software
4. Use the sequence of commands that are the equivalent of FILE > OPEN in your software
5. Browse to find the MDRM_CSV.csv where you saved it on your own disk
6. Choose the MDRM_CSV.csv file and click the equivalent of OPEN in your software
7. If you have never opened a .csv file with your software, you may need to tell your software that you wish to use a specific program to open the .csv file.  Once you indicate which software program should open the .csv file, your spreadsheet software should be able to open it going forward without having to ask you again.  

* PLEASE NOTE: If the MDRM_CSV.csv file is opened in browser it could take a long time to open with the potential to crash the browser.
