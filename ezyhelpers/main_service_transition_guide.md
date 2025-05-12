# MainService Component Transition Guide

This guide provides step-by-step instructions for transitioning your `MainService` model from using reusable components (via ManyToMany fields) to using specific components for each service (via ForeignKey fields).

## Changes Made

The following changes have been implemented:

1. Added ForeignKey fields to `ServiceStat`, `ServiceFeature`, and `FAQ` models linking them to `MainService`.
2. Removed ManyToMany fields from `MainService` (stats, features, faqs).
3. Created inline admin components for these models in the `MainServiceAdmin`.
4. Created data migration scripts to preserve existing relationships.

## Implementation Process

### 1. Back Up Your Database

Before applying any migrations, create a backup of your database:

```bash
# For SQLite (which you're using)
cp ezyhelpers/db.sqlite3 ezyhelpers/db.sqlite3.backup
```

### 2. Apply the Migrations

Run the following commands to apply the migrations:

```bash
# Generate migration files (if you need to generate them yourself)
python manage.py makemigrations main

# Apply migrations
python manage.py migrate main
```

The migration files have already been created for you:
- `main/migrations/0002_data_migration.py` - Handles adding new fields and migrating existing data

### 3. Verify Changes in Admin

1. Start your development server:
   ```bash
   python manage.py runserver
   ```

2. Navigate to the admin interface and check that:
   - When editing a `MainService`, you can now add stats, features, and FAQs as inline components
   - The old multi-select interfaces for these components are gone
   - The data from previous relationships has been preserved

### 4. (Optional) Clean Up Old Data

After verifying everything works as expected, you may want to consider:

1. Reviewing any standalone `ServiceStat`, `ServiceFeature`, or `FAQ` entries that aren't associated with any `MainService`
2. Determining if you want to keep the standalone admin pages for these models

## Troubleshooting

### If Migrations Fail

If you encounter issues with the migrations:

1. Restore your database backup:
   ```bash
   cp ezyhelpers/db.sqlite3.backup ezyhelpers/db.sqlite3
   ```

2. Try running the data migration script manually:
   ```bash
   python manage.py shell < ezyhelpers/main/migrations/data_migration_script.py
   ```

3. Then run the migrations again, skipping the data migration part:
   ```bash
   # You might need to create a new migration that only includes schema changes
   python manage.py migrate main
   ```

### If Admin Interface Issues

If you notice issues with the admin interface:

1. Check that the inlines are properly configured in `admin.py`
2. Make sure there are no old references to removed fields
3. Verify that `ServiceFeature`, `ServiceStat`, and `FAQ` models are properly linked to `MainService`

## Summary

You've successfully transitioned from a reusable component model to one where each `MainService` has its own unique set of components. This will give you more flexibility in managing your content and a cleaner admin interface. 