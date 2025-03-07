from django.db import models
import os
from datetime import date


# Create your models here.
class UserInfo(models.Model):
    image = models.ImageField(
        upload_to="images/", verbose_name="صورة", default="images/man.jpg"
    )
    militeryNumber = models.CharField(
        max_length=50, verbose_name="الرقم العسكري"
    )  # الرقم الموحد
    name = models.CharField(max_length=100, verbose_name="الاسم", unique=True)
    classification = models.CharField(
        max_length=50,
        verbose_name="التسكين",
    )

    job_classification = models.CharField(
        max_length=50,
        verbose_name="الوحدة الفرعية",
        default="تصنت",
    )
    degree_choices = (
        ("لايكن", "لايكن"),
        ("جندي", "جندي"),
        ("عريف", "عريف"),
        ("رقيب", "رقيب"),
        ("رقيب اول", "رقيب اول"),
        ("مساعد", "مساعد"),
        ("صانع دقيق", "صانع دقيق"),
        ("مساعد اول", "مساعد اول"),
    )

    dgree = models.CharField(
        max_length=50, verbose_name="الدرجة", choices=degree_choices
    )
    study = models.CharField(max_length=100, verbose_name="المؤهل الدراسي")
    getInDate = models.DateField(verbose_name="تاريخ التجنيد")
    getOutDate = models.DateField(verbose_name="تاريخ التسريح")
    curJob = models.CharField(max_length=100, verbose_name="العمل القائم به في السرية")
    preJob = models.CharField(max_length=100, verbose_name="العمل القائم قبل التجنيد")
    birthOfDate = models.DateField(verbose_name="تاريخ الميلاد")
    address = models.CharField(max_length=100, verbose_name="جهة الميلاد")
    status_choices = (("متزوج", "متزوج"), ("اعزب", "اعزب"))
    status = models.CharField(
        max_length=10, verbose_name="الحالة", choices=status_choices
    )
    fullAddress = models.CharField(max_length=100, verbose_name="محل الاقامة تفصيلياً")
    num_of_brothers_and_sisters = models.CharField(
        max_length=5, verbose_name="عدد الإخواة والأخوات"
    )
    num_of_children = models.CharField(max_length=5, verbose_name="عدد الأولاد")
    phone_number = models.CharField(max_length=12, verbose_name="رقم التليفون")
    dad_or_mom_phone_number = models.CharField(
        max_length=12, verbose_name="رقم تليفون الوالد /أقرب الأقارب"
    )
    avarol_size = models.CharField(max_length=5, verbose_name="مقاس الأفرول")
    t_shirt_size_choices = (
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("2XL", "2XL"),
        ("3XL", "3XL"),
    )

    t_shirt_size = models.CharField(
        max_length=5, verbose_name="مقاس التيشرت", choices=t_shirt_size_choices
    )
    shose1_size = models.CharField(max_length=5, verbose_name="مقاس البيادة")
    shose2_size = models.CharField(max_length=5, verbose_name="مقاس الحذاء")
    mask_size_choices = (
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
    )

    mask_size = models.CharField(
        max_length=5, verbose_name="مقاس القناع", choices=mask_size_choices
    )
    blood_class_choices = (
        ("A", "A"),
        ("A+", "A+"),
        ("B", "B"),
        ("B+", "B+"),
        ("O", "O"),
        ("O+", "O+"),
        ("AB", "AB"),
        ("AB+", "AB+"),
    )
    blood_class = models.CharField(
        max_length=10, verbose_name="فصيلة الدم", choices=blood_class_choices
    )

    hobby = models.CharField(max_length=100, verbose_name="الهواية الشخصية")
    fasela_choices = (
        ("الاولي", "الاولي"),
        ("الثانية", "الثانية"),
        ("الثالثة", "الثالثة"),
    )
    fasela = models.CharField(
        max_length=50, verbose_name="الفصيلة", default="الاولي", choices=fasela_choices
    )
    saria_choices = (
        ("الاولي", "الاولي"),
        ("الثانية", "الثانية"),
        ("الثالثة", "الثالثة"),
        ("الرابعة", "الرابعة"),
        ("الخامسة", "الخامسة"),
        ("السادسة", "السادسة"),
    )

    saria = models.CharField(
        max_length=50, verbose_name="السرية", default="الثانية", choices=saria_choices
    )
    medical_situation = models.TextField(verbose_name="الموقف الطبي", default="لايكن")
    vacation_choices = (
        ("الاولي", "الاولي"),
        ("الثانية", "الثانية"),
        ("الثالثة", "الثالثة"),
        ("الرابعة", "الرابعة"),
    )
    vacation = models.CharField(
        max_length=50,
        verbose_name="المدانية",
        default="الاولي",
        choices=vacation_choices,
    )
    seniority = models.CharField(
        max_length=50, default="0000000000", verbose_name="الاقدمية"
    )
    personal_number = models.CharField(
        max_length=50, default="0000000000", verbose_name="ت.الشخصية"
    )
    batch = models.CharField(max_length=100, default="غير محدد", verbose_name="الدفعة")
    national_id = models.CharField(
        max_length=14, default="00000000000000", verbose_name="الرقم القومي"
    )
    graduation_date = models.DateField(
        null=True, blank=True, default=None, verbose_name="تاريخ التخرج"
    )
    RANK_CHOICES = [
        ("لايكن", "لايكن"),
        ("ملازم", "ملازم"),
        ("ملازم أول", "ملازم أول"),
        ("نقيب", "نقيب"),
        ("رائد", "رائد"),
        ("رائد اح", "رائد اح"),
        ("مقدم", "مقدم"),
        ("مقدم اح", "مقدم اح"),
        ("عقيد", "عقيد"),
        ("عقيد اح", "عقيد اح"),
        ("عميد", "عميد"),
        ("عميد اح", "عميد اح"),
        ("لواء", "لواء"),
        ("لواء اح", "لواء اح"),
    ]
    rank = models.CharField(
        max_length=100, default="لايكن", verbose_name="الرتبة", choices=RANK_CHOICES
    )
    weapon = models.CharField(max_length=100, default="غير محدد", verbose_name="السلاح")
    religion = models.CharField(max_length=50, default="مسلم", verbose_name="الديانة")
    current_unit = models.CharField(
        max_length=200, default="غير محدد", verbose_name="الوحدة الحالية"
    )
    college_or_institute = models.CharField(
        max_length=200, default="أكاديمية عسكرية", verbose_name="الكلية/المهعد"
    )
    email = models.EmailField(
        default="example@domain.com", verbose_name="البريد الإلكتروني"
    )

    current_wives = models.IntegerField(default=0, verbose_name="عدد الزوجات الحاليين")
    male_children = models.IntegerField(default=0, verbose_name="ذكور")
    female_children = models.IntegerField(default=0, verbose_name="اناث")
    marriage_date = models.DateField(
        null=True, blank=True, default=None, verbose_name="تاريخ الزواج"
    )
    previous_marriages = models.IntegerField(
        default=0, verbose_name="عدد الزيجات السابقة"
    )
    divorce_date = models.DateField(
        null=True, blank=True, default=None, verbose_name="تاريخ الإنفصال"
    )

    closest_relative = models.CharField(
        max_length=200, default="غير محدد", verbose_name="أقرب الأقارب"
    )

    unified_number = models.CharField(
        max_length=50, default="غير محدد", verbose_name="الرقم الموحد"
    )
    is_officer = models.BooleanField(default=False, verbose_name="هل هو ضابط؟")
    is_soldier = models.BooleanField(default=False, verbose_name="هل هو جندي")

    class Meta:
        ordering = ["seniority"]

    def delete(self, *args, **kwargs):
        if self.image and self.image.name != "images/man.jpg":
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = UserInfo.objects.get(pk=self.pk)
            if (
                old_instance.image
                and self.image.name != old_instance.image.name
                and old_instance.image.name != "images/man.jpg"
            ):
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}-{self.name}"


