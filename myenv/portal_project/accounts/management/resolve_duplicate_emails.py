# # accounts/management/commands/resolve_duplicate_emails.py

# from django.core.management.base import BaseCommand
# from django.db import IntegrityError
# from accounts.models import User
# from django.db.models import Count

# class Command(BaseCommand):
#     help = 'Resolves duplicate emails by appending a number to duplicates'

#     def handle(self, *args, **kwargs):
#         duplicates = User.objects.values('email').annotate(email_count=Count('email')).filter(email_count__gt=1)
#         for duplicate in duplicates:
#             users = User.objects.filter(email=duplicate['email'])
#             for i, user in enumerate(users[1:], start=1):  # Keep the first user, update the rest
#                 user.email = f"{user.email}_{i}"
#                 try:
#                     user.save()
#                     self.stdout.write(self.style.SUCCESS(f"Updated email for user {user.username} to {user.email}"))
#                 except IntegrityError as e:
#                     self.stdout.write(self.style.ERROR(f"Error updating user {user.username}: {e}"))
