"""Module containing Item classes."""

from __future__ import annotations


class Item:
    """Base class for all items."""

    def __init__(
        self,
        name: str,
        value: float = 0.0,
        stackable: bool = True,
    ) -> None:
        """Initialise a base item.

        Args:
            name: The name of the item.
            value: The monetary or general value of the item.
            stackable: Whether multiple quantities of the item can stack.

        Raises:
            ValueError: If name is not a non-empty string.
            TypeError: If value is not a number.
            TypeError: If stackable is not a boolean.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("'name' must be a non-empty string")
        if not isinstance(value, (int, float)):
            raise TypeError(
                "'value' must be a number, got type "
                f"'{type(value)}' instead"
            )
        if not isinstance(stackable, bool):
            raise TypeError(
                "'stackable' must be a boolean, got type "
                f"'{type(stackable)}' instead"
            )

        self.name = name.strip()
        self.value = float(value)
        self.stackable = stackable

    def describe(self) -> str:
        """Return a description of the item."""
        return f"{self.name} (value: {self.value})"

    def __hash__(self) -> int:
        """Return a hash value for dictionary/set usage."""
        return hash((self.name, self.__class__))

    def __eq__(self, other: object) -> bool:
        """Return whether two items are equal."""
        return (
            isinstance(other, Item)
            and self.name == other.name
            and self.__class__ == other.__class__
        )

    def __str__(self) -> str:
        """Return a readable string representation of the item."""
        return self.name

    def __repr__(self) -> str:
        """Return a detailed representation of the item."""
        return (
            f"{self.__class__.__name__}("
            f"name={self.name!r}, value={self.value}, "
            f"stackable={self.stackable})"
        )


class Food(Item):
    """A food item."""

    def __init__(
        self,
        name: str,
        calories: int | None = None,
        cooked: bool | None = None,
        brand: str | None = None,
        value: float = 0.0,
    ) -> None:
        """Initialise a food item.

        Args:
            name: The name of the food.
            calories: The calorie count of the food.
            cooked: Whether the food is cooked.
            brand: The brand of the food.
            value: The value of the food.

        Raises:
            TypeError: If calories is not an integer or None.
            TypeError: If cooked is not a boolean or None.
            TypeError: If brand is not a string or None.
            ValueError: If brand is an empty string.
        """
        if calories is not None and not isinstance(calories, int):
            raise TypeError(
                "'calories' must be an integer or None, got type "
                f"'{type(calories)}' instead"
            )
        if cooked is not None and not isinstance(cooked, bool):
            raise TypeError(
                "'cooked' must be a boolean or None, got type "
                f"'{type(cooked)}' instead"
            )
        if brand is not None and not isinstance(brand, str):
            raise TypeError(
                "'brand' must be a string or None, got type "
                f"'{type(brand)}' instead"
            )
        if isinstance(brand, str) and not brand.strip():
            raise ValueError("'brand' must be a non-empty string if provided")

        super().__init__(name, value=value, stackable=True)
        self.calories = calories
        self.cooked = cooked
        self.brand = brand.strip() if isinstance(brand, str) else None


class Electronic(Item):
    """An electronic item."""

    def __init__(
        self,
        name: str,
        brand: str,
        battery: int = 100,
        value: float = 0.0,
    ) -> None:
        """Initialise an electronic item.

        Args:
            name: The name of the electronic item.
            brand: The brand of the electronic item.
            battery: Battery percentage from 0 to 100.
            value: The value of the electronic item.

        Raises:
            ValueError: If brand is not a non-empty string.
            TypeError: If battery is not an integer.
            ValueError: If battery is outside the range 0 to 100.
        """
        if not isinstance(brand, str):
            raise TypeError(
                "'brand' must be a string, got type "
                f"'{type(brand)}' instead"
            )

        if not brand.strip():
            raise ValueError("'brand' must be a non-empty string")
        if not isinstance(battery, int):
            raise TypeError(
                "'battery' must be an integer, got type "
                f"'{type(battery)}' instead"
            )
        if not 0 <= battery <= 100:
            raise ValueError("'battery' must be between 0 and 100")

        super().__init__(name, value=value, stackable=False)
        self.brand = brand.strip()
        self.battery = battery


class Valuable(Item):
    """A valuable item such as jewellery, gold, or art."""

    def __init__(self, name: str, value: float) -> None:
        """Initialise a valuable item.

        Args:
            name: The name of the valuable item.
            value: The value of the item.
        """
        super().__init__(name, value=value, stackable=False)


class Weapon(Item):
    """A weapon item."""

    def __init__(
        self,
        name: str,
        value: float = 0.0,
    ) -> None:
        """Initialise a weapon.

        Args:
            name: The name of the weapon.
            value: The value of the weapon.
        """
        super().__init__(name, value=value, stackable=False)