class ShootingRecord(models.Model):
    user = models.ForeignKey(
        UserInfo,
        on_delete=models.CASCADE,
        verbose_name="المستخدم",
        related_name="shooting_records",
    )
    result = models.CharField(
        max_length=255, verbose_name="النتيجة", default="غير محدد"
    )
    notes = models.TextField(verbose_name="ملاحظات", default="لايكن")
    data_modified = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    date = models.DateField(default=date.today, verbose_name="التاريخ")

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.id}-{self.user.name}"


class FitnessRecord(models.Model):
    user = models.ForeignKey(
        UserInfo,
        on_delete=models.CASCADE,
        verbose_name="المستخدم",
        related_name="fitness_records",
    )
    running_rate = models.IntegerField(verbose_name="معدل الجري", default=0)
    push_up = models.IntegerField(verbose_name="عدد تمارين الضغط", default=0)
    pull_up = models.IntegerField(verbose_name="عدد تمارين السحب", default=0)
    crunch = models.IntegerField(verbose_name="عدد تمارين المعدة", default=0)
    running = models.IntegerField(verbose_name="عدد الجولات الجري", default=0)
    percentage = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="النسبة المئوية", default=0.0
    )
    weight = models.FloatField(verbose_name="الوزن", default=0.0)
    height = models.FloatField(verbose_name="الطول", default=0.0)
    notes = models.TextField(verbose_name="ملاحظات", default="")
    date = models.DateField(default=date.today, verbose_name="التاريخ")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.id}-{self.user.name}"


