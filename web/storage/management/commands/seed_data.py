import random

import factory
from common.tests.base import faker
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from storage.models.link import Link


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.LazyAttribute(lambda _: faker.name())
    email = factory.LazyAttribute(lambda _: faker.email())
    password = factory.LazyAttribute(lambda _: faker.password())


class LinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Link

    title = factory.LazyAttribute(lambda _: faker.text())
    short_description = factory.LazyAttribute(lambda _: faker.text())
    url = factory.LazyAttribute(lambda _: faker.url())
    image = factory.LazyAttribute(lambda _: faker.image_url())
    link_type = factory.LazyAttribute(
        lambda _: faker.random_element(
            elements=["website", "book", "article", "music", "video"]
        )
    )
    user = factory.SubFactory(UserFactory)


class Command(BaseCommand):
    help = "Seed database with sample data for "

    def add_arguments(self, parser):
        parser.add_argument("num_users", type=int, help="Number of users")
        parser.add_argument("num_links", type=int, help="Number of links")

    def handle(self, *args, **kwargs):
        num_users = kwargs["num_users"]
        num_links = kwargs["num_links"]

        self.stdout.write(self.style.SUCCESS("Seeding database..."))

        UserFactory.create_batch(num_users)
        LinkFactory.create_batch(num_links)

        self.stdout.write(self.style.SUCCESS("Database seeding completed."))
