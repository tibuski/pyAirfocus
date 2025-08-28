import json
import pandas as pd
from collections import defaultdict
import os

def load_json_data(file_path):
    """Load JSON data from file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def extract_workspace_data(data):
    """Extract workspace data and create a structured dataset"""
    workspaces = []
    
    # Skip _GLOBAL_TOTALS and process cluster data
    for cluster_key, cluster_data in data.items():
        if cluster_key == "_GLOBAL_TOTALS":
            continue
            
        # Handle nested structure (cluster > workspace)
        for workspace_key, workspace_data in cluster_data.items():
            workspace_info = {
                'Cluster': cluster_key,
                'Workspace': workspace_key,
                'Full_Path': f"{cluster_key} > {workspace_key}"
            }
            
            # Extract workspace totals if available
            if '_WORKSPACE_TOTALS' in workspace_data:
                totals = workspace_data['_WORKSPACE_TOTALS']
                workspace_info.update({
                    'Total_True_Fields': totals.get('total_true_fields', 0),
                    'Total_False_Fields': totals.get('total_false_fields', 0),
                    'Total_Items': totals.get('total_items', 0),
                    'Total_Unique_Fields': totals.get('total_unique_fields', 0)
                })
            else:
                # Initialize with zeros if no totals found
                workspace_info.update({
                    'Total_True_Fields': 0,
                    'Total_False_Fields': 0,
                    'Total_Items': 0,
                    'Total_Unique_Fields': 0
                })
            
            # Extract field statistics and status counts
            field_stats = defaultdict(int)
            status_counts = defaultdict(int)
            all_fields = set()
            
            # Process individual items in the workspace
            for item_key, item_data in workspace_data.items():
                if item_key == '_WORKSPACE_TOTALS':
                    continue
                
                # Count status occurrences
                if '_status' in item_data:
                    status_counts[item_data['_status']] += 1
                
                # Count field true/false occurrences
                for field_key, field_value in item_data.items():
                    if field_key != '_status' and isinstance(field_value, bool):
                        all_fields.add(field_key)
                        if field_value:
                            field_stats[f"{field_key}_True"] += 1
                        else:
                            field_stats[f"{field_key}_False"] += 1
            
            # Add field statistics to workspace info
            workspace_info.update(field_stats)
            
            # Add status counts to workspace info
            for status, count in status_counts.items():
                workspace_info[f"Status_{status.replace(' ', '_')}"] = count
            
            workspaces.append(workspace_info)
    
    return workspaces

def create_excel_report(workspaces_data, output_file):
    """Create Excel report with multiple sheets"""
    
    # Create main dataframe
    df = pd.DataFrame(workspaces_data)
    
    # Fill NaN values with 0 for numeric columns
    numeric_columns = df.select_dtypes(include=['number']).columns
    df[numeric_columns] = df[numeric_columns].fillna(0)
    
    # Create Excel writer
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        
        # Sheet 1: Complete data
        df.to_excel(writer, sheet_name='Complete_Data', index=False)
        
        # Sheet 2: Summary totals only
        summary_cols = ['Cluster', 'Workspace', 'Full_Path', 'Total_True_Fields', 
                       'Total_False_Fields', 'Total_Items', 'Total_Unique_Fields']
        df_summary = df[summary_cols].copy()
        df_summary.to_excel(writer, sheet_name='Summary_Totals', index=False)
        
        # Sheet 3: Status counts
        status_cols = ['Cluster', 'Workspace', 'Full_Path'] + [col for col in df.columns if col.startswith('Status_')]
        if len(status_cols) > 3:  # Only create if status columns exist
            df_status = df[status_cols].copy()
            df_status.to_excel(writer, sheet_name='Status_Counts', index=False)
        
        # Sheet 4: Field statistics (True/False counts)
        field_cols = ['Cluster', 'Workspace', 'Full_Path'] + [col for col in df.columns if col.endswith('_True') or col.endswith('_False')]
        if len(field_cols) > 3:  # Only create if field columns exist
            df_fields = df[field_cols].copy()
            df_fields.to_excel(writer, sheet_name='Field_Statistics', index=False)
        
        # Auto-adjust column widths for all sheets
        for sheet_name in writer.sheets:
            worksheet = writer.sheets[sheet_name]
            for column in worksheet.columns:
                max_length = 0
                column_letter = column[0].column_letter
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                adjusted_width = min(max_length + 2, 50)  # Cap at 50 characters
                worksheet.column_dimensions[column_letter].width = adjusted_width

def main():
    """Main function to process JSON and create Excel report"""
    
    # File paths
    json_file = 'field_statuses.json'
    excel_file = 'workspace_analysis_report.xlsx'
    
    # Check if JSON file exists
    if not os.path.exists(json_file):
        print(f"Error: {json_file} not found in current directory")
        return
    
    try:
        # Load and process data
        print("Loading JSON data...")
        data = load_json_data(json_file)
        
        print("Extracting workspace data...")
        workspaces = extract_workspace_data(data)
        
        print(f"Found {len(workspaces)} workspaces")
        
        # Create Excel report
        print("Creating Excel report...")
        create_excel_report(workspaces, excel_file)
        
        print(f"Excel report created successfully: {excel_file}")
        print("\nReport contains the following sheets:")
        print("1. Complete_Data - All extracted data")
        print("2. Summary_Totals - Workspace totals only")
        print("3. Status_Counts - Item status distribution")
        print("4. Field_Statistics - Field true/false counts")
        
        # Display summary statistics
        df = pd.DataFrame(workspaces)
        print(f"\nSummary Statistics:")
        print(f"Total workspaces: {len(workspaces)}")
        print(f"Total items across all workspaces: {df['Total_Items'].sum()}")
        print(f"Total true fields: {df['Total_True_Fields'].sum()}")
        print(f"Total false fields: {df['Total_False_Fields'].sum()}")
        
    except Exception as e:
        print(f"Error processing data: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
