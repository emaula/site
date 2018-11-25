from selenium import webdriver

browser = webdriver.Firefox()

# A teacher hears about EmAula.xyz and goes to the homepage to check it out
browser.get('http://localhost:8000')

# In the homepage, the teacher finds the following menus:
# Sobre (About)

# Equipe (Team)

# Colabore! (Colaborate)

# Inscrave-se! (Register)

# The teacher also finds an inputbox to login into the EmAula system
assert 'EmAula.xyz - Planeje e compartilhe suas aulas!' in browser.title, "Browser title was " + browser.title
