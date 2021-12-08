from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates room_types"

    def handle(self, *args, **options):
        room_types = [
            "Hotel room",
            "Shared room",
            "Private room",
            "Entire room",
        ]

        for r in room_types:
            room_models.RoomType.objects.create(name=r)

        self.stdout.write(self.style.SUCCESS(f"{len(room_types)} room_types created!"))
