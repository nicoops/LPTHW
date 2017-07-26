#Designating the formatter variable to return 4 %r strings
formatter = "%r %r %r %r"
#I beileve this will return 1, 2, 3, 4
print formatter % (1, 2, 3, 4)
#I believe this will return one, two, three, four
print formatter % ("one", "two", "three", "four")
#I believe this will return True, False, False, True
print formatter % (True, False, False, True)
#I believe this will return formatter x 4
print formatter % (formatter, formatter, formatter, formatter)
#I believe this will return the poem below
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.", #because there is a ' in don't, python print's this string using double "
    "So I said goodnight."
)

#Some syntax errors on this one, type more carefully
