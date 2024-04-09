# Check if multiple Keys exist in a Dictionary in Python

my_dict = {
    'name': 'Bobby Hadz',
    'country': 'Austria',
    'age': 30
}

if all(key in my_dict for key in ("name", "country")):
    # 👇️ this runs
    print('multiple keys are in the dictionary')