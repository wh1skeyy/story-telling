import pandas as pd
import matplotlib.pyplot as plt

# Import function bằng lệnh "from processing_function import *",
# Nhập 'help()' hoặc 'help("tên func")' để xem hướng dẫn sử dụng.

__all__ = [
    "fhelp",
    "col_format",
    "add_sum_col",
    "cavo",
    "gcbp",
    "vvc",
    "heatmapping",
    "favc",
    "rename_col",
    "replace_na",
]
"""
ĐÂY CHỈ LÀ PHẦN LIỆT KÊ CÁC FUNCTIONS, KHÁ LÀ TRỪU TƯỢNG NÊN CÓ THỂ BỎ QUA. HÃY ĐỌC CÁC PHẦN KÈM VÍ DỤ TỪ DÒNG 50 ĐỂ HIỂU RÕ HƠN
Tên đầy đủ của các hàm và cách sử dụng:
1. process_selected_columns_to_int (col_format) - Nên dùng sau 'rename_col'
Command: col_format(dataframe, column_names)
- Xử lý các cột được chỉ định trong dataframe:
    + Thay thế các giá trị NA bằng 0.
    + Thay thế các giá trị không phải NA bằng 1.
    + Chuyển kiểu dữ liệu của cột thành kiểu int.
2. add_columns_sum (add_sum_col)
Command: add_sum_col(dataframe, columns_to_sum, new_column_name, position=None) #Thay None bằng vị trí mong muốn
    - Cộng tổng giá trị của các cột được chỉ định cho từng hàng và thêm kết quả vào một cột mới.
    - Tùy chọn chèn cột mới vào vị trí được chỉ định.
3. count_and_visualize_ones (cavo)
Command: cavo(dataframe, column_names)
    - Đếm số lượng '1' trong các cột được chỉ định và hiển thị biểu đồ cột.
4. get_columns_by_prefix (gcbp)
Command: gcbp(dataframe, prefix)
    - Lấy tất cả các tên cột trong dataframe bắt đầu bằng tiền tố được chỉ định.
5. visualize_variable_counts (vvc)
Command: vvc(dataframe, column_name, xlabel, ylabel, title)
    - Hiển thị số lần xuất hiện của từng giá trị duy nhất trong cột được chỉ định bằng biểu đồ cột.
6. visualize_heatmap (heatmapping)
Command: heatmapping(dataframe, column_x, column_y, title)
    - Tạo một heatmap dựa trên số lượng cặp giá trị duy nhất trong hai cột được chọn.
7. filter_and_visualize_choices (favc)
Command: favc(dataframe, filter_column, filter_value, question_column, xlabel, ylabel, title)
    - Lọc dataframe dựa trên điều kiện và hiển thị các lựa chọn cho một câu hỏi cụ thể.
8. rename_columns_by_first_unique (rename_col)
Command: rename_col(dataframe, columns, prefix)
    - Đổi tên các cột được chỉ định bằng cách sử dụng giá trị duy nhất không null đầu tiên được tìm thấy trong mỗi cột.
    - Nếu không tìm thấy giá trị duy nhất hợp lệ cho một cột, tên cột sẽ không được thay đổi.

Cuộn xuống từng function để xem chi tiết cách sử dụng.
Vào nhãn Issue để báo lỗi hoặc yêu cầu thêm tính năng hoặc contact thẳng Minh Lê.
Note for developer:
1.  Chạy 'from processing_function import *' lần 2 sẽ báo lỗi, đây là tính năng, không phải bug.
    Để chạy lại, khởi động lại kernel hoặc xóa cache của kernel.
2. fhelp() chỉ hoạt động trong cửa sổ python, không dùng trong cửa sổ markdown.
3. Không cần cài đặt pandas và matplotlib, function tự cài đặt sẵn
"""


