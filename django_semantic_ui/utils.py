from django.utils.html import format_html
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text
from django_semantic_ui.exceptions import SemanticUIException
from django.conf import settings


class Constant:
    """
    Default Constant used on the DSU package.
    """
    JQUERY_URL = 'https://code.jquery.com/jquery-3.1.1.min.js'
    JQUERY_INTEGRITY_HASH = 'sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8='
    JQUERY_CROSSORIGIN = 'anonymous'
    GULP_VERSION = '3.9.1'
    SEMANTIC_UI_VERSION = 'latest'
    SEMANTIC_DIRNAME = 'semantic'
    JAVASCRIPT_FILE = '/dist/semantic.min.js'
    STYLESHEET_FILE = '/dist/semantic.min.css'
    PACKAGE_NAME = 'dsu'
    STATIC_URL = '/static/'

    def __init__(self):
        pass


class Utils:
    """
    Default static methods used on the DSU package.
    """

    def __init__(self):
        pass

    @staticmethod
    def get_static_folder():
        """
        Return the STATIC url defined on the django project
        :return: STATIC url defined.
        """
        try:
            static_url = settings.STATIC_URL
        except:
            static_url = Constant.STATIC_URL
        return static_url

    @staticmethod
    def get_document_url(semantic_folder=Constant.SEMANTIC_DIRNAME, filename=None):
        """
        Get the relative path from any semantic file
        :param semantic_folder: the absolute semantic folder path
        :param filename: the filename selected
        :return: relative path from the semantic file selected.
        """
        if not filename:
            raise SemanticUIException(
                "[ERROR] The filename  from javascript, component or stylesheet is required.")
        else:
            return '{0}{1}/{2}{3}'.format(
                Utils.get_static_folder(), Constant.PACKAGE_NAME,
                semantic_folder, filename)

    @staticmethod
    def get_text_value(value=None):
        """
        Format the HTML content inside from HTML tag selected.
        :param value: HTML content unformatted inside from a HTML tag.
        :return: HTML content formatted
        """
        return force_text(value) if value else ''

    @staticmethod
    def get_attrs_formatted(attrs=None):
        """
        Format all attrs defined on a HTML tag selected.
        :param attrs: dictionary with all attrs defined in a HTML tag.
        :return: Attrs formatted.
        """
        return mark_safe(flatatt(attrs=attrs)) if attrs else ''

    @staticmethod
    def render_tag(tag, attrs=None, content=None, close=True):
        """
        Build a HTML tag with attributes, HTML content.
        :param tag: HTML tag name
        :param attrs: dictionary with all attrs defined on the HTML tag.
        :param content: HTML content added inside HTML tag.
        :param close: boolean to close HTML tag.
        :return: the HTML tag rendered.
        """
        content_formatted = Utils.get_text_value(value=content)
        attrs_formatted = Utils.get_attrs_formatted(attrs=attrs)
        html = "<{0} {1}>{2}".format(tag, attrs_formatted, content_formatted)
        html += "</{0}>".format(tag) if close or content else ""
        return format_html(
            format_string=html,
            tag=tag,
            attrs=attrs_formatted,
            content=content_formatted)
