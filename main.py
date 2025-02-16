Certainly! Below is a Python program for a project called "Data Privacy Guardian". It provides functionality to anonymize and encrypt personal data in datasets. For simplicity, let's assume we're dealing with CSV files. We'll use libraries like `pandas` for data handling and `cryptography` for encryption. Please make sure to install these libraries using pip if you have not already: `pip install pandas cryptography`.

```python
import pandas as pd
from cryptography.fernet import Fernet
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataPrivacyGuardian:
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            # Generate a new key if none provided
            self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
        logging.info("Data Privacy Guardian Initialized.")

    def encrypt_data(self, data):
        """
        Encrypt the input data using Fernet symmetric encryption.
        :param data: The data to encrypt, must be a string.
        :return: Encrypted byte string.
        """
        try:
            # Fernet works with byte strings, so we need to ensure the data is encoded
            encrypted_data = self.cipher_suite.encrypt(data.encode('utf-8'))
            return encrypted_data
        except Exception as e:
            logging.error(f"Encryption failed: {e}")
            return None

    def anonymize_dataset(self, file_path, sensitive_columns):
        """
        Anonymizes specified columns in the dataset.
        :param file_path: Path to the CSV file to process.
        :param sensitive_columns: List of column names to anonymize.
        :return: None
        """
        try:
            df = pd.read_csv(file_path)
            for column in sensitive_columns:
                if column in df.columns:
                    logging.info(f"Anonymizing column: {column}")
                    df[column] = df[column].apply(lambda x: self.encrypt_data(str(x)))
                else:
                    logging.warning(f"Column {column} not found in the dataset.")
            
            # Save the anonymized dataset to a new file
            output_file_path = file_path.replace(".csv", "_anonymized.csv")
            df.to_csv(output_file_path, index=False)
            logging.info(f"Anonymized dataset saved to {output_file_path}")
        except FileNotFoundError:
            logging.error("The specified file was not found.")
        except Exception as e:
            logging.error(f"An error occurred while anonymizing the dataset: {e}")

def main():
    # Example usage
    guardian = DataPrivacyGuardian()

    # Specify the path to the CSV file and the sensitive columns to anonymize
    file_path = 'path_to_your_dataset.csv'  # Change this to your dataset file path
    sensitive_columns = ['name', 'email', 'phone_number']  # Replace with actual sensitive columns

    guardian.anonymize_dataset(file_path, sensitive_columns)

if __name__ == "__main__":
    main()
```

### Key Features:
1. **Encryption**: Uses `cryptography`'s Fernet library for encrypting data.
2. **Anonymization**: Reads a dataset from a CSV file, encrypts specified columns, and writes the output to a new file.
3. **Error Handling**: Catches and logs different types of exceptions including file not found and encryption errors.
4. **Logging**: Provides clear logging messages for different stages of the program for ease of tracking operations and troubleshooting.

### Important:
- Update `file_path` and `sensitive_columns` with actual paths and column names relevant to your dataset.
- Keep your encryption keys secure, as they are required to decrypt the data later.