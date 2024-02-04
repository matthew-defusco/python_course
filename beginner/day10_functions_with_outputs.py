# Functions with outputs
def format_name(f_name: str, l_name: str) -> str:
  # This is called a Docstring that adds a description of what the function should do as documentation.
  """This function returns a title case version of the first and last name that are passed in."""
  return f"{f_name} {l_name}".title()


name = format_name("Matthew", "defusco")
print(name)
