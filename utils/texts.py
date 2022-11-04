version = "0.1"
author = 'akumaru'
from .colors import colors

xodo_text = f"""xodo - CLI tool that helps to follow TODO.
version: {version}
author: {author}

guide -> xodo guide"""

guide_text = f"""{colors.OKCYAN}xodo - CLI tool that helps to follow TODO.
version:  {version}
author: {author}

Available commands:
			{colors.HEADER}add:
				usage: xodo add
				to add a new xodo.

			guide:
				usage: xodo guide
				to get a guide

			list:
				usage: xodo list
				to get all xodos list"""