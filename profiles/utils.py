import moneyed
import datetime
import random
import string
from django.utils.text import slugify

def get_clean_currencies():
    money_currencies = moneyed.CURRENCIES
    currs = [(cur.code, cur.name + " (" + cur.code + ")") for cur in list(money_currencies.values())]
    currs_sorted = sorted(currs, key=lambda tup: tup[1])
    bad_currs = ['XTS', 'XBB', 'XBD', 'XBC', 'XXX', 'AED', 'AFN', 'ALL', 'AMD', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BMD',
    'BND', 'BOB', 'BOV', 'BRL', 'BSD', 'BTN', 'BYN', 'BYR', 'BZD', 'CAD', 'CHE', 'CHF', 'CHW', 'CNY', 'COP', 'COU', 'CRC', 'CUC', 'CUP', 'CZK',
    'DKK', 'DOP', 'FJD', 'FKP', 'GEL', 'GIP', 'GTQ', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JMD',
    'JOD', 'JPY', 'KGS', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LSL', 'LTL', 'LVL', 'MDL', 'MKD', 'MMK', 'MNT', 'MOP', 'MVR',
    'MWK', 'MXN', 'MXV', 'MYR', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'SAR',
    'SBD', 'SDG', 'SEK', 'SGD', 'SHP', 'SRD', 'SVC', 'SYP', 'TJS', 'TMM', 'TMT', 'TRY', 'TVD', 'TWD', 'UAH', 'UYI', 'UYU', 'UZS', 'VEF', 'VND',
    'VUV', 'WST', 'XCD', 'XFO', 'XFU', 'XPD', 'XPF', 'XSU', 'YER']
    currs_cleaned = [cur for cur in currs_sorted if cur[0] not in bad_currs]
    return currs_cleaned

def sme_choices():
    """
        Helper function to retrieve all listed choices for the SME model
    """
    LEGAL_STRUCT = (
        ('BC', 'Benefit Corporation'),
        ('CO', 'Co-op'),
        ('CR', 'Corporation'),
        ('LL', 'Limited Liability Company'),
        ('NP', 'Non-Profit/Non-Governmental Organization'),
        ('PT', 'Partnership'),
        ('SP', 'Sole-Proprietorship'),
        ('OT', 'Other'),
    )
    OWNERSHIP = (
        ('WO', 'Woman Owned'),
        ('YO', 'Youth Owned'),
        ('LO', 'Local Owned'),
        ('IO', 'International Owned'),
        ('OT', 'Other'),
    )
    SECTOR = (
        ('Agriculture', (
            ('as', 'Agri-Services'),
            ('at', 'Agri-tech'),
            ('bk', 'Beauty/Skincare'),
            ('br', 'Beverages'),
            ('fu', 'Foodstuffs'),
            ('fd', 'Restaurant/ Food Retail/ Catering'))
         ),
        ('Alternative Energy', (
            ('ap', 'Appliances'),
            ('be', 'Biofuel/Ethanol'),
            ('co', 'Cooking Energy'),
            ('ha', 'HVAC Systems'),
            ('oh', 'Other'),
            ('se', 'Solar Electricity'),
            ('sw', 'Solar Water Pumps'))
         ),
        ('Business Services', (
            ('cl', 'Consulting Services'),
            ('fn', 'Financing/ Financial Services'),
            ('hr', 'Human Resources'),
            ('sp', 'Office Space/ Shared Workspace'))
         ),
         ('Craft', (
             ('ac', 'Accessories'),
             ('at', 'Art'),
             ('ct', 'Clothing'),
             ('fw', 'Footwear'),
             ('fd', 'Furniture/décor'),
             ('hc', 'Handicrafts'),
             ('jl', 'Jewelry'))
         ),
        ('Education', (
            ('bo', 'Books'),
            ('pe', 'Child Care/ primary education'),
            ('he', 'Higher Education'),
            ('pu', 'Publishing'),
            ('st', 'Skills Training'),
            ('vt', 'Vocational Training'))
         ),
        ('Other', (
            ('bm', 'BMO'),
            ('cn', 'Construction Services'),
            ('py', 'Property & Development'))
         ),
        ('Services', (
            ('or', 'Other'),)
         ),
        ('Technology', (
            ('ec', 'E-Commerce'),
            ('it', 'IT'),
            ('mm', 'Multimedia'),
            ('op', 'Online Payments'),
            ('ot', 'Other'),
            ('sc', 'Security'),
            ('sr', 'Software'))
         ),
        ('Tourism', (
            ('ld', 'House Lodging'),
            ('lf', 'Lodging and Food'))
         ),
        ('Accomodation & Food Services', (
            ('hotels', 'Hotels'),
            ('restaurants', 'Restaurants'),
            ('catering', 'Catering'),
            ('bakery', 'Bakery'),
            ('delivery', 'Food Delivery'))
         ),
         ('Waste - Health - Hygiene', (
             ('hg', 'Hygiene'),
             ('rg', 'Recycling'),
             ('we', 'Waste Management'),
             ('wr', 'Water'))
          )
    )
    YEAR_CHOICES = []
    for r in range(1970, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    return LEGAL_STRUCT, OWNERSHIP, YEAR_CHOICES, get_clean_currencies(), SECTOR


DONT_USE = ['create']
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.get_user().email)
    if slug in DONT_USE:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def add_filter_choices(context, user):
    LEGAL_STRUCT, OWNERSHIP, YEAR_CHOICES, CURRENCIES, SECTOR = sme_choices()
    context['legal_choices'] = LEGAL_STRUCT
    context['ownership'] = OWNERSHIP
    context['currencies'] = CURRENCIES
    context['sectors'] = SECTOR
    context['years'] = YEAR_CHOICES
    return context

def filter_search(self, qs):
    legal = self.request.GET.get('legal')
    owner = self.request.GET.get('owner')
    currency = self.request.GET.get('currency')
    sector = self.request.GET.get('sector')
    year = self.request.GET.get('year')
    country = self.request.GET.get('country')
    if legal:
        qs = qs.filter(legal_structure__iexact=legal)
    if owner:
        qs = qs.filter(ownership__iexact=owner)
    if currency:
        qs = qs.filter(currency__iexact=currency)
    if sector:
        qs = qs.filter(sector__iexact=sector)
    if year:
        qs = qs.filter(year_founded__iexact=year)
    if country:
        for q in qs:
            if q.get_country().name != country:
                qs = qs.exclude(user=q.get_user())
    return qs
