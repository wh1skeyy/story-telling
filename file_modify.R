# Load necessary library
library(dplyr)

# Read the CSV file into a dataframe
data <- read.csv("Data_Storage\\kaggle_survey_2020_responses.csv", stringsAsFactors = FALSE)

# Replace all occurrences of 'None' with 'No/None'
data <- data %>% mutate_all(~ gsub("None", "No/None", .))

# Save the modified dataframe back to a CSV file (optional)
write.csv(data, "Data_Storage\\kaggle_survey_2020_responses_modified.csv", row.names = FALSE)