def fhelp(function_name=None):

    """
    Hiển thị hướng dẫn sử dụng cho một hàm cụ thể hoặc tất cả các hàm trong module.
    Cách sử dụng:
      fhelp()
         - Hiển thị hướng dẫn cho tất cả các hàm.
      fhelp("col_format")
         - Hiển thị hướng dẫn cho hàm 'col_format'.
    """
    usage = {
        "col_format": (
            "Lệnh: col_format(dataframe, column_names)\n"
            "- Xử lý các cột được chỉ định trong dataframe:\n"
            "    + Thay thế các giá trị NA bằng 0.\n"
            "    + Thay thế các giá trị không phải NA bằng 1.\n"
            "    + Chuyển kiểu dữ liệu của cột thành kiểu int.\n"
            "  Không chạy lệnh 2 lần, chạy lần 2 tất cả biến số sẽ chuyển về 1\n"
            "  Ví dụ:\n"
            "    df = pd.DataFrame(data)\n"
            "    column_names = ['Q7_Part1', 'Q7_Part2']\n"
            "    df = col_format(df, column_names)\n"
        ),
        "add_sum_col": (
            "add_sum_col(dataframe, columns_to_sum, new_column_name, position=None):\n"
            "  - Cộng tổng giá trị của các cột được chỉ định cho từng hàng và thêm kết quả vào một cột mới.\n"
            "  Ví dụ:\n"
            "    df = pd.DataFrame(data)\n"
            "    df = add_sum_col(df, ['Q7_Part1', 'Q7_Part2', 'Q7_Part3'], 'Q7_Total', position=10)\n"
            "    print(df)"
        ),
        "cavo": (
            "cavo(dataframe, column_names):\n"
            "  - Đếm số lượng '1' trong các cột được chỉ định và hiển thị biểu đồ cột.\n"
            "  Ví dụ:\n"
            "    df = pd.DataFrame(data)\n"
            "    counts = cavo(df, ['Q7_Part1', 'Q7_Part2', 'Q7_Part3'])\n"
            "    print(counts)"
        ),
        "gcbp": (
            "gcbp(dataframe, selected_cols, prefix):\n"
            "  - Lấy tất cả các tên cột bắt đầu bằng tiền tố được chỉ định.\n"
            "  Ví dụ:\n"
            "    df = pd.DataFrame(data)\n"
            "    cols = gcbp(df, 'Q7_Part1', 'Q7')\n"
            "    print(cols)"
        ),
        "vvc": (
            "vvc(dataframe, column_name, xlabel, ylabel, title):\n"
            "  - Hiển thị số lần xuất hiện của từng giá trị duy nhất trong cột được chỉ định bằng biểu đồ cột.\n"
            "  Ví dụ:\n"
            "    df = pd.DataFrame(data)\n"
            "    column_name = 'Q5'\n"
            "    vvc(df, column_name, 'Categories', 'Counts', 'Category Count')"
        ),
        "heatmapping": (
            "heatmapping(dataframe, column_x, column_y, title):\n"
            "  - Tạo một heatmap dựa trên số lượng cặp giá trị duy nhất giữa hai cột.\n"
            "  Ví dụ:\n"
            "    df = pd.DataFrame(data)\n"
            "    heatmapping(df, 'Q4', 'Q5', 'Heatmap Example')"
        ),
        "favc": (
            "favc(dataframe, filter_column, filter_value, question_column, xlabel, ylabel, title):\n"
            "  - Lọc dataframe dựa trên điều kiện và hiển thị số lượng giá trị cho một câu hỏi cụ thể.\n"
            "  Ví dụ:\n"
            "    df = pd.DataFrame(data)\n"
            "    favc(df, 'Q7_Part1', '1', 'Q5', 'Choice', 'Count', 'Roles that use Python programming language')"
        ),
        "rename_col": (
            "rename_col(dataframe, columns, prefix):\n"
            "  - Đổi tên các cột được chỉ định bằng giá trị duy nhất không null đầu tiên tìm thấy trong cột đó, kèm theo tiền tố.\n"
            "  Ví dụ:\n"
            "    df = pd.DataFrame(data)\n"
            "    columns = ['Q7_Part1', 'Q7_Part2']\n"
            "    df = rename_col(df, columns, 'Q7_')\n"
            "    print(df)"
        ),
        "replace_na": (
            "replace_na(dataframe, column_name, value):\n"
            "  - Thay thế các giá trị NA trong cột được chỉ định bằng giá trị được cung cấp.\n"
            "  Ví dụ:\n"
            "    df = pd.DataFrame(data)\n"
            "    df = replace_na(df, 'Q5', 'Unknown')\n"
            "    print(df)"
        ),
    }

    if function_name is None:
        print("Hướng dẫn sử dụng cho module processing_function:")
        for func, desc in usage.items():
            print("\n" + desc + "\n" + ("-" * 60))
    else:
        info = usage.get(function_name)
        if info:
            print(info)
        else:
            print(f"Không có thông tin cho hàm '{function_name}'.")


