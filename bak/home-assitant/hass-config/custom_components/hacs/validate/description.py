from __future__ import annotations

from .base import ActionValidationBase, ValidationException
from ..repositories.base import HacsRepository


async def async_setup_validator(repository: HacsRepository) -> Validator:
    """Set up this validator."""
    return Validator(repository=repository)


class Validator(ActionValidationBase):
    """Validate the repository."""

    more_info = "https://hacs.xyz/docs/publish/include#check-repository"
    allow_fork = False

    async def async_validate(self):
        """Validate the repository."""
        if not self.repository.data.description:
            raise ValidationException("The repository has no description")
