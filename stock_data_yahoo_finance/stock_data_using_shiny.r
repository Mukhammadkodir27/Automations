# Install necessary libraries if not already installed

library(DBI)
library(RMySQL)
library(ggplot2)
library(shiny)

# Connect to MySQL database
conn <- dbConnect(RMySQL::MySQL(),
                  dbname = "stock_data",
                  host = "localhost",
                  user = "root",  # Adjust according to your credentials
                  password = "Polska123#")

# Fetch data from the database
aapl_data <- dbGetQuery(conn, "SELECT Date, Close FROM AAPL")
tsla_data <- dbGetQuery(conn, "SELECT Date, Close FROM TSLA")
googl_data <- dbGetQuery(conn, "SELECT Date, Close FROM GOOGL")

# Convert the Date column to Date type
aapl_data$Date <- as.Date(aapl_data$Date)
tsla_data$Date <- as.Date(tsla_data$Date)
googl_data$Date <- as.Date(googl_data$Date)

# Shiny UI
ui <- fluidPage(
  titlePanel("Stock Prices Over Time"),
  
  sidebarLayout(
    sidebarPanel(
      # Dropdown for selecting the year
      selectInput("year", "Select Year", 
                  choices = unique(format(aapl_data$Date, "%Y")), 
                  selected = "2023"),
      
      # Dropdown for selecting months
      selectInput("month", "Select Month", 
                  choices = month.name, 
                  selected = "January")
    ),
    
    mainPanel(
      plotOutput("stockPlot")
    )
  )
)

# Shiny Server logic
server <- function(input, output) {
  
  # Reactive data based on year and month selected
  filtered_data <- reactive({
    selected_year <- input$year
    selected_month <- which(month.name == input$month)
    
    # Filter the data for the selected year and month
    filtered_aapl <- aapl_data[format(aapl_data$Date, "%Y") == selected_year & 
                                 format(aapl_data$Date, "%m") == sprintf("%02d", selected_month), ]
    
    filtered_tsla <- tsla_data[format(tsla_data$Date, "%Y") == selected_year & 
                                 format(tsla_data$Date, "%m") == sprintf("%02d", selected_month), ]
    
    filtered_googl <- googl_data[format(googl_data$Date, "%Y") == selected_year & 
                                   format(googl_data$Date, "%m") == sprintf("%02d", selected_month), ]
    
    # Combine the data
    all_data <- rbind(
      data.frame(filtered_aapl, Company = "Apple"),
      data.frame(filtered_tsla, Company = "Tesla"),
      data.frame(filtered_googl, Company = "Google")
    )
    
    return(all_data)
  })
  
  # Plot the data
  output$stockPlot <- renderPlot({
    data <- filtered_data()
    
    ggplot(data, aes(x = Date, y = Close, color = Company)) +
      geom_line(size = 1) +
      labs(title = paste("Stock Prices in", input$month, input$year),
           subtitle = "Closing Price of Apple, Tesla, and Google",
           x = "Date",
           y = "Closing Price (USD)",
           caption = "Data source: Yahoo Finance") +
      theme_minimal() +
      theme(legend.title = element_blank(),
            legend.position = "top")
  })
}

# Run the Shiny app
shinyApp(ui = ui, server = server)
