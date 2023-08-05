from django.test import TestCase
from .models import Laboratorio
from django.urls import reverse

class LaboratorioTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio 9",
            ciudad='Santiago',
            pais='Chile'
        )

    def test_model_content(self):
        self.assertEqual(self.laboratorio.nombre, 'Laboratorio 9')
        self.assertEqual(self.laboratorio.ciudad, 'Santiago')
        self.assertEqual(self.laboratorio.pais, 'Chile')
    
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/laboratorio/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("crud_lab"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app_laboratorio/laboratorio.html")
        self.assertContains(response, "Información de Laboratorios")
