onetonine = len("onetwothreefourfivesixseveneightnine")
andd = len("and")
hundred = len("hundred")
teens = len("teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen")
thousand = len("onethousand")
tensdigits = len("twentythirtyfortyfiftysixtyseventyeightyninety")

totalchars = 0
totalchars += onetonine * 90 # 1-9, 21-29 etc, so 9 occurances, for 1-9, 101-109, 200, etc
totalchars += onetonine * 100 # 100 "one"n hundreds, 100 "two" hundreds
totalchars += andd * (900 - 9) # "and" wherever the number > 100 and not divisible by 100
totalchars += hundred * 900 # 100 one "hundred"s, 100 two "hundred"s ... 100 nine "hundred"s
totalchars += teens * 10
totalchars += thousand
totalchars += tensdigits * 100 # 10 twenty-somethings for each hundred

print totalchars