class MicroSlop:
    """
    Represents a software product that can be toggled on/off, with a name and price.
    Provides methods to change state and update the product details dynamically.
    """

    def __init__(self, product: str, price: int) -> None:
        # Initialize the instance with a product name and price.
        # The product starts in an "off" state by default.
        self.product = product
        self.price = price
        self.turned_on = False

    def slop_on(self) -> None:
        """Activate the product if not already on; otherwise, inform the user."""
        if self.turned_on:
            print(f"{self.product} is already active.")
        else:
            self.turned_on = True
            print(f"{self.product} is now active.")

    def slop_off(self) -> None:
        """Deactivate the product if it is currently on; otherwise, inform the user."""
        if not self.turned_on:
            print(f"{self.product} is already inactive.")
        else:
            self.turned_on = False
            print(f"{self.product} has been deactivated.")

    def update_product(self, new_product: str, new_price: int) -> None:
        """
        Update the product's name and price.
        Resets the turned_on state to False to avoid accidental activation of the new product.
        """
        self.product = new_product
        self.price = new_price
        self.turned_on = False
        print(f"Product updated: {self.product} at ${self.price} (inactive).")

    def __str__(self) -> str:
        """Provide a human-readable representation of the object."""
        status = "on" if self.turned_on else "off"
        return f"{self.product} (${self.price}) - {status}"

    def __repr__(self) -> str:
        """Provide an unambiguous representation for debugging purposes."""
        return f"MicroSlop(product={self.product!r}, price={self.price!r}, turned_on={self.turned_on})"

    # Usage examples

    def __add__(self, other: MicroSlop):
        """Return a new MicroSlop instance that is the sum of two products."""
        return f"{self.price} + {other.price}"


notes: MicroSlop = MicroSlop("Notes", 100)  # type-hinted
outlook = MicroSlop("Outlook", 200)  # no type hint

notes.slop_off()  # already off
notes.slop_on()  # now active
notes.update_product("Notebook", 150)  # reset and update product

# Print instances meaningfully
print(notes)  # Notebook ($150) - off
print(outlook)  # Outlook ($200) - off
print(notes + outlook)
