from twocaptcha import TwoCaptcha
import requests
import time

API_KEY = '3061c419f89285010ad583ff2d1c1849'
site_key = 'af0bced3-7d4f-40ff-bded-8511552f97d1'
url = 'bestiotjobs.com'
SECRET_KEY = 'ES_25c0b936160949cf99ecd022156185d8'  # Замініть на ваш секретний ключ hCaptcha

# Step 1: Send the captcha solving request
response = requests.post('http://2captcha.com/in.php', data={
    'key': API_KEY,
    'method': 'hcaptcha',
    'sitekey': site_key,
    'pageurl': url
})

if response.status_code != 200 or response.text[0:2] != 'OK':
    print('Error sending captcha solving request')
    print(response.text)
else:
    captcha_id = response.text.split('|')[1]
    print(f'Captcha ID: {captcha_id}')

    # Step 2: Retrieve the result
    while True:
        time.sleep(5)  # Wait a few seconds before checking the result
        result_response = requests.get(f'http://2captcha.com/res.php?key={API_KEY}&action=get&id={captcha_id}')

        if result_response.text == 'CAPCHA_NOT_READY':
            continue
        elif result_response.text[0:2] == 'OK':
            captcha_code = result_response.text.split('|')[1]
            print('Captcha solved: ' + captcha_code)

            # Step 3: Verify the captcha response with hCaptcha secret key
            verification_response = requests.post('https://hcaptcha.com/siteverify', data={
                'secret': SECRET_KEY,
                'response': captcha_code
            })

            verification_result = verification_response.json()

            if verification_result['success']:
                print('Captcha successfully verified')
            else:
                print('Captcha verification failed')
                print(verification_result)

            break
        else:
            print('Error retrieving captcha result')
            print(result_response.text)
            break
