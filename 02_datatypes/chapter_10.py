import arrow

brewing_time = arrow.utcnow()

rome_time = brewing_time.to("Europe/Rome")

from collections import namedtuple

ChaiProfile = namedtuple("ChaiProfile", ["flavor", "aroma"])

chai = ChaiProfile(flavor="Masala", aroma="Spicy & Sweet")

print(chai)