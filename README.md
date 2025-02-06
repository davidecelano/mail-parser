# mail-parser

## What the Code Does

The `mail-parser.py` script extracts metadata and content from `.msg` email files. It processes each `.msg` file in a specified directory, extracts relevant information such as the sender, recipients, subject, body, and attachments, and saves the extracted data in a JSON file. The script also allows you to skip certain file extensions when processing attachments.

## Usage

To run the script, use the following command-line arguments:

| Argument            | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `mail_folder`       | Path to the folder containing `.msg` files.                                  |
| `attachments_folder`| Root folder for saving attachments.                                          |
| `output_folder`     | Folder where the extracted JSON file will be saved.                          |
| `--skip-extensions` | Comma-separated list of extensions to skip (e.g. `.gif,.png`). This argument is optional. |

Example usage:
```sh
python mail-parser.py <mail_folder> <attachments_folder> <output_folder> [--skip-extensions <extensions>]
```

Replace `<mail_folder>`, `<attachments_folder>`, and `<output_folder>` with the appropriate paths. The `--skip-extensions` argument is optional and allows you to specify file extensions to skip when processing attachments.

## Environment Setup

To set up the environment and install dependencies for this project, follow these steps:

| Step | Description                                                                 |
|------|-----------------------------------------------------------------------------|
| 1    | Ensure you have Python installed on your system. You can download it from the official Python website. |
| 2    | Open a terminal or command prompt.                                           |
| 3    | Navigate to the root directory of the project where the `mail-parser.py` file is located. |
| 4    | Install the required dependencies using the following command:               |
|      | ```sh                                                                       |
|      | pip install extract_msg                                                     |
|      | ```                                                                         |
| 5    | Verify that the dependencies are installed correctly by running the script with the `--help` option: |
|      | ```sh                                                                       |
|      | python mail-parser.py --help                                                |
|      | ```                                                                         |

This will ensure that the necessary dependencies are installed and the script can run without issues.

## Running the Script on a Windows Client

To run the script on a Windows client, follow these steps:

| Step | Description                                                                 |
|------|-----------------------------------------------------------------------------|
| 1    | Ensure you have Python installed on your system. You can download it from the official Python website. |
| 2    | Open a terminal or command prompt.                                           |
| 3    | Navigate to the root directory of the project where the `mail-parser.py` file is located. |
| 4    | Install the required dependencies using the following command:               |
|      | ```sh                                                                       |
|      | pip install extract_msg                                                     |
|      | ```                                                                         |
| 5    | Verify that the dependencies are installed correctly by running the script with the `--help` option: |
|      | ```sh                                                                       |
|      | python mail-parser.py --help                                                |
|      | ```                                                                         |
| 6    | Run the script with the required command-line arguments:                     |
|      | ```sh                                                                       |
|      | python mail-parser.py <mail_folder> <attachments_folder> <output_folder> [--skip-extensions <extensions>] |
|      | ```                                                                         |
|      | Replace `<mail_folder>`, `<attachments_folder>`, and `<output_folder>` with the appropriate paths. The `--skip-extensions` argument is optional and allows you to specify file extensions to skip when processing attachments. |

This will ensure that the script runs correctly on a Windows client.
