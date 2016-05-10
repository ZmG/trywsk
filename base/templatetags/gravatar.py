## From the gravatar website

### gravatar.py ###############
# place inside a 'templatetags' directory inside the top level of
# a Django app (not project, must be inside an app) at the top of
# your page template include this:
# {% load gravatar %}
# and to use the url do this:
# <img src="{% gravatar_url 'someone@somewhere.com' %}">
# or
# <img src="{% gravatar_url sometemplatevariable %}">
# just make sure to update the "default" image path below


from django import template
import urllib
import hashlib

register = template.Library()


class GravatarUrlNode(template.Node):
    def __init__(self, email, size):
        self.email = template.Variable(email)
        self.size = template.Variable(size)

    def render(self, context):
        try:
            email = self.email.resolve(context)
            size = self.size.resolve(context)
        except template.VariableDoesNotExist:
            return ''

        default = "//example.com/static/images/defaultavatar.jpg"

        if email:
            gravatar_url = "//www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
        else:
            # default image
            gravatar_url = '//www.gravatar.com/avatar/00000000000000000000000000000000?'

        # removed default until we have an actual default image we can use.
        #gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
        gravatar_url += urllib.urlencode({'s': str(size)})

        return gravatar_url


@register.tag
def gravatar_url(parser, token):
    try:
        tag_name, email, size = token.split_contents()

    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]

    gravatar_url = GravatarUrlNode(email, size)


    return gravatar_url