from django.db import models


from users.models import Student,Teacher





class Classes(models.Model): # sinflar
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name


class Sciences(models.Model): # fanlar
    name = models.CharField(max_length=100)
    classes = models.ForeignKey(Classes,on_delete=models.CASCADE,related_name='classes')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='fanlar')

    def __str__(self):
        return f"{self.name} | {self.classes} "
    

class Attendance(models.Model): # yo'qlama
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='yoqlama_user')
    sciences = models.ForeignKey(Sciences, on_delete=models.CASCADE, related_name='yoqlama_fan')
    status = models.BooleanField(default=False)
    remark = models.TextField(null=True, blank=True) # izoh

    def str(self):
        return f"{self.student} - {'yes' if self.bor else 'no'} ({self.date})"


class Grade(models.Model): # baxo
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="ballar")
    sciences = models.ForeignKey(Sciences, on_delete=models.CASCADE, related_name="ballar")
    ball = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student} | {self.sciences.name} fanidan | {self.ball} ball "
    

class Exam(models.Model): # imtihon
    name = models.CharField(max_length=100)
    date = models.DateField()
    sciences = models.ForeignKey(Sciences, on_delete=models.CASCADE, related_name="imtihonlar")

    def str(self):
        return f"{self.name} -- ({self.date})"
    

class ExamResult(models.Model):  # Imtihon natijasi
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ball = models.PositiveIntegerField()