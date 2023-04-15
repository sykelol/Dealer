import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'virtualcargeeks.settings')
django.setup()

from base.views import generate_qr_code_with_logo
from base.models import User

if __name__ == '__main__':
    dealer_id = 19
    dealer = User.objects.get(id=dealer_id)

    if dealer and dealer.is_dealer:
        logo_path = os.path.join(os.path.dirname(__file__), 'images', 'static', 'logo12.png')
        generate_qr_code_with_logo(dealer, logo_path)
    else:
        print("No dealer found with the given ID.")