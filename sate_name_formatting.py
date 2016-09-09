import re

#
# FUNCTIONS
#
# Takes a string as an argument
# Removes the word Incorporated if it exists at the end of a string
# Returns a modified string if Incorporate exists at the end of a string, otherwise returns the original string
def remove_incorporated(s):
    return re.sub(r'(\,*\sIncorporated\.*$)','', s)


# Takes a string as an argument
# Removes the following if they exist at the end of a string: , Inc. | Inc. |, Inc| Inc<br>
# Returns a modified string if one one of the above patterns exist, otherwise returns the original string
def remove_incorporated_abbreviation(s):
    return re.sub(r'(\,*\s[Ii][Nn][Cc]\.*$)','', s)

# Takes a string as an argument
# Removes the following if they exist at the end of a string:, L.L.C. and all other variations with/without periods and commas<br>
# Returns a modified string if one one of the above patterns exist, otherwise returns the original string
def remove_llc(s):
    return re.sub(r'(\,*\s[Ll]\.*[Ll]\.*[Cc]\.*$)','', s) 

# Takes a string as an argument
# Removes the following if they exist at the end of a string:, L.C. and all other variations with/without periods and commas<br>
# Returns a modified string if one one of the above patterns exist, otherwise returns the original string
def remove_lc(s):
    return re.sub(r'(\,*\s[Ll]\.*[Cc]\.*$)','', s)

# Takes a string as an argument
# Removes the following if they exist at the end of a string:, L.L.P. and all other variations with/without periods and commas<br>
# Returns a modified string if one one of the above patterns exist, otherwise returns the original string
def remove_llp(s):
    return re.sub(r'(\,*\s[Ll]\.*[Ll]\.*[Pp]\.*$)','', s) 

# Takes a string as an argument
# Removes the following if they exist at the end of a string:, L.P. and all other variations with/without periods and commas<br>
# Returns a modified string if one one of the above patterns exist, otherwise returns the original string
def remove_lp(s):
    return re.sub(r'(\,*\s[Ll]\.*[Pp]\.*$)','', s)

# Takes a string as an argument
# Removes the word Limited at the end of the string<br>
# Returns a modified string without the word Limited, otherwise returns the original string
def remove_limited(s):
    return re.sub(r'(\,*\s[Ll][Ii][Mm][Ii][Tt][Ee][Dd]\.*$)','', s)

# Takes a string as an argument
# Removes the following if they exist at the end of a string:, Ltd. and all other variations with/without periods and commas<br>
# Returns a modified string if one one of the above patterns exist, otherwise returns the original string
def remove_ltd(s):
    return re.sub(r'(\,*\s[Ll]\.*[Tt]\.*[Dd]\.*$)','', s)

# Takes a string as an argument
# Removes the word Corporation at the end of a string<br>
# Returns a modified string without the word Corporation, otherwise returns the original string
def remove_corporation(s):
    return re.sub(r'(\,*\s[Cc][Oo][Rr][Pp][Oo][Rr][Aa][Tt][Ii][Oo][Nn]\.*$)','', s)

# Takes a string as an argument
# Removes the following if they exist at the end of a string:, Corp. and all other variations with/without periods and commas<br>
# Returns a modified string if one one of the above patterns exist, otherwise returns the original string
def remove_corp(s):
    return re.sub(r'(\,*\s[Cc][Oo][Rr][Pp]\.*$)','', s)

# Takes a string as an argument
# Takes the abbreviated form of the word Company and spells it out long hand
# Returns a modified string if one one of the above patterns exist, otherwise returns the original string
def edit_company(s):
    return re.sub(r'(\,*\s[Cc][Oo]\.*$)',' Company', s)


### DBA 


##Some companies are listed as xxx company DBA yyy brand; we want the brand name ONLY to remain
# Step 1 to remove DBA: Standardize the 'DBA' format; remove lines, remove periods, make all capitals
####jwdataset['name'] = jwdataset ['name'].str.replace (r'') #remove all tet preceding the DBA
def standardize_dba(s):
    return re.sub(r'(\s[Dd]\/*\.*[Bb]\/*\.*[Aa]\/*\.*\s)', ' DBA ', s)

#Step 2 to remove DBA: Remove the legal name and the "DBA", leaving just the company's brand name
def remove_dba(s):
    return re.sub(r'(^.*DBA )', '', s) 



#
# TESTS
#

def test_remove_incorporated():
    assert remove_incorporated('Foo Incorporated') == 'Foo'
    assert remove_incorporated('Foo, Inc.') == 'Foo, Inc.'

def test_remove_incorporated_abbreviation():
    assert remove_incorporated_abbreviation('Foo Inc.') == 'Foo'
    assert remove_incorporated_abbreviation('Foo, Inc.') == 'Foo'
    assert remove_incorporated_abbreviation('Foo, Inc') == 'Foo'
    assert remove_incorporated_abbreviation('Foo Inc') == 'Foo'
    assert remove_incorporated_abbreviation('Foo Incorporated') == 'Foo Incorporated'
    
