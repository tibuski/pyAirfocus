# Excel Report Generator for Field Status Analysis

This script processes JSON files containing workspace field status data and creates comprehensive, professionally styled Excel reports with advanced formatting and visual analysis features.

## ✨ Features

### Data Analysis
- **Workspace Totals**: Filled fields, unset fields, total items, unique fields
- **Field Statistics**: True/false counts for each field type
- **Status Distribution**: Counts of different status types across workspaces
- **Hierarchical Organization**: Data organized by clusters and workspaces

### Visual Enhancements
- **🎨 Modern Orange Theme**: Professional styling across all sheets
- **📊 Conditional Formatting**: Pastel color coding for key metrics
- **📋 Clean Typography**: Segoe UI font with optimized sizing
- **🔄 Alternating Rows**: Enhanced readability with subtle color alternation
- **📐 Auto-sizing**: Automatic column width adjustment

### User Experience
- **🥇 Summary First**: Summary Totals sheet as the default first tab
- **📝 Clean Names**: No underscores in column or sheet names
- **🎯 Intuitive Layout**: Logical sheet ordering for better workflow

## 📊 Output Sheets

The Excel file contains 4 professionally styled sheets:

1. **Summary Totals** - 🏆 Key metrics with conditional formatting (first tab)
2. **Status Counts** - 📈 Distribution of item statuses per workspace  
3. **Field Statistics** - 📋 True/false counts for each field type per workspace
4. **Complete Data** - 🗂️ All extracted data in one comprehensive view (last tab)

## 🎨 Visual Features

### Conditional Formatting (Summary Totals)
- **Total Filled Fields**: Pastel red → yellow → green gradient
- **Total Unset Fields**: Pastel green → yellow → red gradient (inverted)
- **Eye-friendly**: Soft pastel colors for comfortable viewing

### Modern Orange Theme
- **Headers**: Vibrant orange background (`#FF8C42`) with white text
- **Alternating Rows**: Light orange tint (`#FFF4E6`) for better readability
- **Typography**: Segoe UI font family for modern appearance
- **Borders**: Subtle light gray borders for clean separation

## 📦 Installation

1. Install the required dependencies:
```bash
pip install -r requirements_excel.txt
```

Or install manually:
```bash
pip install pandas openpyxl
```

## 🚀 Usage

### Command Line Interface

The script supports flexible command line arguments:

```bash
# Basic usage
python create_excel_report.py input_file.json output_report.xlsx

# Examples
python create_excel_report.py Era.json EraDashboard.xlsx
python create_excel_report.py field_statuses.json analysis_report.xlsx

# With verbose output
python create_excel_report.py data.json report.xlsx -v

# Get help
python create_excel_report.py -h
```

### Parameters

- **`json_file`** (required): Path to the input JSON file containing workspace data
- **`excel_file`** (required): Path for the output Excel report file
- **`-v, --verbose`** (optional): Enable verbose output for detailed processing information

## 📋 Data Structure

### Column Names (Clean Format)

**Basic Information:**
- **Cluster**: The main cluster name
- **Workspace**: The workspace name within the cluster  
- **Full Path**: Complete hierarchical path (Cluster > Workspace)

**Summary Metrics:**
- **Total Filled Fields**: Number of fields set to true (with conditional formatting)
- **Total Unset Fields**: Number of fields set to false (with conditional formatting)
- **Total Items**: Total number of items in workspace
- **Total Unique Fields**: Number of unique field types

**Detailed Statistics:**
- **[FieldName] True**: Count of items where this field is true
- **[FieldName] False**: Count of items where this field is false
- **Status [StatusName]**: Count of items with each status type

## 📊 Example Output

### Console Output
The script provides clear progress updates and summary statistics:

```
Loading JSON data...
Extracting workspace data...
Found 9 workspaces
Creating Excel report...
Excel report created successfully: EraDashboard.xlsx

Report contains the following sheets:
1. Summary Totals - Workspace totals only
2. Status Counts - Item status distribution  
3. Field Statistics - Field true/false counts
4. Complete Data - All extracted data

Summary Statistics:
Total workspaces: 9
Total items across all workspaces: 240
Total filled fields: 530
Total unset fields: 2350
```

### Excel Output Features

- **🎨 Professional Styling**: Modern orange theme across all sheets
- **📊 Smart Formatting**: Conditional formatting highlights important data patterns
- **📋 Organized Layout**: Logical sheet order with Summary Totals as the first tab
- **🔍 Easy Navigation**: Clean sheet names without underscores
- **📐 Optimized Display**: Auto-adjusted column widths for best readability

## 🔧 Advanced Features

### Conditional Formatting Logic
- **High Performance**: Green shades indicate good completion rates
- **Attention Needed**: Red shades highlight areas requiring focus
- **Balanced View**: Yellow shades show moderate performance
- **Intuitive Colors**: Pastel tones for comfortable extended viewing

### Modern Design Elements
- **Typography**: Segoe UI font for modern, professional appearance
- **Color Harmony**: Orange-based theme with complementary accent colors
- **Visual Hierarchy**: Clear distinction between headers and data
- **Accessibility**: High contrast ratios for excellent readability

## 🛠️ Troubleshooting

### Common Issues
- **File Not Found**: Ensure the JSON file path is correct and accessible
- **Permission Error**: Check write permissions in the output directory
- **Import Error**: Verify all dependencies are installed: `pip install pandas openpyxl`
- **Memory Issues**: For very large datasets, ensure sufficient RAM is available

### Best Practices
- Use descriptive output filenames for better organization
- Run with `-v` flag for detailed processing information
- Ensure JSON files are valid before processing
- Keep backup copies of important data files

## 📈 Performance Tips

- **File Size**: The script efficiently handles large datasets with thousands of workspaces
- **Processing Speed**: Optimized algorithms for fast data extraction and formatting
- **Memory Usage**: Efficient pandas operations minimize memory footprint
- **Output Quality**: Balanced between comprehensive data and file size optimization
