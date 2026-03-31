"""Module containing the Inventory class."""

from __future__ import annotations

from .item import Item


class Inventory:
    """A class to manage a person's inventory."""

    def __init__(self, max_capacity: int = 100) -> None:
        """Initialize the inventory.

        Args:
            max_capacity: The maximum total number of items allowed.

        Raises:
            TypeError: If max_capacity is not an integer.
            ValueError: If max_capacity is negative.
        """
        if not isinstance(max_capacity, int):
            raise TypeError(
                "'max_capacity' must be an integer, got type "
                f"'{type(max_capacity)}' instead"
            )
        if max_capacity < 0:
            raise ValueError("'max_capacity' must be non-negative")

        self.stackable_items: dict[Item, int] = {}
        self.unique_items: list[Item] = []
        self.max_capacity = max_capacity

    @property
    def item_count(self) -> int:
        """Return the total number of items in the inventory."""
        return sum(self.stackable_items.values()) + len(self.unique_items)

    @property
    def unique_item_types(self) -> int:
        """Return the number of unique item types in the inventory."""
        stackable_types = len(self.stackable_items)
        non_stackable_types = len(set(self.unique_items))
        return stackable_types + non_stackable_types

    def add_item(self, item: Item, quantity: int = 1) -> None:
        """Add an item to the inventory.

        Stackable items are grouped by quantity.
        Non-stackable items are stored as individual instances.

        Args:
            item: The item to add.
            quantity: The number of items to add.

        Raises:
            TypeError: If item is not an Item or quantity is not an integer.
            ValueError: If quantity is not positive.
            ValueError: If adding the item exceeds max capacity.
        """
        if not isinstance(item, Item):
            raise TypeError(
                "'item' must be an 'Item' object, got type "
                f"'{type(item)}' instead"
            )
        if not isinstance(quantity, int):
            raise TypeError(
                "'quantity' must be an integer, got type "
                f"'{type(quantity)}' instead"
            )
        if quantity <= 0:
            raise ValueError("'quantity' must be positive")
        if self.item_count + quantity > self.max_capacity:
            raise ValueError("Inventory capacity exceeded")

        if item.stackable:
            self.stackable_items[item] = (
                self.stackable_items.get(item, 0) + quantity
            )
        else:
            for _ in range(quantity):
                self.unique_items.append(item.clone())

    def remove_item(self, item: Item, quantity: int = 1) -> None:
        """Remove an item from the inventory.

        Args:
            item: The item to remove.
            quantity: The number of items to remove.

        Raises:
            TypeError: If item is not an Item or quantity is not an integer.
            ValueError: If quantity is not positive.
            ValueError: If the item is not found or quantity is insufficient.
        """
        if not isinstance(item, Item):
            raise TypeError(
                "'item' must be an 'Item' object, got type "
                f"'{type(item)}' instead"
            )
        if not isinstance(quantity, int):
            raise TypeError(
                f"'quantity' must be an integer, got type "
                f"'{type(quantity)}' instead"
            )
        if quantity <= 0:
            raise ValueError("'quantity' must be positive")

        if item.stackable:
            if item not in self.stackable_items:
                raise ValueError("Item not found in inventory")
            if self.stackable_items[item] < quantity:
                raise ValueError("Not enough quantity to remove")

            self.stackable_items[item] -= quantity
            if self.stackable_items[item] == 0:
                del self.stackable_items[item]
        else:
            matches = [
                stored_item for stored_item in self.unique_items
                if stored_item == item
            ]
            if len(matches) < quantity:
                raise ValueError("Not enough quantity to remove")

            removed = 0
            remaining_items: list[Item] = []
            for stored_item in self.unique_items:
                if stored_item == item and removed < quantity:
                    removed += 1
                else:
                    remaining_items.append(stored_item)
            self.unique_items = remaining_items

    def clear(self) -> None:
        """Clear the inventory."""
        self.stackable_items.clear()
        self.unique_items.clear()

    def get_items(self) -> str:
        """Return a formatted list of inventory items."""
        if self.is_empty():
            return "Inventory is empty"

        lines: list[str] = []

        for item, qty in sorted(
            self.stackable_items.items(),
            key=lambda pair: pair[0].name.lower()
        ):
            lines.append(f"{item.describe()} x{qty}")

        for item in sorted(
            self.unique_items,
            key=lambda stored: stored.name.lower()
        ):
            lines.append(item.describe())

        return "\n".join(lines)
    
    def list_items(self) -> None:
        """Print a human-readable listing of the inventory to stdout."""
        print(self.get_items())

    def is_empty(self) -> bool:
        """Return True if the inventory is empty."""
        return self.item_count == 0

    def has_item(self, item: Item) -> bool:
        """Return True if the inventory contains the given item."""
        if not isinstance(item, Item):
            raise TypeError(
                f"'item' must be an 'Item' object, got type "
                f"'{type(item).__name__}' instead'"
            )
        if item.stackable:
            return item in self.stackable_items
        return item in self.unique_items

    def get_quantity(self, item: Item) -> int:
        """Return the quantity of a given item in the inventory."""
        if item.stackable:
            return self.stackable_items.get(item, 0)
        return sum(
            1 for stored_item in self.unique_items if stored_item == item
        )

    def is_full(self) -> bool:
        """Return True if the inventory has reached max capacity."""
        return self.item_count >= self.max_capacity

    def remove_all(self, item: Item) -> None:
        """Remove all instances of a given item from the inventory."""
        if item.stackable:
            self.stackable_items.pop(item, None)
        else:
            self.unique_items = [
                stored_item for stored_item in self.unique_items
                if stored_item != item
            ]

    def filter_items(self, item_type: type[Item]) -> str:
        """Return a formatted list of items of a specific type."""
        lines: list[str] = []

        for item, qty in sorted(
            self.stackable_items.items(),
            key=lambda pair: pair[0].name.lower()
        ):
            if isinstance(item, item_type):
                lines.append(f"{item.describe()} x{qty}")

        for item in sorted(
            self.unique_items,
            key=lambda stored: stored.name.lower()
        ):
            if isinstance(item, item_type):
                lines.append(item.describe())

        if not lines:
            return (
                f"No items of type {item_type.__name__} found."
            )

        return "\n".join(lines)

    def sort_items(self) -> str:
        """Return a formatted list of all items sorted by name."""
        return self.get_items()

    def total_value(self) -> float:
        """Return the total value of all items in the inventory."""
        stackable_value = sum(
            (item.value or 0.0) * qty
            for item, qty in self.stackable_items.items()
        )
        unique_value = sum((item.value or 0.0) for item in self.unique_items)
        return stackable_value + unique_value

    def __str__(self) -> str:
        """Return a readable string representation of the inventory."""
        return self.get_items()

    def __repr__(self) -> str:
        """Return a detailed representation of the inventory."""
        return (
            "Inventory("
            f"stackable_items={self.stackable_items!r}, "
            f"unique_items={self.unique_items!r}, "
            f"max_capacity={self.max_capacity})"
        )
