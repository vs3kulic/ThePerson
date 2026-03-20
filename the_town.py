"""Add yourself as a Person instance here!"""

from theperson.person import Person, Profile, Professional


if __name__ == "__main__":
    morpheus = Person(
        profile=Profile(name="Morpheus", gender="male"),
        professional=Professional(occupation="developer on GitHub"),
    )

    morpheus.introduce()
