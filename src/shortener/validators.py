from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(value):
	url_validator = URLValidator()
	valid_value = value
	if "http" not in value:
		valid_value = "http://" + value
	try:
		url_validator(valid_value)
	except:
		raise ValidationError("Invalid URL for this field")
	return valid_value


def validate_dot_com(value):
	if not "com" in value:
		raise ValidationError("URL invalid because of missing .com")