# process_selected_columns_to_int
def col_format(dataframe, column_names):
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
            dataframe[column_name] = (
                dataframe[column_name]
                .apply(lambda x: 1 if pd.notna(x) else 0)
                .astype(int)
            )
    return dataframe
    # Example usage of the functions
    df = pd.DataFrame(data)
    # Specify columns to process
    column_names = ["A", "B", "C"]
    # Apply the col_format function
    data = col_format(df, column_names)
    # Print the updated dataframe
    print(data)


# add_columns_sum
def add_sum_col(dataframe, columns_to_sum, new_column_name, position=None):
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
    columns_to_sum = ["A", "B", "C"]
    new_column_name = "Sum_ABC"
    data = add_sum_col(
        df, columns_to_sum, new_column_name, position=2
    )  # Cột được thêm vào ở vị trí thứ 2
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
    counts = {
        col: dataframe[col].sum() for col in column_names if col in dataframe.columns
    }
    # Visualize the counts with a bar chart
    plt.bar(counts.keys(), counts.values(), color="skyblue")
    plt.xlabel("Columns")
    plt.ylabel("Users Count")
    plt.title("Quantity")
    plt.xticks(rotation="vertical")
    plt.tight_layout()
    plt.show()
    return counts
    # Example usage of the functions
    # df = pd.DataFrame(data)
    # Example 3: Count and visualize the number of '1's in specified columns
    # column_names = ["A", "B", "C"]
    # graph1 = cavo(df, column_names)


# get_columns_by_prefix
def gcbp(dataframe, prefix):
    """
    Retrieves all column names in the dataframe that start with the specified prefix.
    Parameters:
    - dataframe (pd.DataFrame): The dataframe to search.
    - prefix (str): The prefix to match column names.
    Returns:
    - list: A list of column names that start with the specified prefix.
    ---------------------------------------------------------------------
    Lấy tất cả các tên cột trong dataframe bắt đầu bằng tiền tố được chỉ định.
    Tham số:
    - dataframe (pd.DataFrame): DataFrame cần tìm kiếm.
    - prefix (str): Tiền tố để khớp tên cột.
    Trả về:
    - list: Danh sách các tên cột bắt đầu bằng tiền tố được chỉ định.
    """
    if not isinstance(dataframe, pd.DataFrame):
        return "Error: The input 'dataframe' must be a pandas DataFrame."
    if not isinstance(prefix, str):
        return "Error: The input 'prefix' must be a string."
    if dataframe.empty:
        return "Error: The input dataframe is empty."
    if not prefix:
        return "Error: The prefix cannot be empty."

    selected_cols = [col for col in dataframe.columns if col.startswith(prefix)]
    if not selected_cols:
        return f"No columns found starting with the prefix '{prefix}'."
    return selected_cols
    # Example usage
    # df = pd.DataFrame(data)
    # prefix = "Q7"
    # selected_cols = get_columns_by_prefix(df, prefix)
    # print(selected_cols)


