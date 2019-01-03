from django import template
from django_semantic_ui.utils import Utils, Constant
from django_semantic_ui.models import SemanticUI


register = template.Library()
dsu = SemanticUI()


@register.simple_tag()
def dsu_javascript_url():
    """
    Template tag that allow load the main semantic-ui javascript lib.
    example to use
    {% dsu_javascript_url %}
    :return: string
    """
    return Utils.render_tag(
        tag='script',
        attrs={
            'src': Utils.get_document_url(
                semantic_folder=dsu.semantic_folder, filename=Constant.JAVASCRIPT_FILE)
        })


@register.simple_tag()
def dsu_stylesheet_url():
    """
    Template tag that allow load the main semantic-ui stylesheet.
    example to use
    {% dsu_stylesheet_url %}
    :return:
    """
    return Utils.render_tag(
        tag='link',
        attrs={
            'href': Utils.get_document_url(
                semantic_folder=dsu.semantic_folder, filename=Constant.STYLESHEET_FILE),
            'rel': 'stylesheet',
            'type': 'text/css'}, close=False)


@register.simple_tag()
def dsu_jquery_url():
    """
    Template tag that allow load the default jquery javascript lib required by semantic-ui (this tag is optional)
    example to use
    {% dsu_jquery_url %}
    NOTE: You can change the jquery_url in your settings.py using the DSU_JQUERY_URL setting.
    :return: string
    """
    options = {'src': dsu.jquery_url}
    if Constant.JQUERY_URL == dsu.jquery_url:
        options = {
            'src': dsu.jquery_url,
            'integrity': Constant.JQUERY_INTEGRITY_HASH,
            'crossorigin': Constant.JQUERY_CROSSORIGIN}
    return Utils.render_tag(tag='script', attrs=options)
