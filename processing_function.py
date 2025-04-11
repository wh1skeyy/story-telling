import pandas as pd
import matplotlib.pyplot as plt
# Import function bằng lệnh "from processing_function import *"
___all___ = ['pscti', 'acs', 'cavo']


#process_selected_columns_to_int
def pscti(dataframe, column_names):
    """
    Processes the specified columns in the dataframe:
    - Replaces NA values with 0.
    - Replaces non-NA values with 1.
    - Converts the column type to int.
    Parameters:
    dataframe (pd.DataFrame): The dataframe to process.
    column_names (list): List of column names to process.
    Returns:
    pd.DataFrame: The updated dataframe.
    ------------------------------------------------------
    Xử lý các cột được chỉ định trong dataframe:
    - Thay thế các giá trị NA bằng 0.
    - Thay thế các giá trị không phải NA bằng 1.
    - Chuyển kiểu dữ liệu của cột thành kiểu int.
    Tham số:
    - dataframe (pd.DataFrame): DataFrame cần xử lý.
    - column_names (list): Danh sách tên các cột cần xử lý.
    Trả về:
    - pd.DataFrame: DataFrame đã được cập nhật.
    """
    for column_name in column_names:
        if column_name in dataframe.columns:
            dataframe[column_name] = dataframe[column_name].apply(lambda x: 1 if x != 0 else 0).astype(int)
    return dataframe
    # Example usage of the functions
    df = pd.DataFrame(data)
    # Specify columns to process
    column_names = ['A', 'B', 'C']
    # Apply the pscti function
    data = pscti(df, column_names)
    # Print the updated dataframe
    print(data)

#add_columns_sum
def acs(dataframe, columns_to_sum, new_column_name, position=None):
    """
    Sums the values of the specified columns for each row and adds the result as a new column.
    Optionally inserts the new column at the specified position.
    Parameters:
    - dataframe (pd.DataFrame): The dataframe to process.
    - columns_to_sum (list): List of column names to sum.
    - new_column_name (str): Name of the new column to store the sum.
    - position (int, optional): Desired position (zero-indexed) of the new column. 
      If None, the column is added at the end.
    Returns:
    - pd.DataFrame: Updated dataframe with the new column.
    -------------------------------------------------------------------------------------
    Cộng tổng giá trị của các cột được chỉ định cho từng hàng và thêm kết quả vào một cột mới. 
    Tùy chọn chèn cột mới vào vị trí được chỉ định.
    Tham số:
    - dataframe (pd.DataFrame): DataFrame cần xử lý.
    - columns_to_sum (list): Danh sách tên các cột cần cộng tổng.
    - new_column_name (str): Tên của cột mới để lưu trữ tổng giá trị.
    - position (int, optional): Vị trí mong muốn (theo chỉ số bắt đầu từ 0) của cột mới. 
    Nếu là None, cột sẽ được thêm vào cuối.
    Trả về:
    - pd.DataFrame: DataFrame đã được cập nhật với cột mới.
    """
    dataframe[new_column_name] = dataframe[columns_to_sum].sum(axis=1)
    if position is not None:
        cols = list(dataframe.columns)
        cols.remove(new_column_name)
        cols.insert(position, new_column_name)
        dataframe = dataframe[cols]
    return dataframe
    # Example usage of the functions
    df = pd.DataFrame(data)
    # Example 2: Add a new column as the sum of specified columns
    columns_to_sum = ['A', 'B', 'C']
    new_column_name = 'Sum_ABC'
    data = acs(df, columns_to_sum, new_column_name, position=2) # Cột được thêm vào ở vị trí thứ 2
    data.head()



##count_and_visualize_ones
def cavo(dataframe, column_names):
        """
        Counts the number of '1' in the specified columns and visualizes the counts with a bar chart.
        Parameters:
        - dataframe (pd.DataFrame): The dataframe to process.
        - column_names (list): List of column names to count '1's.
        Returns:
        - dict: A dictionary with column names as keys and counts of '1' as values.
        -------------------------------------------------------------------------------
        Đếm số lượng '1' trong các cột được chỉ định và hiển thị biểu đồ cột.
        Tham số:
        - dataframe (pd.DataFrame): DataFrame cần xử lý.
        - column_names (list): Danh sách tên các cột cần đếm số lượng '1'.
        Trả về:
        - dict: Một dictionary với tên cột là key và số lượng '1' là value.
        """
        counts = {col: dataframe[col].sum() for col in column_names if col in dataframe.columns}
        # Visualize the counts with a bar chart
        plt.bar(counts.keys(), counts.values(), color='skyblue')
        plt.xlabel('Columns')
        plt.ylabel('Users Count')
        plt.title('Quantity')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        return counts
        # Example usage of the functions
        df = pd.DataFrame(data)
        # Example 3: Count and visualize the number of '1's in specified columns
        column_names = ['A', 'B', 'C']
        graph1 = cavo(df, column_names)