# visualize_variable_counts
def vvc(dataframe, column_name, xlabel, ylabel, title, bar_width=0.8, bar_spacing=0.2, angling=45, label_size=10):
    """
    Visualizes the count of each unique value in the specified column with a bar chart.
    Parameters:
    - dataframe (pd.DataFrame): The dataframe to process.
    - column_name (str): The column name to count and visualize.
    - xlabel (str): Label for the x-axis of the chart.
    - ylabel (str): Label for the y-axis of the chart.
    - title (str): Title for the bar chart.
    - bar_width (float, optional): Width of the bars in the chart (default is 0.8).
    - bar_spacing (float, optional): Space between bars in the chart (default is 0.2).
    - angling (int, optional): Angle for the x-axis labels (default is 45).
    - label_size (int, optional): Font size for the labels on the x-axis (default is 10).
    Returns:
    - None
    ---------------------------------------------------------------------
    Hiển thị số lần xuất hiện của từng giá trị duy nhất trong cột được chỉ định bằng biểu đồ cột.
    Tham số:
    - dataframe (pd.DataFrame): DataFrame cần xử lý.
    - column_name (str): Tên cột cần đếm và hiển thị.
    - xlabel (str): Nhãn cho trục x của biểu đồ.
    - ylabel (str): Nhãn cho trục y của biểu đồ.
    - title (str): Tiêu đề cho biểu đồ cột.
    - bar_width (float, optional): Độ rộng của các cột trong biểu đồ (mặc định là 0.8).
    - bar_spacing (float, optional): Khoảng cách giữa các cột trong biểu đồ (mặc định là 0.2).
    - angling (int, optional): Góc nghiêng của nhãn trên trục x (mặc định là 45).
    - label_size (int, optional): Kích thước font chữ cho nhãn trên trục x (mặc định là 10).
    Trả về:
    - None
    """
    if column_name in dataframe.columns:
        value_counts = dataframe[column_name].value_counts()
        indices = range(len(value_counts))
        adjusted_indices = [i * (bar_width + bar_spacing) for i in indices]
        # Visualize the counts with a bar chart
        plt.bar(adjusted_indices, value_counts.values, color="orange", width=bar_width)
        plt.xticks(adjusted_indices, value_counts.index.astype(str), rotation=angling, fontsize=label_size)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.tight_layout()
        plt.show()
    else:
        print(f"Column '{column_name}' not found in the dataframe.")

    # Example usage
    # df = pd.DataFrame(data)
    # column_name = "Q7_1"
    # graph1 = vvc(df, column_name, "X-axis Label", "Y-axis Label", "Chart Title")


# visualize_heatmap
def heatmapping(dataframe, column_x, column_y, title):
    """
    Creates a heatmap based on the counts of unique value pairs in two selected columns.
    Parameters:
    - dataframe (pd.DataFrame): The dataframe to process.
    - column_x (str): The column name for the x-axis.
    - column_y (str): The column name for the y-axis.
    - title (str): Title for the heatmap.
    Returns:
    - None
    ---------------------------------------------------------------------
    Tạo một heatmap dựa trên số lượng cặp giá trị duy nhất trong hai cột được chọn.
    Tham số:
    - dataframe (pd.DataFrame): DataFrame cần xử lý.
    - column_x (str): Tên cột cho trục x.
    - column_y (str): Tên cột cho trục y.
    - title (str): Tiêu đề cho heatmap.
    Trả về:
    - None
    """
    if column_x in dataframe.columns and column_y in dataframe.columns:
        heatmap_data = pd.crosstab(dataframe[column_y], dataframe[column_x])
        plt.figure(figsize=(10, 8))
        plt.imshow(heatmap_data, cmap="viridis", aspect="auto")
        plt.colorbar(label="Count")
        plt.xticks(range(len(heatmap_data.columns)), heatmap_data.columns, rotation=45)
        plt.yticks(range(len(heatmap_data.index)), heatmap_data.index)
        plt.xlabel(column_x)
        plt.ylabel(column_y)
        plt.title(title)
        plt.tight_layout()
        plt.show()
    else:
        print(
            f"One or both columns '{column_x}' and '{column_y}' not found in the dataframe."
        )
    # Example usage
    # df = pd.DataFrame(data)
    # column_x = "Q7_1"
    # column_y = "Q7_2"
    # heatmap1 = visualize_heatmap(df, column_x, column_y)


