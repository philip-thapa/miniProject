from django.http import JsonResponse


def home(request):
    return JsonResponse({
        'miniProject': 'Full-stack Ecommerce App',
        'TeamMembers': {
            'member1': {
                'name': 'Philip Thapa',
                'rollNo': '17U61A0528',
                'email': 'philipthapa3@gmail.com',
                'phone': '8106267754',
                'from': "Nepal",
                'photo': 'https://lh3.googleusercontent.com/90-JCt7KYEFtbZE6PH-sRbbF3W0H3G_tpGjH_CE3Jpx-NmMA1wB2DtiUI8GNjToTeEqnlfcOJ06AGKGYPs5y99mUGUUabGkUzaSm1vhiGyL2yDqY35y0IwEc2Ej-NOwjsIvWrVJV2G0fWQlvf64bLCoAqBAKOobClRiLMRnMw3fzqNXDAFj0Og5RKIbp09vbYsO-1yYE9D96ZUZzUWjTkVr2Jpxd546_CexZ0sN28XWeZ-aGrnVkB3pF39R0c57NghbI06ibkLwYYGl5H0vvUgbQMwJ26U6YngUsaHRxQWJ8JUiQgA7xK6bNXQVqvk909d9ndJsT-2G72Q06h3h4h4hJWYZJQfTaBpupsKU0C0cZAcc-lw17tv9MwiR6HonIXMsFXKxwFnPANS2Adm-ycgrsSC8giHii02PkKUNFkjI2l_zoXhCxXbfz2c2laT2bKcOuNO7clG3ZEV9BhnrAPtIon4GiVnr5f7WYo8Qzp4krvuzXV0y_26s2UMz0i4_j2PooSR-nE4eWpu9yXMkkewAXS-dLbq4Cg-jnGmPgceCHSkHrQC4fccn3_dkaxsigM-MxkoXnGiUQ6S0Ro0eEDHJxbcWafFu9LcDy-RkRGah-aZDP9LYqAteDJKfWhcHl8U-RSo9K8GIqQdpvBkwwLLDjaCdSIEI_iSEeTB-rocCCFJfPjRgLKv8RwSamOA=s1400-no?authuser=0'
            },
            'member2': {
                'name': "Mohd Isbah",
                'rollNo': '17U61A0520',
                'email': 'mohammadisbah78@gmail.com',
                'phone': '9959011207',
                'from': 'Bihar',
                'photo': 'xxxx'
            }
        },
        'Language': 'Python and Javascript',
        'details': 'we are making a full stack Ecommerce App. We are using Django-v3 REST-framework in the backend and '
                   'React with Hooks in the Frontend. We are using BrainTree for payment gateway '
    })
