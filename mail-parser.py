import os
import json
import extract_msg
import argparse
from datetime import datetime

def extract_emails(mail_dir, attachments_root, output_dir, skip_extensions=None):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # List to store extracted email data
    email_data = []

    # Convert skip_extensions into a set of lowercased extensions for faster lookups
    skip_extensions_set = set(ext.lower() for ext in skip_extensions) if skip_extensions else set()

    # Process each .msg file in the given directory
    for filename in os.listdir(mail_dir):
        if filename.endswith(".msg"):
            msg_path = os.path.join(mail_dir, filename)
            msg = extract_msg.Message(msg_path)

            # Use msg.date directly if it's already a datetime object
            email_datetime = msg.date if isinstance(msg.date, datetime) else None
            formatted_date = email_datetime.strftime("%Y-%m-%d_%H-%M-%S") if email_datetime else "unknown_date"

            # Prepare to collect attachments
            attachments = []
            email_attachment_dir = None  # We will create this only if there are attachments

            for attachment in msg.attachments:
                # Check if the attachment has a valid filename and isn't in the skip list
                if attachment.longFilename and not any(attachment.longFilename.lower().endswith(ext) for ext in skip_extensions_set):
                    # Create the attachment folder only if necessary
                    if email_attachment_dir is None:
                        email_attachment_dir = os.path.join(attachments_root, formatted_date)
                        os.makedirs(email_attachment_dir, exist_ok=True)

                    attachment_path = os.path.join(email_attachment_dir, attachment.longFilename)
                    with open(attachment_path, "wb") as att_file:
                        att_file.write(attachment.data)
                    attachments.append(attachment_path)
                elif attachment.longFilename:
                    print(f"Skipping attachment with extension in skip list: {attachment.longFilename}")

            # Only add the email to the JSON if there are attachments or other data to include
            email_entry = {
                "date": email_datetime.strftime("%Y-%m-%d %H:%M:%S") if email_datetime else "Unknown",
                "time": email_datetime.strftime("%H:%M:%S") if email_datetime else "unknown_time",
                "sender": msg.sender,
                "recipient_to": msg.to,
                "recipient_cc": msg.cc,
                "subject": msg.subject,
                "body": msg.body if msg.body else msg.htmlBody,  # Prefer text, fallback to HTML
                "attachments": attachments,
                "filename": filename
            }

            email_data.append(email_entry)

    # Save extracted data to JSON in the specified output folder
    output_json = os.path.join(output_dir, "extracted_emails.json")
    with open(output_json, "w", encoding="utf-8") as json_file:
        json.dump(email_data, json_file, indent=4, ensure_ascii=False)

    print(f"Extraction complete! Data saved to {output_json}")

# Command-line argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract metadata and content from .msg email files.")
    parser.add_argument("mail_folder", help="Path to the folder containing .msg files")
    parser.add_argument("attachments_folder", help="Root folder for saving attachments")
    parser.add_argument("output_folder", help="Folder where the extracted JSON file will be saved")
    parser.add_argument("--skip-extensions", help="Comma-separated list of extensions to skip (e.g. .gif,.png)")

    args = parser.parse_args()

    # Split the skip extensions argument into a list if provided
    skip_extensions = args.skip_extensions.split(",") if args.skip_extensions else None

    extract_emails(args.mail_folder, args.attachments_folder, args.output_folder, skip_extensions)