class EducationRecord(models.Model):
    user = models.ForeignKey(
        UserInfo,
        on_delete=models.CASCADE,
        verbose_name="المستخدم",
        related_name="education_records",
    )
    electronic_war = models.FloatField(default=0.0, verbose_name="حرب الكترونية")
    weapons = models.FloatField(default=0.0, verbose_name="أسلحة")
    military_security = models.FloatField(default=0.0, verbose_name="أمن حربي")
    topography = models.FloatField(default=0.0, verbose_name="طبوغرافيا")
    chemical_war = models.FloatField(default=0.0, verbose_name="حرب كيميائية")
    presentation_of_self_mission = models.FloatField(
        default=0.0, verbose_name="تقديم النفس+المهمة"
    )
    percentage = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="النسبة المئوية", default=0.0
    )
    notes = models.TextField(verbose_name="ملاحظات", default="")
    date = models.DateField(default=date.today, verbose_name="التاريخ")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل")

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.id}-{self.user.name}"


class LeaderOpinionRecord(models.Model):
    user = models.ForeignKey(
        UserInfo,
        on_delete=models.CASCADE,
        verbose_name="المستخدم",
        related_name="leader_opinion_records",
    )
    military_discipline = models.CharField(
        max_length=255, verbose_name="الانضباط العسكري", default="جيد"
    )
    response_to_orders = models.CharField(
        max_length=255, verbose_name="الاستجابة للأوامر", default="جيد"
    )
    execution_of_tasks = models.CharField(
        max_length=255, verbose_name="تنفيذ المهام", default="جيد"
    )
    general_appearance = models.CharField(
        max_length=255, verbose_name="المظهر العام", default="جيد"
    )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل")

    def __str__(self):
        return f"{self.id}-{self.user.name}"


class GiftRecord(models.Model):
    user = models.ForeignKey(
        UserInfo,
        on_delete=models.CASCADE,
        verbose_name="المستخدم",
        related_name="gift_records",
    )
    commander = models.CharField(max_length=255, verbose_name="القائد", default="")
    type = models.CharField(max_length=255, verbose_name="نوع المنحة", default="")
    reason = models.TextField(verbose_name="السبب", default="")
    date = models.DateField(verbose_name="التاريخ")
    number_of_days = models.IntegerField(verbose_name="عدد الأيام", default=0)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل")

    def __str__(self):
        return f"{self.id}-{self.user.name}"


