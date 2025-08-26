from django.core.management.base import BaseCommand
import pandas as pd
from department.models import Department
from research_assistant.models import ResearchAssistant
from django.utils.text import slugify  # added here

class Command(BaseCommand):
    help = "Import departments and research assistants from Excel"

    def handle(self, *args, **options):
        # ✅ Hard-coded file path
        file_path = r"D:\My projects\python\Projects\exam_schedule\excel files\ex.xlsx"

        # Read Excel (no header since it’s just text lines)
        df = pd.read_excel(file_path, header=None)

        current_department = None
        for _, row in df.iterrows():
            value = str(row[0]).strip()
            if not value or value.lower() == "nan":
                continue  # skip empty rows

            # If line contains "Mühendisliği", treat as department
            if "mühendisliği" in value.lower():
                current_department, _ = Department.objects.get_or_create(
                    name=value,
                    defaults={"code": slugify(value)[:10]}  # short unique code
                )
                self.stdout.write(self.style.SUCCESS(f"Added department: {value}"))
            else:
                # Otherwise treat as Research Assistant (linked to current department)
                if current_department:
                    ra, _ = ResearchAssistant.objects.get_or_create(
                        name=value,
                        department=current_department
                    )
                    self.stdout.write(f"   Added assistant: {value} -> {current_department.name}")
