from django.db import models

class OurTrainer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    expertise = models.CharField(max_length=255)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='frontend/static/frontend/images/')

    def __str__(self):
        return self.name

class PharmaceuticalCompany(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField()

    def __str__(self):
        return self.name

class TrainingProgram(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    trainer = models.ForeignKey(OurTrainer, on_delete=models.CASCADE)
    pharmaceutical_company = models.ForeignKey(PharmaceuticalCompany, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    duration = models.IntegerField()

    def __str__(self):
        return self.title

class Application(models.Model):
    training_program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    qualifications = models.TextField()
    cover_letter = models.TextField()

    def __str__(self):
        return self.applicant_name
