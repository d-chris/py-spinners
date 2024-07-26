from spinners.base import BaseSpinners, ValidationError


def register_spinner(priority: int = None):
    """
    Decorator to register Enum classes with the BaseSpinners class.
    """

    def decorator(enum_class):
        try:
            BaseSpinners.insert(priority, enum_class)
        except ValidationError as e:
            raise ValidationError(f"{enum_class} is not a suitable spinner") from e
        except TypeError:
            BaseSpinners.append(enum_class)

        return enum_class

    # If the decorator is used without arguments
    if callable(priority):
        enum_class = priority
        priority = -1
        return decorator(enum_class)

    return decorator
