#!/usr/bin/env python3
import os
import json
import requests
import random

TEXT_GEN_API_VAR = 'DEEP_AI_KEY'

words = [
    'The', 'he', 'at', 'but', 'there', 'of', 'was', 'be', 'not', 'use', 'and', 'for', 'this', 'what', 'an', 'a', 'on', 'have', 'all', 'each',
    'to', 'are', 'from', 'were', 'which', 'in', 'as', 'or', 'we', 'she', 'is', 'with', 'ine', 'when', 'do', 'you', 'his', 'had', 'your',
    'how', 'that', 'they', 'by', 'can', 'their', 'it', 'I', 'word', 'said', 'if'
]

with open(os.path.join(os.path.dirname(__file__), './data/cities.json')) as cities_file:
    cities = json.load(cities_file)

gop_members = [
    'Gary VanDeaver', 'Bryan Slaton', 'Cecil Bell Jr.', 'Keith Bell', 'Cole Hefner', 'Matt Schaefer', 'Jay Dean', 'Cody Harris',
    'Chris Paddie', 'Travis Clardy', 'Kyle Kacal', 'Ben Leman', 'John N. Raney', 'Steve Toth', 'Will Metcalf', 'John Cyrier', 'Ernest Bailes',
    'James White', 'Terry Wilson', 'Dade Phelan', 'Mayes Middleton', 'Greg Bonnen', 'Cody Vasut', 'Brooks Landgraf', 'Tom Craddick',
    'Dustin Burrows', 'John Frullo', 'Phil Stephenson', 'John T. Smithee', 'Four Price', 'Ken King', 'Candy Noble', 'Stephanie Klick',
    'Jeff Cason', 'Matt Krause', 'Tony Tinderholt', 'David Cook', 'Craig Goldman', 'Giovanni Capriglione', 'Charlie Geren', 'Sam Harless',
    'Dan Huberty', 'Briscoe Cain', 'Dennis Paul', 'Tom Oliverson', 'Mike Schofield'
]
firstNames = ['Hannah', 'Olivia', 'Marcia', 'Sarah',
              'Tara', 'Brooke', 'Wanda', 'Andrea', 'Julie']

maleFirstNames = [
    'Michael',
    'Christopher',
    'Matthew',
    'Joshua',
    'Jacob',
    'Nicholas',
    'Andrew',
    'Daniel',
    'Tyler',
    'Joseph',
    'Brandon',
    'David',
    'James',
    'Ryan',
    'John',
    'Zachary',
    'Justin',
    'William',
    'Anthony',
    'Robert',
    'Patrick',
]

lastNames = [
    'Morgan', 'Walker', 'Lewis', 'Butler', 'Jones', 'Barnes', 'Martin', 'Wright', 'Foster', 'Smith', 'Johnson', 'Williams', 'Brown', 'Miller',
    'Davis', 'Garcia', 'Rodriguez', 'Wilson', 'Martinez', 'Anderson', 'Taylor', 'Thomas', 'Hernandez', 'Jackson', 'Thompson', 'White'
]

# Seeds for text body generation
gpt2_prompts = [
    'My neighbor got an illegal abortion.', 'I suspect my father has violated the abortion ban.',
    random.choice(firstNames) + ' ' + random.choice(lastNames) +
    ' is helping people get abortions.',
    random.choice(gop_members) + ' has been sneaking around the abortion clinic in ' +
    random.choice(list(cities)) + '.'
]

info_location = [
    'A friend saw them', 'I work at the clinic', 'I know his secretary', 'He told me at the club', 'The police report', 'His wife told me',
    'From a coworker', 'From a neighbor', 'From a family member.', 'Heard from a friend', 'a relative told me', 'a private source',
    'A confession at church', 'I know their cousin', 'a taxi driver', 'From a cashier', 'Got a confidential tip', 'From a fellow parent',
    'a concerned citizen', 'From a relative.', 'A PP volunteer', 'A charity worker', 'A social worker', 'From my friend who knows cops',
    'from a lawyer', 'From a government employee'
]


hatePhrase = [
    ' I wouldn\'t breath the same air.',                    ' I wouldn\'t touch them with a ten-foot pole!',
    ' I unfortunately won\'t be voting red for a while.',   ' I\'m sick to my stomach just thinking about it.',
    ' Oh, that makes my skin crawl!',                       ' I think it\'s quite nauseating!',
    ' "You shall not murder." Exodus 20:13',                ' Shame on these monsters!',
    ' "Children are a heritage from the LORD, offspring a reward from him." Psalm 127:3',
    ' "Like arrows in the hands of a warrior are children born in one’s youth." Psalm 127:4', '',
]

