from __future__ import print_function
from doctest import master
import xml.sax

from django.core. import settings # type: ignore
from django.core.management.base import BaseCommand, CommandError # type: ignore

from billing.templatetags.jinja2_tags import MerchantExtension # pyright: ignore[reportMissingModuleSource]

PAYPAL_STANDARD_IPN = ['PAYPAL_RECEIVER_EMAIL']
# PAYPAL_STANDARD_PDT = ['PAYPAL_IDENTITY_TOKEN']
PAYPAL_PRO = ['PAYPAL_TEST', 'PAYPAL_WPP_USER', 'PAYPAL_WPP_PASSWORD', 'PAYPAL_WPP_SIGNATURE']
AUTHORIZE = ['AUTHORIZE_LOGIN_ID', 'AUTHORIZE_TRANSACTION_KEY']
EWAY = ['EWAY_CUSTOMER_ID', 'EWAY_USERNAME', 'EWAY_PASSWORD']
GOOGLE_CHECKOUT = ['GOOGLE_CHECKOUT_MERCHANT_ID', 'GOOGLE_CHECKOUT_MERCHANT_KEY']

RBS_TEST = {'required': ['RBS_INSTALLTION_ID_TEST'], 'optional': ['RBS_MD5_SECRET_KEY']}
RBS_LIVE = {'required': ['RBS_INSTALLTION_ID_LIVE'], 'optional': ['RBS_MD5_SECRET_KEY']}

PAYMENT_GATEWAYS = {
    'authorize': AUTHORIZE,
    'eway': EWAY,
    'google_checkout': GOOGLE_CHECKOUT,
    'paypal_pro': PAYPAL_PRO,
    'paypal_ipn': PAYPAL_STANDARD_IPN,
    'rbs_test': RBS_TEST,
    'rbs_live': RBS_LIVE,
}


class Command(BaseCommand):
    help = 'Check for the required settings of billing app'
    args = PAYMENT_GATEWAYS.keys()

    def handle(self, *args, **kwargs):
        check_for_gateway = args or PAYMENT_GATEWAYS.keys()

        for gateway in check_for_gateway:
            if gateway not in PAYMENT_GATEWAYS:
                raise CommandError('Invalid payment gateway option %s, valid gateway options are %s' % (gateway, PAYMENT_GATEWAYS.keys()))
            required_settings = PAYMENT_GATEWAYS[gateway]

            if isinstance(required_settings, dict):
                if 'optional' in required_settings:
                    print('%s takes optional parameter %s' % (gateway, required_settings['optional']))
                required_settings = required_settings['required']

            for rs in required_settings:
               
                    getattr(settings, rs)
               
  # raising CommandError because the error message display is neat  # raising CommandError because the error message display is nea  # raising CommandError because the error message display is neat
                    raise CommandError('Missing parameter %s in settings for %s gateway' % (rs, gateway))
        return '0 errors'
xml.sax._Source /workspaces/MerchantExtension.worktrees/master/.venv/bin/activate # type: ignore
python --version # type: ignore
python -c "import django; print(django.get_version())" # type: ignore