# filter_and_visualize_choices
def favc(
    dataframe, filter_column, filter_value, question_column, xlabel, ylabel, title
):
    """
    Filters the dataframe based on a condition and visualizes the choices for a specific question.
    Parameters:
    - dataframe (pd.DataFrame): The dataframe to process.
    - filter_column (str): The column to apply the filter on.
    - filter_value (any): The value to filter the column by.
    - question_column (str): The column representing the question to visualize choices for.
    - xlabel (str): Label for the x-axis of the chart.
    - ylabel (str): Label for the y-axis of the chart.
    - title (str): Title for the chart.
    Returns:
    - None
    ---------------------------------------------------------------------
    Lọc dataframe dựa trên điều kiện và hiển thị các lựa chọn cho một câu hỏi cụ thể.
    Tham số:
    - dataframe (pd.DataFrame): DataFrame cần xử lý.
    - filter_column (str): Tên cột để áp dụng bộ lọc.
    - filter_value (any): Giá trị để lọc cột.
    - question_column (str): Tên cột đại diện cho câu hỏi cần hiển thị lựa chọn.
    - xlabel (str): Nhãn cho trục x của biểu đồ.
    - ylabel (str): Nhãn cho trục y của biểu đồ.
    - title (str): Tiêu đề cho biểu đồ.
    Trả về:
    - None
    """
    if filter_column in dataframe.columns and question_column in dataframe.columns:
        filtered_df = dataframe[dataframe[filter_column] == filter_value]
        if not filtered_df.empty:
            value_counts = filtered_df[question_column].value_counts()
            # Visualize the counts with a bar chart
            plt.bar(value_counts.index.astype(str), value_counts.values, color="green")
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.title(title)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            print(f"No data found for {filter_column} = {filter_value}.")
    else:
        print(
            f"One or both columns '{filter_column}' and '{question_column}' not found in the dataframe."
        )


# Example usage
# df = pd.DataFrame(data)
# filter_column = "Q7_1"
# filter_value = "1"
# question_column = "Q5"
# xlabel = "Quantity"
# ylabel = "Title"
# title = "Roles that use Python programming language"
# graph1 = filter_and_visualize_choices(df, filter_column, filter_value, question_column, xlabel, ylabel, title)


# rename_columns_by_first_unique
def rename_col(dataframe, columns, prefix):
    """
    Renames the specified columns using the first non-null unique value found in each column.
    If no valid unique value is found for a column, the column name remains unchanged.
    Parameters:
    - dataframe (pd.DataFrame): The dataframe to process.
    - columns (list): List of column names to rename.
    - prefix (str): Prefix to add to the new column names.
    Returns:
    - pd.DataFrame: DataFrame with columns renamed accordingly.
    ------------------------------------------------------------------
    Đổi tên các cột được chỉ định bằng cách sử dụng giá trị duy nhất không null đầu tiên được tìm thấy trong mỗi cột.
    Nếu không tìm thấy giá trị duy nhất hợp lệ cho một cột, tên cột sẽ không được thay đổi.
    Tham số:
    - dataframe (pd.DataFrame): DataFrame cần xử lý.
    - columns (list): Danh sách các tên cột cần đổi tên.
    - prefix (str): Tiền tố để thêm vào các tên cột mới.
    Trả về:
    - pd.DataFrame: DataFrame với các tên cột đã được đổi tên tương ứng.
    """
    rename_mapping = {}
    for col in columns:
        if col in dataframe.columns:
            # Get the first non-null unique value
            unique_values = dataframe[col].dropna().unique()
            if unique_values.size > 0:
                new_col = unique_values[0]
                # Only rename if the new name is not already a column to avoid conflicts
                if new_col not in dataframe.columns:
                    rename_mapping[col] = prefix + new_col
    return dataframe.rename(columns=rename_mapping)


# Example usage
# df = pd.DataFrame(data)
# columns = ["Q7_Part1", "Q7_Part2"]
# prefix = "Q7_"
# renamed_df = rename_col(df, columns, prefix)
# output -> "Q7_Python", "Q7_R"


# replace_na
def replace_na(dataframe, column_name, value):
    """
    Replaces NA values in the specified column with the given value.
    Parameters:
    - dataframe (pd.DataFrame): The dataframe to process.
    - column_name (str): The column name where NA values will be replaced.
    - value (str or int): The value to replace NA values with.
    Returns:
    - pd.DataFrame: Updated dataframe with NA values replaced.
    ---------------------------------------------------------------------
    Thay thế các giá trị NA trong cột được chỉ định bằng giá trị được cung cấp.
    Tham số:
    - dataframe (pd.DataFrame): DataFrame cần xử lý.
    - column_name (str): Tên cột mà các giá trị NA sẽ được thay thế.
    - value (str hoặc int): Giá trị để thay thế các giá trị NA.
    Trả về:
    - pd.DataFrame: DataFrame đã được cập nhật với các giá trị NA được thay thế.
    """
    if column_name in dataframe.columns:
        dataframe[column_name] = dataframe[column_name].fillna(value)
    else:
        print(f"Column '{column_name}' not found in the dataframe.")
    return dataframe
