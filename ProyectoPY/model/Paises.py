import requests
import json

country_codes = [
    "AF", "AL", "DZ", "AD", "AO", "AG", "AR", "AM", "AU", "AT",
    "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BT",
    "BO", "BA", "BW", "BR", "BN", "BG", "BF", "BI", "KH", "CM",
    "CA", "CV", "CF", "TD", "CL", "CN", "CO", "KM", "CG", "CR",
    "HR", "CU", "CY", "CZ", "CI", "CD", "DK", "DJ", "DM", "DO",
    "EC", "EG", "SV", "GQ", "ER", "EE", "ET", "FJ", "FI", "FR",
    "GA", "GM", "GE", "DE", "GH", "GR", "GD", "GT", "GN", "GW",
    "GY", "HT", "HN", "HU", "IS", "IN", "ID", "IR", "IQ", "IE",
    "IL", "IT", "JM", "JP", "JO", "KZ", "KE", "KI", "KP", "KR",
    "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT",
    "LU", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MR",
    "MU", "MX", "FM", "MD", "MC", "MN", "ME", "MA", "MZ", "MM",
    "NA", "NR", "NP", "NL", "NZ", "NI", "NE", "NG", "NO", "OM",
    "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "QA",
    "RO", "RU", "RW", "KN", "LC", "VC", "WS", "SM", "ST", "SA",
    "SN", "RS", "SC", "SL", "SG", "SK", "SI", "SB", "SO", "ZA",
    "ES", "LK", "SD", "SR", "SZ", "SE", "CH", "SY", "TW", "TJ",
    "TZ", "TH", "TL", "TG", "TO", "TT", "TN", "TR", "TM", "TV",
    "UG", "UA", "AE", "GB", "US", "UY", "UZ", "VU", "VA", "VE",
    "VN", "YE", "ZM", "ZW",
]

country_names = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 
    'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Republic of the Congo', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Ivory Coast', 'DR Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 
    'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'North Korea', 'South Korea', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'North Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 
    'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'São Tomé and Príncipe', 
    'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Eswatini', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
]

nameToCode = dict()
for i in range(len(country_codes)):
    nameToCode[country_names[i]] = country_codes[i]



'''
codigo para obtener los nombres
for code in country_codes:
    url = f"https://restcountries.com/v3.1/alpha/{code}?fields=name"
    response = requests.get(url)
    if response.status_code == 200:
        # Access the text content of the response
        page_text = response.text
        parsed_data = json.loads(page_text)

        # Print or process the extracted text
        nombre = parsed_data['name']['common']
        print("'", nombre, "', ", end='', sep='')
    else:
        print ("", end='')
'''

