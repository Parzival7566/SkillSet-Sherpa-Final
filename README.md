# Career Guidance System

## Overview

This Career Guidance System is a Flask-based web application designed to help 10th-grade students explore future career options based on their academic performance and aptitude. The system combines OCR technology for processing marksheets, an aptitude test, and AI-powered analysis to provide personalized career recommendations.

## Features

- **Marksheet Upload**: Users can upload their academic marksheets in PDF format.
- **OCR Processing**: Utilizes EasyOCR to extract data from uploaded marksheets.
- **Aptitude Test**: Includes a 20-question aptitude test based on the RIASEC model.
- **AI-Powered Analysis**: Leverages the LlamaAPI to analyze student data and generate career recommendations.
- **Responsive Web Interface**: User-friendly interface for easy interaction with the system.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript (assumed)
- **OCR**: EasyOCR
- **Data Processing**: Pandas, OpenPyXL
- **AI Integration**: LlamaAPI

## Setup and Installation

1. Clone the repository
2. Install required dependencies:
   ```
   pip install flask llamaapi img2table pandas openpyxl
   ```
3. Set up your LlamaAPI key in the code
4. Run the application:
   ```
   python app.py
   ```

## How It Works

1. **Marksheet Upload**: Users upload their marksheet PDF.
2. **Data Extraction**: The system processes the PDF, extracts relevant information, and saves it as CSV.
3. **Aptitude Test**: Users complete a 20-question aptitude test.
4. **Data Analysis**: The system combines marksheet data with aptitude test results.
5. **AI Processing**: LlamaAPI analyzes the combined data to generate career recommendations.
6. **Results Display**: The system presents personalized career guidance to the user.

## Future Enhancements

- Integration with more educational resources
- Expanded aptitude test options
- Mobile app development
- Integration with career counseling services

## Contributors

Kanishk Arya, Vedant Deshmukh, Saahil Tamboli, Ketaki Dabade, Anushka Wani, Sakshi Ubale
