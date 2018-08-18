# Generated by Django 2.0 on 2018-06-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20180614_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smeprofile',
            name='currency',
            field=models.CharField(choices=[('MOP', 'Pataca (MOP)'), ('HNL', 'Lempira (HNL)'), ('HUF', 'Forint (HUF)'), ('LKR', 'Sri Lanka Rupee (LKR)'), ('XOF', 'CFA Franc BCEAO (XOF)'), ('TWD', 'New Taiwan Dollar (TWD)'), ('SCR', 'Seychelles Rupee (SCR)'), ('XAU', 'Gold (XAU)'), ('DOP', 'Dominican Peso (DOP)'), ('TVD', 'Tuvalu dollar (TVD)'), ('TND', 'Tunisian Dinar (TND)'), ('COU', 'Unidad de Valor Real (COU)'), ('CNY', 'Yuan Renminbi (CNY)'), ('UGX', 'Uganda Shilling (UGX)'), ('XYZ', 'Default currency. (XYZ)'), ('ZMW', 'Zambian Kwacha (ZMW)'), ('MMK', 'Kyat (MMK)'), ('DJF', 'Djibouti Franc (DJF)'), ('HKD', 'Hong Kong Dollar (HKD)'), ('LYD', 'Libyan Dinar (LYD)'), ('FJD', 'Fiji Dollar (FJD)'), ('FKP', 'Falkland Islands Pound (FKP)'), ('USD', 'US Dollar (USD)'), ('STD', 'Dobra (STD)'), ('BGN', 'Bulgarian Lev (BGN)'), ('XCD', 'East Caribbean Dollar (XCD)'), ('BHD', 'Bahraini Dinar (BHD)'), ('LRD', 'Liberian Dollar (LRD)'), ('SZL', 'Lilangeni (SZL)'), ('BZD', 'Belize Dollar (BZD)'), ('UYU', 'Uruguayan peso (UYU)'), ('WST', 'Tala (WST)'), ('XBA', 'Bond Markets Units European Composite Unit (EURCO) (XBA)'), ('XFU', 'UIC-Franc (XFU)'), ('NOK', 'Norwegian Krone (NOK)'), ('XSU', 'Sucre (XSU)'), ('DZD', 'Algerian Dinar (DZD)'), ('MZN', 'Metical (MZN)'), ('AOA', 'Kwanza (AOA)'), ('AFN', 'Afghani (AFN)'), ('LSL', 'Lesotho loti (LSL)'), ('PAB', 'Balboa (PAB)'), ('MAD', 'Moroccan Dirham (MAD)'), ('BSD', 'Bahamian Dollar (BSD)'), ('UYI', 'Uruguay Peso en Unidades Indexadas (URUIURUI) (UYI)'), ('BRL', 'Brazilian Real (BRL)'), ('TMM', 'Manat (TMM)'), ('KHR', 'Riel (KHR)'), ('SAR', 'Saudi Riyal (SAR)'), ('BBD', 'Barbados Dollar (BBD)'), ('AZN', 'Azerbaijanian Manat (AZN)'), ('CHE', 'WIR Euro (CHE)'), ('NGN', 'Naira (NGN)'), ('VEF', 'Bolivar Fuerte (VEF)'), ('RON', 'New Leu (RON)'), ('CRC', 'Costa Rican Colon (CRC)'), ('RWF', 'Rwanda Franc (RWF)'), ('IMP', 'Isle of Man Pound (IMP)'), ('NZD', 'New Zealand Dollar (NZD)'), ('XDR', 'SDR (XDR)'), ('CHF', 'Swiss Franc (CHF)'), ('UAH', 'Hryvnia (UAH)'), ('UZS', 'Uzbekistan Sum (UZS)'), ('HTG', 'Haitian gourde (HTG)'), ('ISK', 'Iceland Krona (ISK)'), ('ZWN', 'Zimbabwe dollar A/08 (ZWN)'), ('SLL', 'Leone (SLL)'), ('XFO', 'Gold-Franc (XFO)'), ('NAD', 'Namibian Dollar (NAD)'), ('BDT', 'Taka (BDT)'), ('MDL', 'Moldovan Leu (MDL)'), ('CUP', 'Cuban Peso (CUP)'), ('YER', 'Yemeni Rial (YER)'), ('BYR', 'Belarussian Ruble (BYR)'), ('EUR', 'Euro (EUR)'), ('MRO', 'Ouguiya (MRO)'), ('ILS', 'New Israeli Sheqel (ILS)'), ('BWP', 'Pula (BWP)'), ('ALL', 'Lek (ALL)'), ('GIP', 'Gibraltar Pound (GIP)'), ('GTQ', 'Quetzal (GTQ)'), ('JPY', 'Yen (JPY)'), ('TOP', 'Paanga (TOP)'), ('JOD', 'Jordanian Dinar (JOD)'), ('MVR', 'Rufiyaa (MVR)'), ('KES', 'Kenyan Shilling (KES)'), ('DKK', 'Danish Krone (DKK)'), ('AUD', 'Australian Dollar (AUD)'), ('PGK', 'Kina (PGK)'), ('XAF', 'CFA franc BEAC (XAF)'), ('SSP', 'South Sudanese Pound (SSP)'), ('CAD', 'Canadian Dollar (CAD)'), ('KPW', 'North Korean Won (KPW)'), ('AED', 'UAE Dirham (AED)'), ('CLF', 'Unidad de Fomento (CLF)'), ('TTD', 'Trinidad and Tobago Dollar (TTD)'), ('CDF', 'Congolese franc (CDF)'), ('AMD', 'Armenian Dram (AMD)'), ('KGS', 'Som (KGS)'), ('XUA', 'ADB Unit of Account (XUA)'), ('THB', 'Baht (THB)'), ('ANG', 'Netherlands Antillian Guilder (ANG)'), ('CZK', 'Czech Koruna (CZK)'), ('SEK', 'Swedish Krona (SEK)'), ('PEN', 'Nuevo Sol (PEN)'), ('XPF', 'CFP Franc (XPF)'), ('RSD', 'Serbian Dinar (RSD)'), ('SHP', 'Saint Helena Pound (SHP)'), ('LBP', 'Lebanese Pound (LBP)'), ('AWG', 'Aruban Guilder (AWG)'), ('KWD', 'Kuwaiti Dinar (KWD)'), ('LVL', 'Latvian Lats (LVL)'), ('GMD', 'Dalasi (GMD)'), ('SBD', 'Solomon Islands Dollar (SBD)'), ('BIF', 'Burundi Franc (BIF)'), ('CLP', 'Chilean peso (CLP)'), ('XBD', 'European Unit of Account 17(E.U.A.-17) (XBD)'), ('SYP', 'Syrian Pound (SYP)'), ('IQD', 'Iraqi Dinar (IQD)'), ('SOS', 'Somali Shilling (SOS)'), ('QAR', 'Qatari Rial (QAR)'), ('INR', 'Indian Rupee (INR)'), ('CHW', 'WIR Franc (CHW)'), ('CVE', 'Cape Verde Escudo (CVE)'), ('GEL', 'Lari (GEL)'), ('RUB', 'Russian Ruble (RUB)'), ('GHS', 'Ghana Cedi (GHS)'), ('MWK', 'Malawian Kwacha (MWK)'), ('MUR', 'Mauritius Rupee (MUR)'), ('TMT', 'Turkmenistan New Manat (TMT)'), ('PLN', 'Zloty (PLN)'), ('ERN', 'Nakfa (ERN)'), ('XBC', 'European Unit of Account 9(E.U.A.-9) (XBC)'), ('PYG', 'Guarani (PYG)'), ('ZWL', 'Zimbabwe dollar A/09 (ZWL)'), ('ZMK', 'Zambian Kwacha (ZMK)'), ('MXV', 'Mexican Unidad de Inversion (UDI) (MXV)'), ('TRY', 'Turkish Lira (TRY)'), ('XAG', 'Silver (XAG)'), ('ZWD', 'Zimbabwe Dollar A/06 (ZWD)'), ('KYD', 'Cayman Islands Dollar (KYD)'), ('HRK', 'Croatian Kuna (HRK)'), ('PKR', 'Pakistan Rupee (PKR)'), ('TZS', 'Tanzanian Shilling (TZS)'), ('KZT', 'Tenge (KZT)'), ('NPR', 'Nepalese Rupee (NPR)'), ('XXX', 'The codes assigned for transactions where no currency is involved (XXX)'), ('BMD', 'Bermudian Dollar (customarily known as Bermuda Dollar) (BMD)'), ('SVC', 'El Salvador Colon (SVC)'), ('KRW', 'Won (KRW)'), ('IDR', 'Rupiah (IDR)'), ('BAM', 'Convertible Marks (BAM)'), ('MNT', 'Tugrik (MNT)'), ('XPT', 'Platinum (XPT)'), ('GYD', 'Guyana Dollar (GYD)'), ('VUV', 'Vatu (VUV)'), ('MYR', 'Malaysian Ringgit (MYR)'), ('XBB', 'European Monetary Unit (E.M.U.-6) (XBB)'), ('BND', 'Brunei Dollar (BND)'), ('VND', 'Dong (VND)'), ('TJS', 'Somoni (TJS)'), ('NIO', 'Cordoba Oro (NIO)'), ('GBP', 'Pound Sterling (GBP)'), ('PHP', 'Philippine Peso (PHP)'), ('USN', 'US Dollar (Next day) (USN)'), ('ZAR', 'Rand (ZAR)'), ('ARS', 'Argentine Peso (ARS)'), ('MKD', 'Denar (MKD)'), ('OMR', 'Rial Omani (OMR)'), ('SGD', 'Singapore Dollar (SGD)'), ('MGA', 'Malagasy Ariary (MGA)'), ('SDG', 'Sudanese Pound (SDG)'), ('BTN', 'Bhutanese ngultrum (BTN)'), ('JMD', 'Jamaican Dollar (JMD)'), ('BOV', 'Mvdol (BOV)'), ('COP', 'Colombian peso (COP)'), ('LAK', 'Kip (LAK)'), ('SRD', 'Surinam Dollar (SRD)'), ('XTS', 'Codes specifically reserved for testing purposes (XTS)'), ('ETB', 'Ethiopian Birr (ETB)'), ('EGP', 'Egyptian Pound (EGP)'), ('MXN', 'Mexican peso (MXN)'), ('GNF', 'Guinea Franc (GNF)'), ('IRR', 'Iranian Rial (IRR)'), ('CUC', 'Cuban convertible peso (CUC)'), ('LTL', 'Lithuanian Litas (LTL)'), ('KMF', 'Comoro Franc (KMF)'), ('BOB', 'Boliviano (BOB)'), ('BYN', 'Belarussian Ruble (BYN)'), ('XPD', 'Palladium (XPD)')], max_length=50),
        ),
    ]