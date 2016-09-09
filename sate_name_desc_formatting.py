import re

#
# FUNCTIONS
#


# Takes a string as an argument
# Changes the apostrophe
# Returns a modified string that removes the apostrophe, otherwise returns the original string
def remove_plural_apostrophe_u(s):
    return re.sub(r"(Farmers' Market)","Farmers Market", s)

def remove_plural_apostrophe_l(s):
    return re.sub(r"(farmers' market)","farmers market", s)

# Takes a string as an argument
# Changes the apostrophe
# Returns a modified string that removes the apostrophe, otherwise returns the original string
def remove_singular_apostrophe_u(s):
    return re.sub(r'(Farmer\'s Market)', "Farmers Market", s)

def remove_singular_apostrophe_l(s):
    return re.sub(r'(farmer\'s market)', "farmers market", s)

# Takes a string as an argument
# Returns a modified string that adds back in the apostrophe, otherwise returns the original string
def add_back_apostrophe_u(s):
    return re.sub(r'(Farmers Market)', "Farmer's Market", s)

def add_back_apostrophe_l(s):
    return re.sub(r'(farmers market)', "farmer's market", s)



###LEADING AND TRAILING WHITESPACES

def leading_whitespace (s):
    return re.sub(r'(^\s+)','',s)

def trailing_whitespace (s):
    return re.sub(r'(\s+$)','',s)



#
# TESTS
#

def test_remove_plural_apostrophe():
    assert remove_plural_apostrophe_u("Farmers' Market") == "Farmers Market"
    assert remove_plural_apostrophe_l("farmers' market") == "farmers market"
    
def test_remove_singular_apostrophe():
    assert remove_singular_apostrophe_u("Farmers Market") == "Farmers Market"   
    assert remove_singular_apostrophe_l("farmers market") == "farmers market"    
    
def test_add_back_apostrophe():
    assert add_back_apostrophe_u("Farmers Market") == "Farmer's Market"
    assert add_back_apostrophe_l("farmers market") == "farmer's market"
    
   
def test_leading_whitespace ():
    assert leading_whitespace (' Foo ') == 'Foo '
    assert leading_whitespace (' Foo Bar') == 'Foo Bar'

def test_trailing_whitespace ():
    assert trailing_whitespace ('Foo ') == 'Foo'
    assert trailing_whitespace (' Foo Bar ') == ' Foo Bar'

    
def run_tests():
    test_remove_plural_apostrophe()
    test_remove_singular_apostrophe()
    test_add_back_apostrophe()
    test_leading_whitespace()
    test_trailing_whitespace()
    
run_tests()