zipDict = {
    'ArlingtonZips': [76010, 76017, 76014, 76001, 76002, 76016, 76013, 76018, 76012, 76006, 76011, 76015, 76060, 76063, 75050, 75051, 75052, 76005, 76040, 76112, 76119, 76120, 76019, 76003, 76004, 76007, 76094, 76096, ],
    'AustinZips': [78745, 78745, 78753, 78741, 78758, 78704, 78744, 78759, 78748, 78749, 78705, 78723, 78727, 78750, 78731, 78702, 78757, 78703, 78752, 78717, 78724, 78739, 78751, 78735, 78746, 78721, 78726, 78747, 78754, 78617, 78729, 78730, 78701, 78756, 78722, 78736, 78653, 78660, 78732, 78652, 78712, 78725, 78733, 78742, 78610, 78613, 78641, 78664, 78681, 78710, 78719, 78728, 78734, 78737, 78738, 78798, 78799, ],
    'Corpus ChristiZips': [78415, 78413, 78412, 78414, 78418, 78411, 78410, 78404, 78408, 78401, 78417, 78407, 78409, 78406, 78402, 78419, 78373, 78374, 78380, 78470, 78471, 78473, 78474, 78475, 78405, 78416, 78362, 78370, 78476, 78477, 78478, ],
    'DallasZips': [75217, 75211, 75228, 75227, 75243, 75216, 75287, 75220, 75231, 75206, 75214, 75224, 75248, 75229, 75208, 75238, 75232, 75204, 75230, 75241, 75212, 75240, 75252, 75254, 75218, 75219, 75253, 75235, 75237, 75203, 75236, 75215, 75223, 75233, 75209, ],
    'El PasoZips': [79936, 79912, 79924, 79907, 79925, 79915, 79938, 79904, 79930, 79905, 79932, 79902, 79934, 79903, 79935, 79901, 79922, 79928, 79927, 79908, 79911, 79835, 79821, 79906, ],
    'Fort WorthZips': [76244, 76133, 76116, 76137, 76112, 76119, 76106, 76110, 76123, 76179, 76107, 76132, 76105, 76115, ],
    'GarlandZips': [75040, 75043, 75044, 75042, 75041, 75048, 75081, 75082, 75089, 75098, 5150, 75218, 75228, 75238, 75243, 75045, 75046, 75047, 75049, ],
    'HoustonZips': [77036, 77072, 77077, 77081, 77080, 77099, 77057, 77009, 77055, 77074, 77075, 77035, 77042, 77087, 77004, 77034, 77063, 77076, 77082, 77092, 77096, 77339, 77007, 77008, 77017, 77045, 77079, 77088, 77022, 77023, 77060, 77016, 77033, 77053, 77018, 77020, 77021, 77025, 77061, 77062, 77093, 77345, 77026, 77043, 77054, 77089, 77091, 77012, 77024, 77071, 77006, 77011, 77019, 77040, 77056, 77002, 77013, 77028, 77085, 77489, 77015, 77027, 77031, 77047, 77048, 77051, 77059, 77078, 77084, 77098, 77003, 77005, 77030, 77598, 77041, 77044, 77058, 77067, 77029, ],
    'IrvingZips': [75061, 75062, 75060, 75063, 75038, 75039, 75050, 75220, 75234, 75247, 75037, 75059, 75064, 75014, 75015, 75016, 75017,	],
    'LaredoZips': [78046, 78045, 78041, 78040, 78043, 78049, 78042, 78044, ],
    'LubbockZips': [79311, 79329, 79343, 79401, 79403, 79404, 79406, 79407, 79410, 79411, 79412, 79413, 79414, 79415, 79416, 79423, 79424, 79350, 79250, 79366, 79358, 79363, 79364, 79382, ],
    'PlanoZips': [75025, 75093, 75023, 75074, 75024, 75075, 75094, 75010, 75013, 75082, 75252, 75287, 75026, 75086, ],
    'San AntonioZips': [78228, 78207, 78250, 78247, 78249, 78251, 78240, 78227, 78223, 78201, 78216, 78230, 78210, 78237, 78213, 78258, 78221, 78211, 78217, 78218, 78242, 78232, 78233, 78229, 78209, 78245, 78212, 78214, 78254, 78259, 78222, 78224, 78238, 78220, 78225, 78248, 78202, 78023, 78204, 78244, 78203, 78219, 78226, 78231, 78234, 78256, 78239, 78260, 78109, 78208, 78255, 78257, 78205, 78215, 78252, 78266, 78056, 78073, 78112, 78154, 78206, 78235, 78236, 78241, 78243, 78253, 78261, 78262, 78263, 78264, 78284, 78285, 78275, 78286, 78287, 78288, 78289, 78246, 78265, 78268, 78269, 78270, 78278, 78279, 78280, 78283, 78291, 78292, 78293, 78294, 78295, 78296, 78297, 78298, 78299, ],
}

