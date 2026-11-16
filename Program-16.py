

import traceback


# Custom Exception Classes
class FileProcessingError(Exception):
    pass


class InvalidFileFormatError(FileProcessingError):
    pass


class EmptyFileError(FileProcessingError):
    pass


def process_file(filename):
    file = None

    try:
        file = open(filename, "r")

        print("File opened successfully.")

        data = file.read()

        if not data:
            raise EmptyFileError("The file is empty.")

        if not filename.endswith(".txt"):
            raise InvalidFileFormatError("Invalid file format.")

        print("\nFile Content:")
        print(data)

    except FileNotFoundError:
        print("Error: File not found.")

    except EmptyFileError as e:
        print("Error:", e)
        traceback.print_exc()

    except InvalidFileFormatError as e:
        print("Error:", e)
        traceback.print_exc()

    except Exception as e:
        print("Unexpected Error:", e)
        traceback.print_exc()

    else:
        print("\nFile processed successfully.")

    finally:
        if file is not None:
            file.close()
            print("\nFile closed successfully.")
        else:
            print("\nNo file was opened.")


# Main Program
filename = input("Enter file name: ")
process_file(filename)
