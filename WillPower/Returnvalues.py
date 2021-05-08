def anime(name,genre='Fiction'):
    if genre=='Horror':
        return name
    else:
        print(f"{name} belongs to {genre} genre")
    
anime('Naruto','Ninja')
anime(name='Ninja Hattori',genre='Ninja')
anime('Black Clover')
anime_name=anime('Another','Horror')
print(f"{anime_name} belongs to Horror genre and is very scary,\nRUNNN!!!")

#optional args
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

musician = get_formatted_name('jaunne','D Arc')
print(musician)