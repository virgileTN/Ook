Interpreter Oui!.
===========

####EN:
Interpreter language Oui!.

| Character         | Meaning                                                                                     |
|-------------------|---------------------------------------------------------------------------------------------|
|     Oui. Oui.     | increment the data pointer (to point to the next cell to the right).                        |
|     Oui! Oui!     | decrement the data pointer (to point to the next cell to the left).                         |
|     Oui. Oui?     | increment (increase by one) the byte at the data pointer.                                   |
|     Oui? Oui.     | decrement (decrease by one) the byte at the data pointer.                                   |
|     Oui! Oui.     | output the byte at the data pointer.                                                        |
|     Oui. Oui!     | accept one byte of input, storing its value in the byte at the data pointer.                |
|     Oui! Oui?     | if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.      |
|     Oui? Oui!     | if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the,next command, jump it back to the command after the matching [ command.      |