class DisciplineRecord(models.Model):
    user = models.ForeignKey(
        UserInfo,
        on_delete=models.CASCADE,
        verbose_name="المستخدم",
        related_name="discipline_records",
    )
    commander = models.CharField(max_length=255, verbose_name="القائد", default="")
    reason = models.TextField(verbose_name="السبب", default="")
    type = models.CharField(max_length=255, verbose_name="النوع", default="")
    date = models.DateField(verbose_name="التاريخ")
    number_of_days = models.IntegerField(verbose_name="عدد الأيام", default=0)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل")

    def __str__(self):
        return f"{self.id}-{self.user.name}"


class VacationNote(models.Model):
    sub_unit = models.CharField(
        max_length=255, verbose_name="الوحدة الفرعية", default=""
    )
    duration = models.IntegerField(verbose_name="المدة", default=0)
    fieldwork_location = models.CharField(
        max_length=255, verbose_name="موقع العمل الميداني", default=""
    )
    notes = models.TextField(verbose_name="ملاحظات", default="")
    departure_date = models.DateField(verbose_name="تاريخ المغادرة")
    grants_discounts = models.TextField(verbose_name="الخصومات والمنح", default="")
    grade = models.CharField(max_length=255, verbose_name="الدرجة", default="")
    return_date = models.DateField(verbose_name="وقت العودة")
    name = models.CharField(max_length=255, verbose_name="الاسم", default="")
    governorate = models.CharField(max_length=255, verbose_name="المحافظة", default="")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل")

    def __str__(self):
        return f"{self.id}-{self.user.name}"

    class Meta:
        ordering = ["name"]


class EltemasRecord(models.Model):
    user = models.ForeignKey(
        UserInfo,
        on_delete=models.CASCADE,
        verbose_name="المستخدم",
        related_name="eltemas_records",
    )
    reason = models.TextField(verbose_name="السبب", default="")
    date = models.DateField(verbose_name="التاريخ")
    number_of_days = models.IntegerField(verbose_name="عدد الأيام", default=0)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل")

    def __str__(self):
        return f"{self.id}-{self.user.name}"


class Course(models.Model):
    user = models.ForeignKey(
        UserInfo,
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name="الضابط",
    )
    course_name = models.CharField(max_length=255, verbose_name="اسم الدورة")
    institution = models.CharField(
        max_length=255, verbose_name="المؤسسة", blank=True, null=True
    )
    start_date = models.DateField(verbose_name="تاريخ البداية", default="2024-12-12")
    end_date = models.DateField(verbose_name="تاريخ النهاية", blank=True, null=True)
    grade = models.CharField(max_length=255, verbose_name="اسم الدورة", default=" ")

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        return f"{self.course_name} - {self.user.name}"


class PreviousPosition(models.Model):
    user = models.ForeignKey(
        UserInfo,
        on_delete=models.CASCADE,
        related_name="previous_positions",
        verbose_name="الضابط",
    )
    position_name = models.CharField(max_length=255, verbose_name="اسم الوظيفة")
    start_date = models.DateField(verbose_name="تاريخ البداية")
    end_date = models.DateField(verbose_name="تاريخ النهاية", blank=True, null=True)

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        return (
            f"{self.position_name} ({self.start_date} - {self.end_date or 'Present'})"
        )


class PreviousUnit(models.Model):
    user = models.ForeignKey(
        UserInfo,
        on_delete=models.CASCADE,
        related_name="previous_units",
        verbose_name="الضابط",
    )
    unit_name = models.CharField(max_length=255, verbose_name="اسم الوحدة")
    start_date = models.DateField(verbose_name="تاريخ البداية")
    end_date = models.DateField(verbose_name="تاريخ النهاية", blank=True, null=True)

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        return f"{self.unit_name} ({self.start_date} - {self.end_date or 'Present'})"


class MedicalSituation(models.Model):
    user = models.ForeignKey(
        UserInfo,
        on_delete=models.CASCADE,
        related_name="medical_situations",
        verbose_name="الضابط",
    )
    date = models.DateField(verbose_name="التاريخ")
    diagnosis = models.TextField(verbose_name="التشخيص")
    hospital = models.CharField(max_length=255, verbose_name="المستشفي")
    recommendation = models.TextField(verbose_name="التوصية")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات")

    def __str__(self):
        return f"{self.date} - {self.hospital}"