def test_remove_llc():
    assert remove_llc('Foo, L.L.C.') == 'Foo'
    assert remove_llc('Foo, LL.C.') == 'Foo'
    assert remove_llc('Foo, LLC.') == 'Foo'
    assert remove_llc('Foo, LLC') == 'Foo'
    assert remove_llc('Foo L.L.C.') == 'Foo'
    assert remove_llc('Foo LL.C.') == 'Foo'
    assert remove_llc('Foo LLC.') == 'Foo'
    assert remove_llc('Foo LLC') == 'Foo'
    assert remove_llc('Foo Llc') == 'Foo'
    assert remove_llc('Foo llc') == 'Foo'

def test_remove_lc():
    assert remove_lc('Foo, L.C.') == 'Foo'
    assert remove_lc('Foo, LC.') == 'Foo'
    assert remove_lc('Foo, LC') == 'Foo'
    assert remove_lc('Foo L.C.') == 'Foo'
    assert remove_lc('Foo LC.') == 'Foo'
    assert remove_lc('Foo LC') == 'Foo'
    assert remove_lc('Foo Lc') == 'Foo'
    assert remove_lc('Foo lc') == 'Foo'

def test_remove_llp():
    assert remove_llp('Foo, L.L.P.') == 'Foo'
    assert remove_llp('Foo, LL.P.') == 'Foo'
    assert remove_llp('Foo, LLP.') == 'Foo'
    assert remove_llp('Foo, LLP') == 'Foo'
    assert remove_llp('Foo L.L.P.') == 'Foo'
    assert remove_llp('Foo LL.P.') == 'Foo'
    assert remove_llp('Foo LLP.') == 'Foo'
    assert remove_llp('Foo LLP') == 'Foo'
    assert remove_llp('Foo Llp') == 'Foo'
    assert remove_llp('Foo llp') == 'Foo'    
    
def test_remove_lp():
    assert remove_lp('Foo, L.P.') == 'Foo'
    assert remove_lp('Foo, LP.') == 'Foo'
    assert remove_lp('Foo, LP') == 'Foo'
    assert remove_lp('Foo L.P.') == 'Foo'
    assert remove_lp('Foo LP.') == 'Foo'
    assert remove_lp('Foo LP') == 'Foo'
    assert remove_lp('Foo Lp') == 'Foo'
    assert remove_lp('Foo lp') == 'Foo'

def test_remove_limited():
    assert remove_limited('Foo, Limited') == 'Foo'
    assert remove_limited('Foo, Limited.') == 'Foo'
    assert remove_limited('Foo Limited') == 'Foo'
    assert remove_limited('Foo Limited.') == 'Foo'
    
def test_remove_ltd():
    assert remove_ltd('Foo, L.T.D.') == 'Foo'
    assert remove_ltd('Foo, LT.D.') == 'Foo'
    assert remove_ltd('Foo, LTD.') == 'Foo'
    assert remove_ltd('Foo, Ltd.') == 'Foo'
    assert remove_ltd('Foo, Ltd') == 'Foo'
    assert remove_ltd('Foo L.T.D.') == 'Foo'
    assert remove_ltd('Foo LT.D.') == 'Foo'
    assert remove_ltd('Foo LTD.') == 'Foo'
    assert remove_ltd('Foo Ltd.') == 'Foo'
    assert remove_ltd('Foo Ltd') == 'Foo'
    
def test_remove_corporation():
    assert remove_corporation('Foo, Corporation') == 'Foo'
    assert remove_corporation('Foo, Corporation.') == 'Foo'
    assert remove_corporation('Foo Corporation') == 'Foo'
    assert remove_corporation('Foo Corporation.') == 'Foo'
    
def test_remove_corp():
    assert remove_corp('Foo, CORP.') == 'Foo'
    assert remove_corp('Foo, Corp.') == 'Foo'
    assert remove_corp('Foo, CORP') == 'Foo'
    assert remove_corp('Foo, Corp') == 'Foo'
    assert remove_corp('Foo CORP.') == 'Foo'
    assert remove_corp('Foo Corp.') == 'Foo'
    assert remove_corp('Foo CORP') == 'Foo'
    assert remove_corp('Foo Corp') == 'Foo'
    
    
def test_edit_company():
    assert edit_company('Foo, Co.') == 'Foo Company'    
    assert edit_company('Foo, Co') == 'Foo Company' 
    assert edit_company('Foo Co.') == 'Foo Company'    
    assert edit_company('Foo Co') == 'Foo Company' 

def test_standardize_dba ():
    assert standardize_dba('Foo, Co. d/b/a Foo Industries') == 'Foo, Co. DBA Foo Industries'
    assert standardize_dba('Foo, Co. DBA Foo Industries') == 'Foo, Co. DBA Foo Industries'
    assert standardize_dba('Foo, Co. D.b.a. Foo Industries') == 'Foo, Co. DBA Foo Industries'
    
def test_remove_dba ():
    assert remove_dba('Foo, Co. DBA Foo Industries') == 'Foo Industries'

def run_tests():
    test_remove_incorporated()
    test_remove_incorporated_abbreviation()
    test_remove_llc()
    test_remove_lc()
    test_remove_llp()
    test_remove_lp()
    test_remove_limited
    test_remove_ltd()
    test_remove_corporation()
    test_remove_corp()
    test_edit_company()
    test_standardize_dba()
    test_remove_dba ()

    
 
    
run_tests()