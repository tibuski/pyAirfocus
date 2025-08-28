# Excel Report Generator for Field Status Analysis

This script processes the `field_statuses.json` file and creates a comprehensive Excel report with workspace analysis.

## Features

The script extracts and analyzes:
- Workspace totals (true fields, false fields, total items, unique fields)
- Field statistics (true/false counts for each field type)
- Status distribution (counts of different status types)
- Hierarchical organization by clusters and workspaces

## Output

The Excel file contains 4 sheets:
1. **Complete_Data** - All extracted data in one comprehensive view
2. **Summary_Totals** - Workspace-level totals only
3. **Status_Counts** - Distribution of item statuses per workspace
4. **Field_Statistics** - True/false counts for each field type per workspace

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements_excel.txt
```

Or install manually:
```bash
pip install pandas openpyxl
```

## Usage

1. Ensure `field_statuses.json` is in the same directory as the script
2. Run the script:
```bash
python create_excel_report.py
```

3. The script will create `workspace_analysis_report.xlsx` with the analyzed data

## Output Structure

### Columns in the Excel report:

**Basic Information:**
- Cluster: The main cluster name
- Workspace: The workspace name within the cluster
- Full_Path: Complete path (Cluster > Workspace)

**Totals:**
- Total_True_Fields: Number of fields set to true
- Total_False_Fields: Number of fields set to false
- Total_Items: Total number of items in workspace
- Total_Unique_Fields: Number of unique field types

**Field Statistics (for each field type):**
- [FieldName]_True: Count of items where this field is true
- [FieldName]_False: Count of items where this field is false

**Status Counts:**
- Status_[StatusName]: Count of items with each status

## Example Output

The script will show progress and summary statistics:
```
Loading JSON data...
Extracting workspace data...
Found 9 workspaces
Creating Excel report...
Excel report created successfully: workspace_analysis_report.xlsx

Summary Statistics:
Total workspaces: 9
Total items across all workspaces: 240
Total true fields: 530
Total false fields: 2350
```

## Troubleshooting

- Ensure the JSON file exists and is valid
- Check that you have write permissions in the directory
- Make sure all dependencies are installed correctly
