from django import template
from django.core import signing

register = template.Library()


@register.inclusion_tag('export/exporter.html', takes_context=False)
def exporter(btn_text, app_name, model_name ):
    """
    Usage: {% exporter "btn text" "model_name" "app_name" %}
    """

    model_name_crypt = signing.dumps(model_name)
    app_name_crypt = signing.dumps(app_name)

    return {'model': model_name_crypt, 'btn_text': btn_text, 'app':app_name_crypt }
