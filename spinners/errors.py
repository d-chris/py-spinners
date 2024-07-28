class ValidationError(TypeError):
    pass


class ValidationSpinnerError(ValidationError):
    pass


class ValidationObjectError(ValidationError):
    pass


__all__ = [
    "ValidationError",
    "ValidationSpinnerError",
    "ValidationObjectError",
]
