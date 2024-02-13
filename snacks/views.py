from django.views.generic import TemplateView

class HomePageView(TemplateView):
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["snacks"] = [
        {
          "iamge_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Pink_lady_and_cross_section.jpg/1920px-Pink_lady_and_cross_section.jpg",
          "title": "Apple",
          "description": "An apple a day something something...",
          "reference_url": "https://en.wikipedia.org/wiki/Apple"
        },
      ]
      return context
  
class AboutPageView(TemplateView):

  template_name = 'about.html'

# Create your views here.
