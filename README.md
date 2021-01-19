# sesam
Python tool to generate a unique password based on a
given masterpassword and a given domain. Result in clipboard



- master password:
Think of a secure password, preferably according to the guidelines: https://pages.nist.gov/800-63-3/sp800-63b.html
(e.g. ThreeWoerterGrandeStringIs theImportantCondition)

- domain:
enter here the domain to which the password should be created.
importantly remember the spelling, two different spellings (e.g. amasohn or Amasohn) result in two different passwords!

- OK (Button):
The strings masterpassword and domain are used together in an encryption algorithm. The result and thus the password is stored in the cache and can be inserted by pressing Ctrl+V [Win]. The password length can be set in ui.py.  

- Further hints:
Please change the string for the salt, this is used by the encryption algorithm 
used to generate the password

The password is only the same every time with the same master password and the same 
Domain and same salt

