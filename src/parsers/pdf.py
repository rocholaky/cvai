import pymupdf4llm
import os
import pathlib


class PDF: 

    """ 
    PDF is a class that handles PDF files.

    The primary methods of this class are: 
    1. load: the method loads the pdf file into memory.
    2. parse: the method parses the pdf file and returns the text.
    3. get_metadata: the method returns the metadata of the pdf file.
    """
    def __init__(self, file_path: str):
        """
        Initialize the PDF class.

        Args:
            file_path (str): The path to the PDF file.
        """
        self.file_path = file_path
        self.doc = None
        self.metadata = None
        self.llama_reader = pymupdf4llm.LlamaMarkdownReader()

    def load(self):
        """Load the PDF file into memory."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File {self.file_path} does not exist.")
        self.doc = self.llama_reader.load_data("input.pdf")

        # Get metadata
        # self.get_metadata(self.doc)

    def parse(self) -> str:
        """Parse the PDF file and return the text."""
        if self.doc is None:
            raise ValueError("PDF file not loaded. Call load() method first.")
        mrkdown = self.doc.get_content()
        return mrkdown

    def get_metadata(self) -> dict:
        """Get the metadata of the PDF file."""
        if self.metadata is None:
            raise ValueError("PDF file not loaded. Call load() method first.")
        return self.metadata