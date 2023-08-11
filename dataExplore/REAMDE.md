# DataExplorer Class

The **DataExplorer** class is designed to facilitate exploratory data analysis and visualization for your datasets. It provides a set of methods that allow you to quickly generate useful insights into your data. This class is particularly useful when you want to gain a preliminary understanding of your data's characteristics, distributions, and correlations.

## Installation

To use the **DataExplorer** class, make sure you have the necessary libraries installed:

```bash
pip install pandas matplotlib seaborn numpy
```

## Usage

1. Import the required libraries and define your dataset file name.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Define your dataset file name
file_name = 'your_dataset.csv'  # Change this to your actual file name
```

2. Instantiate the **DataExplorer** class by passing the dataset file name.

```python
from pa27_dataexplorer import DataExplorer

explorer = DataExplorer(file_name)
```

3. Explore your data using the available methods:

### Summary

Get a summary of the dataset's shape and column list.

```python
summary = explorer.summary()
print(summary)
```

### Histogram

Generate histograms for numerical columns.

```python
explorer.histogram()
```

### Heatmap

Visualize the correlation between numerical columns using a heatmap.

```python
explorer.heat_map()
```

### Missing Data Info

Display information about missing data in columns.

```python
missing_info = explorer.missing_data_info()
print(missing_info)
```

### Detect Outliers

Work in progress: Method for detecting outliers.

```python
# Call the method once it's implemented
# explorer.detect_outliers()
```

### Create Dashboard

Work in progress: Method for creating an interactive dashboard.

```python
# Call the method once it's implemented
# explorer.create_dashboard()
```

## Example

Here's a quick example of how to use the **DataExplorer** class:

```python
# Import libraries and define your dataset file name
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pa27_dataexplorer import DataExplorer

file_name = 'your_dataset.csv'  # Change this to your actual file name

# Instantiate the DataExplorer class
explorer = DataExplorer(file_name)

# Get summary
summary = explorer.summary()
print(summary)

# Generate histograms
explorer.histogram()

# Visualize correlation using a heatmap
explorer.heat_map()

# Display missing data information
missing_info = explorer.missing_data_info()
print(missing_info)
```

## Contributing

Contributions are welcome! If you find any issues or want to enhance the capabilities of the **DataExplorer** class, feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
