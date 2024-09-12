import pandas as pd
import os
import warnings

# Suppress all warnings, including DtypeWarning
warnings.filterwarnings('ignore')

# Path to the directory containing your files
directory_path = r'C:\Users\Raghad\Desktop\archive'

# List of file extensions for different file types
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')
video_extensions = ('.mp4', '.avi', '.mkv', '.mov', '.flv')
csv_extensions = ('.csv',)
graph_extensions = ('.svg', '.eps', '.pdf')

def determine_data_type(file_path):
    try:
        # Handle CSV files
        if file_path.endswith(csv_extensions):
            # Load the entire .csv file and suppress warnings
            df = pd.read_csv(file_path, low_memory=False)  # Read all rows and let pandas infer types

            # Determine the types of data in each column
            data_types = df.dtypes

            # Determine overall data type for the file
            if data_types.apply(lambda x: pd.api.types.is_string_dtype(x)).any():
                data_type = 'Textual'
            elif data_types.apply(lambda x: pd.api.types.is_numeric_dtype(x)).any():
                data_type = 'Numerical'
            else:
                data_type = 'Mixed'
        
        # Handle image files
        elif file_path.endswith(image_extensions):
            data_type = 'Image'

        # Handle video files
        elif file_path.endswith(video_extensions):
            data_type = 'Video'
        
        # Handle graph files (usually vector formats or PDFs)
        elif file_path.endswith(graph_extensions):
            data_type = 'Graph'
        
        else:
            data_type = 'Unknown'
        
        return {
            "file": file_path,
            "data_type": data_type
        }
    except pd.errors.EmptyDataError:
        return {"file": file_path, "data_type": "Empty"}
    except pd.errors.ParserError:
        return {"file": file_path, "data_type": "Error Parsing"}
    except Exception as e:
        return {"file": file_path, "data_type": f"Error: {str(e)}"}

def analyze_directory(directory_path):
    summaries = []
    for filename in os.listdir(directory_path):
        # Skip directories
        if not os.path.isfile(os.path.join(directory_path, filename)):
            continue

        file_path = os.path.join(directory_path, filename)
        summary = determine_data_type(file_path)
        summaries.append(summary)

    return summaries

# Run the analysis
summaries = analyze_directory(directory_path)

# Print summaries for inspection
for summary in summaries:
    print(summary)

