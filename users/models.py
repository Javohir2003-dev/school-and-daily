from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver







# Student model 

class Student(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone = models.CharField(max_length=15, blank=True, null=True)
    status = models.BooleanField(default=True)
    classes = models.ForeignKey("sciences.Classes", on_delete=models.CASCADE, related_name='oquvchi_sinf')
    date_of_join = models.DateField()
    last_login_date = models.DateField(null=True, blank=True)
    last_login_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, null=True, blank=True)

    def __str__(self):
        return f"{self.last_name} -- {self.first_name}"



class Student_Profile(models.Model):
    first_name = models.CharField(max_length=45,blank=True, null=True)
    last_name = models.CharField(max_length=45,blank=True, null=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='student_profile')
    bio = models.CharField(max_length=170, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    image = models.ImageField(upload_to='user/',null=True, blank=True)

    def __str__(self):
        return f"{self.last_name} -- {self.first_name}"
    


@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):
    if created:

        student_profile = Student_Profile.objects.create(student=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            phone=instance.phone
        )
        instance.profile = student_profile
        instance.save()

    else:  
        if instance.student_profile:
            instance.student_profile.first_name = instance.first_name
            instance.student_profile.last_name = instance.last_name
            instance.student_profile.phone = instance.phone
            instance.student_profile.save()


@receiver(post_save, sender=Student)
def save_student_profile(sender, instance, **kwargs):
    instance.student_profile.save()





# Teacher model 

class Teacher(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone = models.CharField(max_length=15, blank=True, null=True)
    status = models.BooleanField(default=True)
    last_login_date = models.DateField(null=True, blank=True)
    last_login_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, null=True, blank=True)

    def __str__(self):
        return f"{self.last_name} -- {self.first_name}"
    



class Teacher_Profile(models.Model):
    first_name = models.CharField(max_length=45,blank=True, null=True)
    last_name = models.CharField(max_length=45,blank=True, null=True)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='teacher_profile')
    bio = models.CharField(max_length=170, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    image = models.ImageField(upload_to='user/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.last_name} -- {self.first_name}"
    

    
@receiver(post_save, sender=Teacher)
def create_teacher_profile(sender, instance, created, **kwargs):
    if created:

        teacher_profile = Teacher_Profile.objects.create(teacher=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            phone=instance.phone
        )
        instance.profile = teacher_profile
        instance.save()

    else:  
        if instance.teacher_profile:
            instance.teacher_profile.first_name = instance.first_name
            instance.teacher_profile.last_name = instance.last_name
            instance.teacher_profile.phone = instance.phone
            instance.teacher_profile.save()


@receiver(post_save, sender=Teacher)
def save_teacher_profile(sender, instance, **kwargs):
    instance.teacher_profile.save()
    


    


class Parent(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone = models.CharField(max_length=15, blank=True, null=True)
    status = models.BooleanField(default=True)
    last_login_date = models.DateField(null=True, blank=True)
    last_login_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, null=True, blank=True)

    def str(self):
        return f"{self.first_name} {self.last_name}"
    


