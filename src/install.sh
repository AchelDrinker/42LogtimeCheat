#!/bin/bash

function install () {
	shell_f=$(echo -n "$SHELL" | awk -F / '{print $3}')
	shell_f="${HOME}/.${shell_f}rc"
	echo "alias logfarm='python3 ~/$HOME/logtime-farmer/src/logtime-farmer.py'" >> "$shell_f"
}

install
exit 0
