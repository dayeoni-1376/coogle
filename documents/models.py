from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    markdown = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    @property
    def markdown_content(self):
        return self.markdown.read().decode('utf-8')

    @classmethod
    def search_in_markdown(cls, query):
        documents = cls.objects.all()
        pk_list = [ document.pk for document in documents if query in document.markdown_content ]
        return cls.objects.filter(pk__in = pk_list)