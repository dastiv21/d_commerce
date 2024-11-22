from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import AUser, UserActivity, UserEngagement, UserBehavior, EventTracking, ChurnData, PerformanceData
from datetime import timedelta
import random

class Command(BaseCommand):
    help = "Populate the database with sample data for reports."

    def handle(self, *args, **kwargs):
        nigerian_names = [
            "Adeola", "Adewale", "Afolabi", "Ayo", "Babatunde", "Bola",
            "Chiamaka", "Chidera",
            "Chigozie", "Chike", "Chinasa", "Chinenye", "Chinwe", "Chinyere",
            "Damilola", "Danjuma",
            "Ebere", "Efe", "Emeka", "Fadekemi", "Femi", "Folake",
            "Folorunsho", "Gbenga", "Ifeanyi",
            "Ifedayo", "Ijeoma", "Ikechukwu", "Isioma", "Itoro", "Ivie",
            "Jelili", "Jide", "Kehinde",
            "Kemi", "Kudirat", "Lade", "Lekan", "Lola", "Mayowa", "Musa",
            "Ndidi", "Ngozi", "Nkechi",
            "Nnamdi", "Obi", "Obinna", "Olufemi", "Oluwakemi", "Oluwasegun",
            "Onyeka", "Osagie",
            "Sade", "Samuel", "Segun", "Sikiru", "Tayo", "Temidayo", "Tofunmi",
            "Tomiwa", "Uchenna",
            "Ufuoma", "Ugochi", "Uzoma", "Yemi", "Yetunde", "Yewande",
            "Zainab", "Zubairu",
            # Surnames
            "Abimbola", "Abiodun", "Abubakar", "Adebayo", "Adegbite",
            "Adekoya", "Ademola",
            "Adetokunbo", "Agboola", "Agunbiade", "Ajayi", "Akinbayo",
            "Akinola", "Alao", "Alimi",
            "Aminu", "Anyanwu", "Asuquo", "Awoleye", "Balogun", "Bankole",
            "Bello", "Dabiri",
            "Daramola", "Dauda", "Dawodu", "Eke", "Ekunwe", "Elumelu",
            "Emenike", "Eze", "Fashola",
            "Folarin", "Garba", "Gbadebo", "Ibukunoluwa", "Ige", "Ilesanmi",
            "Iloabuchi", "Isiaka",
            "Kadiri", "Kalu", "Kanu", "Kasali", "Kolawole", "Lawal", "Madueke",
            "Makinde", "Mba",
            "Mogaji", "Mohammed", "Murtala", "Nwachukwu", "Nwafor", "Nwankwo",
            "Nwanze", "Obaseki",
            "Odumegwu", "Okafor", "Okeke", "Okoro", "Olumide", "Olanipekun",
            "Olusegun", "Omotayo",
            "Onifade", "Onuoha", "Opara", "Osuji", "Otunla", "Oyebade",
            "Oyekan", "Oyeleke",
            "Oyewole", "Sanni", "Shola", "Suleiman", "Taiwo", "Ugwu",
            "Unachukwu", "Yakubu",
            "Yusuf", "Zakari", "Awe", "Olayinka", "Rotimi", "Korede",
            "Adebisi", "Gbemi",
            "Boluwatife", "Ayotunde", "Morounkeji", "Titilayo", "Iretiola",
            "Odusanya", "Sotunde",
            "Folusho", "Temiloluwa", "Ayomide", "Oluwadamilola", "Ayinde",
            "Olamide", "Olajumoke",
            "Oluwatoyin", "Bolaji", "Abiola", "Aderinsola", "Omowunmi",
            "Bamgbose", "Omodara",
            "Oluwatosin", "Oreoluwa", "Enitan", "Oluwadunni", "Ayodeji",
            "Ewatomilola", "Tolulope",
            "Mojisola", "Jumoke", "Adewumi", "Oluremi", "Titilope", "Ajibade",
            "Aramide", "Balikis",
            "Ashimolowo", "Opemipo", "Abdulahi", "Ayokunle", "Ifetayo",
            "Anjolaoluwa"
        ]

        # Create sample users
        users = []
        for i in nigerian_names:
            user = AUser.objects.create(
                username=i,
                age=random.randint(18, 60),
                location=random.choice(["New York", "London", "Lagos", "Tokyo"]),
                gender=random.choice(["Male", "Female"]),
                segment=random.choice(["new", "returning", "VIP"])
            )
            users.append(user)

        # Populate UserActivity
        for user in users:
            UserActivity.objects.create(
                user=user,
                login_count=random.randint(1, 20),
                last_login=timezone.now() - timedelta(days=random.randint(1, 30)),
                session_duration=timedelta(minutes=random.randint(5, 120)),
                time_spent=random.randint(30, 1000),
                most_accessed_feature=random.choice(["dashboard", "profile", "analytics"])
            )

        # Populate UserEngagement
        for user in users:
            UserEngagement.objects.create(
                user=user,
                click_through_rate=round(random.uniform(1.0, 10.0), 2),
                interaction_rate=round(random.uniform(1.0, 20.0), 2),
                retention_metric=round(random.uniform(50.0, 100.0), 2),
                conversion_rate=round(random.uniform(0.0, 10.0), 2)
            )

        # Populate UserBehavior
        for user in users:
            UserBehavior.objects.create(
                user=user,
                purchase_history=";".join([f"item_{i}" for i in range(random.randint(1, 5))]),
                content_consumption=";".join([f"content_{i}" for i in range(random.randint(1, 10))]),
                preferences=random.choice(["sports", "tech", "entertainment", "education"])
            )

        # Populate EventTracking
        for user in users:
            for _ in range(3):  # Multiple actions per user
                EventTracking.objects.create(
                    user=user,
                    action=random.choice(["button_click", "form_submit", "link_click"]),
                    timestamp=timezone.now() - timedelta(days=random.randint(1, 30)),
                    funnel_stage=random.choice(["awareness", "consideration", "decision"])
                )

        # Populate ChurnData
        for user in users:
            ChurnData.objects.create(
                user=user,
                churned=random.choice([True, False]),
                cancellation_reason="Too expensive" if random.choice([True, False]) else "",
                feedback="I enjoyed using the service." if random.choice([True, False]) else ""
            )

        # Populate PerformanceData
        for _ in range(5):  # Multiple records for server performance
            PerformanceData.objects.create(
                response_time=round(random.uniform(0.1, 1.5), 2),
                error_count=random.randint(0, 5),
                downtime=timedelta(minutes=random.randint(0, 60)),
                api_usage_count=random.randint(50, 1000),
                timestamp=timezone.now() - timedelta(days=random.randint(1, 30))
            )

        self.stdout.write(self.style.SUCCESS("Sample data populated successfully."))
