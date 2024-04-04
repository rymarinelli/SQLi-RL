class ValidateAgentProperties():
    """Class is to be used in composition to define a larger agent class"""
    
    def __init__(self):
        self._url = "http://{ip-address}:8000/index.php"
        self._header = "{'User-Agent': 'Mozilla/5.0, RL-CTF'}"
        self._interaction_form_name = "email"

    @property
    def url(self):
        """Getter for the URL."""
        return self._url

    @property
    def header(self):
        """Getter for the header."""
        return self._header

    @property
    def interaction_form_name(self):
      """Getter for the form name."""
      return self._interaction_form_name 


    @url.setter
    def url(self, value):
        """Setter for the URL, with validation to ensure it starts with 'http'."""
        if not value.startswith("http"):
            raise URLSpecification("URL must start with 'http'")
        self._url = value

    @header.setter
    def header(self, value):
        """Setter for header."""
        if not isinstance(value, dict):
          raise InvalidUserAgent("The headers must be a dictionary")
    
        if 'User-Agent' not in value or not value['User-Agent']:
          raise InvalidUserAgent("The 'User-Agent' key is missing or its value is empty")
          self._header = value

    @interaction_form_name.setter
    def interaction_form_name(self, value):
      """Setter for form name."""
      self._interaction_form_name = value 
