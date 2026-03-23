#make sure to install paddlepaddle
# and i have attached requiremnts.txt -- all packages for running this script
# kindly make sure to run bellow command in python environment
# python -m pip install paddlepaddle -i https://www.paddlepaddle.org.cn/packages/stable/cpu/
# --> this is installation for OCR ,and site link given so it download it from that site insted of python packages

import json
import random
import time
from paddleocr import PaddleOCR
from DrissionPage import ChromiumPage, ChromiumOptions
import tempfile
from curl_cffi import requests

def random_wait(a=1, b=2):
    t = random.uniform(a, b)
    time.sleep(t)


# Create temp profile (acts like incognito)
temp_dir = tempfile.mkdtemp()

co = ChromiumOptions()
co.set_user_data_path(temp_dir)  # fresh profile = no cookies
co.headless(False)
# wait for page load
time.sleep(5)
page = ChromiumPage(co)
page.get("https://2captcha.com/demo/normal/")
time.sleep(8)
image_src = page.ele('xpath://form//img[contains(@alt,"normal")]').attr('src')
if image_src:
    image_path = "captch_image.jpg"
    image_url = image_src
    print("image url :",image_url)
    response = requests.get(image_url,impersonate="chrome101",timeout=20)
    if response.status_code == 200:
        print("content-type:", response.headers.get("content-type"))
        print("content length:", len(response.content))
        print("first 50 bytes:", response.content[:50])
        with open(image_path,"wb") as f:
            f.write(response.content)
            print('image save successfully..')
        # make sure to install paddlepaddle
        ocr = PaddleOCR(use_doc_orientation_classify=False,
                        use_doc_unwarping=False,
                        use_textline_orientation=True)
        image_path = r"captch_image.jpg"
        result = ocr.predict(input=image_path)
        detected_text = "".join(result[0]["rec_texts"])
        print(detected_text)

        #PLACE THIS IN INPUT FILED AND THEN CLICK ON SUBMIT BUTTON
        input_ele = page.ele('xpath://input[@id="simple-captcha-field"]')
        if input_ele:
            input_ele.click()
            input_ele.input(detected_text)
            random_wait(a=1, b=2)
        else:
            print("input found issue...")

        #now button click
        button_ele = page.ele("xpath://button[@type='submit' and contains(text(), 'Check')]")
        if button_ele:
            button_ele.click()
        else:
            print("some issue found...")
        random_wait(a=3, b=4)
        success_message_show =  page.ele('xpath://p[contains(text(),"Captcha is passed successfully!")]')
        if success_message_show:
            page.run_js(f'console.log({json.dumps("OCR OUTPUT:" + detected_text)})')
            print("captch solve..")
        else:
            print("having issue in captch.....")

# =====================================================================================================

