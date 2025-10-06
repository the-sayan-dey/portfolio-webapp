from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=10, default='🎓')
    
    class Meta:
        ordering = ['-year']
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Certificate(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    issue_date = models.DateField()
    credential_url = models.URLField(blank=True)
    icon = models.CharField(max_length=10, default='🏆')
    
    class Meta:
        ordering = ['-issue_date']
    
    def __str__(self):
        return f"{self.name} - {self.issuer}"
    


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text="Comma-separated technologies")
    demo_url = models.URLField(blank=True, help_text="Live demo link")
    github_url = models.URLField(blank=True, help_text="GitHub repository link")
    icon = models.CharField(max_length=10, default='🚀')
    created_at = models.DateField(auto_now_add=True)
    order = models.IntegerField(default=0, help_text="Lower number = appears first")
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title