library(DBI)
library(RMySQL)
library(ggplot2)

# Connect to MySQL database
conn <- dbConnect(RMySQL::MySQL(),
                  dbname = "****",
                  host = "****",
                  user = "****",
                  password = "****")

# Fetch data for all companies
aapl_data <- dbGetQuery(conn, "SELECT Date, Close FROM AAPL")
tsla_data <- dbGetQuery(conn, "SELECT Date, Close FROM TSLA")
googl_data <- dbGetQuery(conn, "SELECT Date, Close FROM GOOGL")

# Combine data for plotting
aapl_data$Company <- "Apple"
tsla_data$Company <- "Tesla"
googl_data$Company <- "Google"

all_data <- rbind(aapl_data, tsla_data, googl_data)

# Plot the data
ggplot(all_data, aes(x = as.Date(Date), y = Close, color = Company)) +
  geom_line(size = 1) +
  labs(title = "Stock Prices Over Time", x = "Date", y = "Closing Price") +
  theme_minimal()