zip_codes = [
    75001,    75006,    75011,    75014,    75015,    75016,    75017,    75019,    75030,    75038,    75039,    75040,    75041,    75042,    75043,    75044,    75045,    75046,    75047,    75048,    75048,    75049,    75050,
    75051,    75052,    75053,    75054,    75060,    75061,    75062,    75063,    75080,    75081,    75082,    75083,    75085,    75088,    75089,    75104,    75106,    75115,    75116,    75123,
    75134,    75137,    75138,    75141,    75146,    75149,    75150,    75159,    75159,    75172,    75180,    75180,    75181,    75182,    75182,    75185,    75187,    75201,    75202,
    75203,    75204,    75205,    75206,    75207,    75208,    75209,    75210,    75211,    75212,    75214,    75215,    75216,    75217,    75218,    75219,    75220,
    75221,    75222,    75223,    75224,    75225,    75226,    75227,    75228,    75229,    75230,    75231,    75232,    75233,    75234,    75234,    75235,    75236,    75237,    75238,    75239,
    75240,    75241,    75242,    75243,    75244,    75244,    75245,    75246,    75247,    75248,    75249,    75250,    75251,    75253,    75254,    75258,    75260,
    75261,    75262,    75263,    75264,    75265,    75266,    75267,    75270,    75295,    75313,    75315,    75336,    75339,    75342,    75354,    75355,    75356,
    75357,    75359,    75360,    75367,    75370,    75371,    75372,    75374,
    75376,    75378,    75379,    75380,    75381,    75382,    75398, ]
# TX IPs gathered from here: https://www.xmyip.com/ip-addresses/united--states/texas
ips = [
    "15.180.224.",  # San Antonio
    "15.155.5.",  # San Antonio
    "15.153.133.",  # San Antonio
    "12.56.225.",  # Dallas
    "67.10.46."  # Edinburg
]
# random element from each list


def anonymous_form():
    while True:
        city, county = random.choice(list(cities.items()))
        form_data = {
            'textarea-1': get_tip_body(),
            'text-1': random.choice(info_location),
            'text-6': 'Dr. ' + random.choice(maleFirstNames) + ' ' + random.choice(lastNames),
            'text-2': city,
            'text-3': 'Texas',
            'text-4': str(random.randint(75001, 79942)),
            'text-5': county,
            'hidden-1': random.choice(ips) + str(random.randint(0, 255)),
            'checkbox-1[]': 'yes' if random.choice([True, False]) else 'no',
        }
        yield form_data

    # def anonymous_form():
    #   while True:
    #       cityNum = random.randint(0, len(cities))
    #       city = list(cities)[cityNum-1]
    #       county = list(cities.values())[cityNum-1]
    #       zipCode = random.choice(zipDict.get(f'{list(cities)[cityNum-1]}Zips'))
    #       form_data = {
    #           'textarea-1': random.choice(gop_members) + ' took their mistress ' + random.choice(firstNames) + ' ' + random.choice(lastNames) +
    #           ' to get an abortion after their affair.' +
    #           random.choice(list(hatePhrase)),
    #           'text-1': random.choice(info_location),
    #           'text-6': 'Dr. ' + (random.choice(list(gop_members))[0] if random.choice([True, False]) else random.choice(list(firstNames))) + ' ' + random.choice(lastNames),
    #           'text-2': city,
    #           'text-3': 'Texas',
    #           'text-4': zipCode,
    #           'text-5': county,
    #           'hidden-1': random.choice(ips) + str(random.randint(0, 255)),
    #           'checkbox-1[]': 'yes' if random.choice([True, False]) else 'no',
    #       }
    #       yield form_data


def sign_up_page():
    raise NotImplementedError()


def get_tip_body():
    # If we have an API key for GPT2, use it
    if TEXT_GEN_API_VAR in os.environ:
        prompt = random.choice(gpt2_prompts)
        r = requests.post(
            "https://api.deepai.org/api/text-generator", data={
                'text': prompt,
            }, headers={'api-key': os.environ[TEXT_GEN_API_VAR]}
        )
        rv = str(r.json()['output'].encode('utf-8'))
        # cut out the prompt, which comes from a limited set and can be filtered on
        rv = rv.replace(prompt, '').lstrip()
        # take string up through last complete sentence since we occasionally get trailing words
        if '.' in rv:
            rv = rv[0:rv.rindex('.')] + '.'
        return rv
    else:
        # standard tip body generation
        return random.choice(gop_members) + ' took their mistress ' + random.choice(firstNames) + ' ' + random.choice(
            lastNames
        ) + ' to get an abortion after their affair.'
