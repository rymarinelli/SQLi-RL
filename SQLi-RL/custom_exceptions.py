class URLSpecification(Exception):
    """Exception raised for errors in the URL specification."""
    def __init__(self, message="URL must start with 'http'"):
        self.message = message
        super().__init__(self.message)

class InvalidUserAgent(Exception):
    """Exception raised when the User-Agent is missing or invalid."""
    def __init__(self, message="Invalid or missing User-Agent"):
        self.message = message
        super().__init__(self.message)
