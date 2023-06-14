.DEFAULT_GOAL = help

run:  ## Run the server
	cd 5esheets && poetry run flask run --port 8000 --reload --debug

translations-extract:  ## Extract all strings to translate from jinja templates
	poetry run pybabel extract -F babel.cfg -o 5esheets/translations/messages.pot .

translations-update:  translations-extract  ## Update the language catalogs with new translations
	poetry run pybabel update -i 5esheets/translations/messages.pot -d 5esheets/translations

translations-compile:  translations-update  ## Compile translations into a .mo file
	poetry run pybabel compile -d 5esheets/translations

help:  ## Display help
	@grep -E '^[%a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?##"}; {printf "\033[36m%-22s\033[0m %s\n", $$1, $$2}'