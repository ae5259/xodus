from .colors import colors

version = "0.1"
author = "akumaru"

done_xodo = "✅"
current_xodo = "🕧"
unfinished_xodo = "⭕️"

xodo_text = f"""xodus - CLI tool that helps to follow TODO.
version: {version}
author: {author}

guide -> xodus guide"""

guide_text = f"""{colors.OKCYAN}xodus - CLI tool that helps to follow TODO.
version:  {version}
author: {author}

Available commands:
			{colors.HEADER}add:
				usage: xodus add
				to add a new xodo.

			guide:
				usage: xodus guide
				to get a guide

			list:
				usage: xodus list
				to get all xodos list
                
            done:
				usage: xodus done <xodo_id>
				to mark a xodo as done
				"""
