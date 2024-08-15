# Information-Retrieval-BERT-BM25

This project is a search engine designed to retrieve Indonesian Supreme Court decisions using advanced information retrieval techniques, including BERT embeddings and BM25 models. The application is built using Flask and provides a simple web interface for users to query and filter court decisions based on specific criteria.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Structure](#data-structure)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Contact](#contact)

## About

This repository implements a search engine specifically designed to retrieve and rank Indonesian Supreme Court decisions. By leveraging BERT embeddings and BM25 models, the system is capable of understanding the nuances of legal language and providing accurate and relevant results based on user queries.

## Features

- **Advanced Information Retrieval:** Combines BERT embeddings and BM25 to enhance the accuracy of search results.
- **Custom Dataset:** Utilizes a dataset of Indonesian Supreme Court decisions.
- **Web Interface:** Includes a simple web interface for users to interact with the search engine.
- **Filtering Options:** Users can filter search results by court name and type of verdict.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/rrayhka/information-retrieval-bert-bm25.git
    cd information-retrieval-bert-bm25
    ```

2. Run the model training script:

    ```bash
    python modelling.py
    ```

3. Run the web application:

    ```bash
    python app.py
    ```

## Usage

1. **Accessing the Web Interface:**
   - After running the application, access the web interface by opening your browser and navigating to `http://localhost:5006`.
   
2. **Performing a Search:**
   - Enter a query related to the legal case or keywords of interest.
   - Optionally, select a court name and/or type of verdict to filter the results.
   - Click "Search" to retrieve and rank relevant court decisions based on your query.

3. **Viewing Details:**
   - Click on a search result to view detailed information about the selected court decision.

## Data Structure

The data used in this project consists of structured information from Indonesian Supreme Court decisions. Below is an example of how the data is organized:

```python
decision_1 = [
    '80/pid.b/2014/pn.spg',  # Case Number
    'pengadilan negeri sampang',  # Court Name
    'tingkat pertama,',  # Case Level
    'durrahman al. p. sulaiman;',  # Defendant Name
    'pasal 351 ayat (1) kuhp',  # Violation (Charges)
    'penjara selama 8 (delapan) bulan;',  # Sentence Demand
    'sayyad effendi',  # Witness Name
    'sitina',  # Witness Name
    '21 januari 2014',  # Incident Date
    'dakwaan tunggal',  # Type of Charges
    'pasal 351 ayat (1) kuhp',  # Violation (Charges)
    'pasal 351 ayat (1) kuhp',  # Violation (Legal Consideration)
    'menjatuhkan pidana terhadap terdakwa',  # Type of Verdict
    'penjara selama 5 (lima) bulan;',  # Sentence
    '22 mei 2014',  # Verdict Date
    'satyawati yun irianti, sh., mhum,',  # Presiding Judge
    'heru setiyadi sh.,',  # Member Judge
    'moh. ismail gunawan, sh.,',  # Member Judge
    'oleptaufikurrahman, sh.,',  # Court Clerk
    'heronika setiawaty, sh.,'  # Prosecutor
]
```

### Fields Explanation:

- **Case Number:** The unique identifier for the court decision.
- **Court Name:** The name of the court where the decision was made.
- **Case Level:** The level of the case, such as first instance.
- **Defendant Name:** The name of the defendant in the case.
- **Violation (Charges):** The specific law or regulation the defendant is accused of violating.
- **Sentence Demand:** The punishment sought by the prosecution.
- **Witness Name:** Names of witnesses involved in the case.
- **Incident Date:** The date when the incident occurred.
- **Type of Charges:** The type of charges brought against the defendant.
- **Violation (Legal Consideration):** The law or regulation used as the basis for the court's decision.
- **Type of Verdict:** The type of decision handed down by the court.
- **Sentence:** The final punishment imposed by the court.
- **Verdict Date:** The date when the verdict was delivered.
- **Presiding Judge:** The name of the judge who presided over the case.
- **Member Judge:** The names of the judges who were part of the decision-making panel.
- **Court Clerk:** The name of the court clerk.
- **Prosecutor:** The name of the prosecutor.

## Project Structure

- `app.py`: The main Flask application file that runs the web interface.
- `modelling.py`: Script for training and fine-tuning the BERT and BM25 models.
- `templates/`: HTML templates for the web interface.
- `data/`: Contains the dataset of Indonesian Supreme Court decisions and metadata.
- `requirements.txt`: List of Python dependencies needed to run the application.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to discuss any changes or improvements.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.


## Contact

Akhyar - [khyar075@gmail.com](mailto:khyar075@gmail.com)
