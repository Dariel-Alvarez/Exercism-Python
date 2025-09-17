def recite(start_verse, end_verse):
    days = ["first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    
    gave = ["a Partridge in a Pear Tree.",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"]
    
    song = []
    for day in range(start_verse, end_verse + 1):
        verse = f"On the {days[day - 1]} day of Christmas my true love gave to me: "
        gifts = []

        for gift in range (day - 1, -1, -1):
            if gift == 0 and day != 1:
                gifts.append("and " + gave[gift])
            else:
                gifts.append(gave[gift])

        verse += ", ".join(gifts)
        song.append(verse)

    return song