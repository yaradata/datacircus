import re

def validate_url(url) -> bool:
	# Validate URL
	url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

	if re.match(url_pattern, url):
		return True
	else:
		return False
